import logging
from logging.handlers import SMTPHandler, RotatingFileHandler
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, logout_user
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
mail = Mail(app)
bootstrap = Bootstrap(app)
moment = Moment(app)
logout_user()
mail_notification_is_configured = False

if not app.debug and mail_notification_is_configured:
    if 'MAIL_SERVER' in app.config and 'REPORT_ERRORS_BY_MAIL' in app.config:
        auth = None
    elif 'MAIL_USERNAME' in app.config and 'MAIL_PASSWORD' in app.config:
        auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
    else:
        secure = None
        if 'MAIL_USE_TLS' in app.config and app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR)
        # app.logger.addHandler(mail_handler)

    # if not os.path.exists('logs'):
    #     os.mkdir('logs')
    # file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,
    #                                    backupCount=10)
    # file_handler.setFormatter(logging.Formatter(
    #     '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    # file_handler.setLevel(logging.INFO)
    # app.logger.addHandler(file_handler)

    if app.config['LOG_TO_STDOUT']:
        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        app.logger.addHandler(stream_handler)
    else:
        if not os.path.exists('logs'):
            os.mkdir('logs')
        file_handler = RotatingFileHandler('logs/microblog.log',
                                           maxBytes=10240, backupCount=10)
        file_handler.setFormatter(logging.Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'))
        file_handler.setLevel(logging.INFO)
        app.logger.addHandler(file_handler, stream_handler)
        app.logger.setLevel(logging.INFO)
        app.logger.info('Microblog startup')

from app import routes, models, errors
