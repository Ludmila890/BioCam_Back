import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/biocam_grupo_7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
