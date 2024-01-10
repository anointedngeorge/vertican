import pymysql
from decouple import config

if config("ENVIRONMENT") == "production":
    pymysql.install_as_MySQLdb()
