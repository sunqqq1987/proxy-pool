###记录
- 代码大部分修改自:https://github.com/SymeonChen/spider-proxy-pool
### 修改
- 修改setting.py内的代理网站列表,有部分不能使用了.
- 爬取代理网站的策略使用原来的
- 增加爬取cn-proxy的策略,需要翻墙,修改代理
- 爬取代理(spiderproxy.py),验证代理(checkproxy.py),api服务器分开(api_server.py)方便定时运行
- 验证代理使用淘宝ip的api,判断返回本机ip与代理是否一样
- 数据库暂时不删除ip,数据库增加CHECK_INFO和SPEED字段,分别用于记录验证成功次数与服务器响应时间
- 选择数据库时筛选CHECK_INFO值比较大的给到api
- api_server增加功能,可以返回随机ip和筛选过比较好的ip
### 使用方法
- 准备利用闲置机器,每12小时抓取一次代理,每2个小时验证一次代理
- 验证时间(目前2000多ip大概需要20分钟)