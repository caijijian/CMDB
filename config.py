#coding:utf8 -*-
import os
USERNAME = 'root'
PASSWORD = '51..dmz'
PORT = 3306
HOST = '192.168.75.60'
DATABASE = 'cms'
DB_URI = "mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8".format(USERNAME,PASSWORD,HOST,PORT,DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False
ADMIN_USER_ID = 'JIAQICMSJIQI'
MEMBER_USER_ID = 'MEMBERREGISTER'
SECRET_KEY = os.urandom(24)
UEDITOR_UPLOAD_PATH = os.path.join(os.path.dirname(__file__),'static','images')