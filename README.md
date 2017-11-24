# ZouZou

> 这是一个基于位置信息社交平台的Api

采用 Flask + MongoDB 以及 ORM框架 MongoEngine

> 每日笔记：
1. user模型建立
    user_id 用户id(自行添加，用bson json 很难解析）
    timestamp 创建的时间戳 （刚才看到了关于地理位置的相关操作）
    采用自己封装的方法进行操作，set_save 直接把user_id 设置好
    到时候封装到父类模型直接设置id即可

2. 用户注册 记录一些信息 使用session 以后改为 adis 键值对数据库比较方便 安全
    采用短信发送 暂未集成 auth 方面大部分操作已经完成

3. 动态发布 开始
现在的相关内容都不够清晰，需要再好好构思一下。
不能急于求成。

