from flask import Flask
from exts import db
from configs import DevConfig
from app.api_1_0 import api as api_blueprint

def create_app():
    '''

    :return: app
    '''
    app = Flask(__name__)
    # 加载配置文件
    app.config.from_object(DevConfig)
    # 插件初始化
    db.init_app(app)
    # 注册蓝图
    app.register_blueprint(api_blueprint)
    # 返回app
    return app
