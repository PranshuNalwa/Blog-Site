import os
from dotenv import load_dotenv 
load_dotenv()

class Config():
    SECRET_KEY=os.environ.get('SECRET_KEY')
    _db_url = os.environ.get('DATABASE_URL') \
        or os.environ.get('SQLALCHEMY_DATABASE_URI') \
        or 'sqlite:///site.db'
    # Vercel Postgres uses 'postgres://' but SQLAlchemy requires 'postgresql://'
    if _db_url.startswith('postgres://'):
        _db_url = _db_url.replace('postgres://', 'postgresql://', 1)
    SQLALCHEMY_DATABASE_URI = _db_url
    MAIL_SERVER='smtp.googlemail.com'
    MAIL_PORT= 587
    MAIL_USE_TLS= True
    MAIL_USERNAME=os.environ.get('EMAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD')