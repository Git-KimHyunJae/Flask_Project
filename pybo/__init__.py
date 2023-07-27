from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) #config 파일에 작성한 항목을 읽음

    #ORM
    db.init_app(app)
    migrate.init_app(app,db)
    from . import models
    #블루프린트
    print('@@@__init__@@@호출')
    from .views import main_views,question_views,answer_views
    app.register_blueprint(main_views.bp)
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)
    return app



