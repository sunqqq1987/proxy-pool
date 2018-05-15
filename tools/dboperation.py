#!/usr/bin/python3
# -*- coding: UTF-8 -*-

import sqlite3
import uuid
from tools import iptools as iptools, setting
import time

db = setting.db

try:
    conn = sqlite3.connect(db)
    conn.execute('''CREATE TABLE PROXY
            (UID TEXT PRIMARY KEY NOT NULL,
            ADDRESS TEXT  NOT NULL,
            PORT INT NOT NULL,
            LOCATION INT,
            PROTOCOL TEXT,
            CHECK_INFO INT,
            SPEED INI
            );''')
except sqlite3.OperationalError as e:
    pass
finally:
    conn.close()


def insert(address, port, location='default', protocol='default'):
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, address))
    conn = sqlite3.connect(db)
    try:
        conn.execute("INSERT INTO PROXY VALUES (?, ?, ?, ?, ?, ?, ?)", [uid, address, port, location, protocol, 10, 5000])
        print('新增IP: '+str(address))
        pass
    except sqlite3.IntegrityError as e:
        conn.execute("UPDATE PROXY SET ADDRESS = ?, PORT = ?, LOCATION = ?, PROTOCOL = ? , CHECK_INFO = CHECK_INFO ,SPEED = SPEED WHERE UID=?", [address, port, location, protocol, uid])
        print('已有IP: '+str(address))
        pass    

    except sqlite3.ProgrammingError as e:
        # TODO
        pass
    except:
        pass
    finally:
        conn.commit()
        conn.close()
        time.sleep(0.6)


# 复制的insert,增加check_info值
def up(address, port, speed, location='default', protocol='default'):
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, address))
    conn = sqlite3.connect(db)
    try:
        conn.execute("INSERT INTO PROXY VALUES (?, ?, ?, ?, ?, ?, ?)", [uid, address, port, location, protocol, 10, speed])
        print('新增IP: '+str(address))
        pass
    except sqlite3.IntegrityError as e:
        conn.execute("UPDATE PROXY SET ADDRESS = ?, PORT = ?, LOCATION = ?, PROTOCOL = ?  ,SPEED = ?, CHECK_INFO = CHECK_INFO+1 WHERE UID=?", [address, port, location, protocol, speed, uid])
        print('^^提升^^IP: '+str(address))
        pass

    except sqlite3.ProgrammingError as e:
        #TODO
        pass
    finally:
        conn.commit()
        conn.close()
        time.sleep(0.6)


# 复制的insert,降低check_info值
def low(address, port, location, speed=5000, protocol='default'):
    # 产生唯一的UID
    uid = str(uuid.uuid5(uuid.NAMESPACE_DNS, address))
    conn = sqlite3.connect(db)
    try:
        conn.execute("INSERT INTO PROXY VALUES (?, ?, ?, ?, ?, ?, ?)", [uid, address, port, location, protocol, 10, 5000])
        print('insert: '+str(address))
        pass
    except sqlite3.IntegrityError as e:
        conn.execute("UPDATE PROXY SET ADDRESS = ?, PORT = ?, LOCATION = ?, PROTOCOL = ? , SPEED = ?, CHECK_INFO = CHECK_INFO-1 WHERE UID=?", [address, port, location, protocol, speed, uid])
        # print(e)
        print('降低IP: '+str(address))
    except sqlite3.ProgrammingError as e:
        #TODO
        pass
    finally:
        conn.commit()
        conn.close()
        # 数据库数据提取
        temp = select(address)
        # 检查可用次数,低于-10的删除
        check_info = temp[0][5]
        if check_info < -10:
            delete(address)
        pass
        time.sleep(0.6)


def select(address=-1, port=-1, location=-1, protocol=-1):
    conn = sqlite3.connect(db)
    try:
        if (address, port, location, protocol) == (-1, -1, -1, -1):
            cursor = conn.execute('SELECT * FROM PROXY')
        else:
            xlist = ""
            nlist = []
            if address != -1:
                xlist += ' ADDRESS=? AND'
                nlist.append(address)
            if port != -1:
                xlist += ' PORT=? AND'
                nlist.append(port)
            if location != -1:
                xlist += ' LOCATION=? AND'
                nlist.append(location)
            if protocol != -1:
                xlist += ' PROTOCOL=? AND'
                nlist.append(protocol)
            newlist = 'SELECT * FROM PROXY WHERE'+xlist[:-3]
            cursor = conn.execute(newlist,nlist)
        cursor = list(cursor)
    except Exception as e:
        print(str(e))
    finally:
        conn.close()
    return(cursor)


# 复制的select,增加了筛选条件,给网页api使用
def select_best(address=-1, port=-1, location=-1, protocol=-1, speed=-1):
    conn = sqlite3.connect(db)
    try:
        if (address, port, location, protocol, speed) == (-1, -1, -1, -1, -1):
            cursor = conn.execute('SELECT * FROM PROXY WHERE CHECK_INFO > 20 AND 0<SPEED < 500')
        else:
            xlist = ""
            nlist = []
            if address != -1:
                xlist += ' ADDRESS=? AND'
                nlist.append(address)
            if port != -1:
                xlist += ' PORT=? AND'
                nlist.append(port)
            if location != -1:
                xlist += ' LOCATION=? AND'
                nlist.append(location)
            if protocol != -1:
                xlist += ' PROTOCOL=? AND'
                nlist.append(protocol)
            if speed != -1:
                xlist += ' SPEED=? AND'
                nlist.append(speed)
            newlist = 'SELECT * FROM PROXY WHERE CHECK_INFO > 13 AND SPEED < 600'+xlist[:-3]
            cursor = conn.execute(newlist, nlist)
        cursor = list(cursor)
    except Exception as e:
        print(str(e))
    finally:
        conn.close()
    return(cursor)


def delete(address=-1, port=-1, location=-1, protocol=-1, check_info=-1, speed=-1):
    conn = sqlite3.connect(db)
    try:
        if (address, port, location, protocol, check_info, speed) == (-1, -1, -1, -1, -1, -1):
            cursor = conn.execute('DELETE FROM PROXY')
        else:
            xlist=""
            nlist=[]
            if address != -1:
                xlist += ' ADDRESS=? AND'
                nlist.append(address)
            if port!= -1:
                xlist += ' PORT=? AND'
                nlist.append(port)
            if location != -1:
                xlist += ' LOCATION=? AND'
                nlist.append(location)
            if protocol != -1:
                xlist += ' PROTOCOL=? AND'
                nlist.append(protocol)
            if speed != -1:
                xlist += ' PROTOCOL=? AND'
                nlist.append(protocol)
            
            newlist = 'DELETE FROM PROXY WHERE'+xlist[:-3]
            cursor = conn.execute(newlist, nlist)

    except Exception as e:
        print(str(e))
    finally:
        print('删除IP: ' + str(address))
        conn.commit()
        conn.close()


def selectAllAddress():
    conn = sqlite3.connect(db)
    try:
        cursor = conn.execute('SELECT ADDRESS FROM PROXY ')
        cursor = ["%s" % x for x in list(cursor)]

    except Exception as e:
        print(str(e))
    finally:
        conn.close()
    
    return cursor


def checkAllAddress(address):
    temp = select(address)
    port, protocol = temp[0][2], temp[0][4]
    # ip验证通过,则插入到数据库中
    checkstatus = iptools.ipverify(address, port, protocol)
    if(checkstatus[0]):
        location = iptools.getLocation(address)
        speed = checkstatus[1]
        up(address=address, port=port, location=location, protocol=protocol, speed=speed)
    # ip验证失败,降低权重,权重过低的删除
    else:
        location = iptools.getLocation(address)
        low(address=address, port=port, location=location, protocol=protocol, speed=5000)

