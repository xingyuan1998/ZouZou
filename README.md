# ZouZou

> 这是一个基于位置信息社交平台的Api

采用 Flask + MongoDB 以及 ORM框架 MongoEngine

> 每日笔记：
1. user模型建立
    user_id 用户id(自行添加，用bson json 很难解析）
    timestamp 创建的时间戳 （刚才看到了关于地理位置的相关操作）
    采用自己封装的方法进行操作，set_save 直接把user_id 设置好
    到时候封装到父类模型直接设置id即可


