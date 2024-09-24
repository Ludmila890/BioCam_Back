import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost:3306/biocam_grupo_7'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
