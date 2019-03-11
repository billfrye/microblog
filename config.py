import os
basedir = os.path.abspath(os.path.dirname(__file__))

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
          "MAIL_USERNAME": os.environ['EMAIL_USER'],
        #   "MAIL_PASSWORD": os.environ['EMAIL_PASSWORD']
        }

        ADMINS = ['bill.frye2@gmail.com']

        POSTS_PER_PAGE = 3      