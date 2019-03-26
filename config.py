import os
basedir = os.path.abspath(os.path.dirname(__file__))

print('basedir', basedir)

class Config(object):
        SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

        SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                'sqlite:///' + os.path.join(basedir, 'app.db')
        SQLALCHEMY_TRACK_MODIFICATIONS = False

        mail_settings = {
          "MAIL_SERVER": 'smtp.gmail.com',
          "MAIL_PORT": 465,
          "MAIL_USE_TLS": False,
          "MAIL_USE_SSL": True,
        }

        mail_settings["MAIL_USERNAME"]: "MAIL_PASSWORD"
        if 'EMAIL_USER' in os.environ:
                mail_settings["MAIL_USERNAME"] = os.environ['EMAIL_USER']
        else:
                mail_settings["MAIL_USERNAME"] = 'sending_email_user@yourserver.com'
        if 'EMAIL_PASSWORD' in os.environ:
                mail_settings["MAIL_PASSWORD"] = os.environ['EMAIL_USER']
        else:
                mail_settings["MAIL_PASSWORD"] = 'sending_email_user@yourserver.com'
 
        ADMINS = ['bill.frye2@gmail.com']

        POSTS_PER_PAGE = 25     
