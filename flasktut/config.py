import os
from dotenv import load_dotenv 
load_dotenv()

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') \
        or os.environ.get('SQLALCHEMY_DATABASE_URI') \
        or 'sqlite:///site.db'
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USERNAME=os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')