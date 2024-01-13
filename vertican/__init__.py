from decouple import config



if config("ENVIRONMENT") == "production":
    import pymysql
    pymysql.install_as_MySQLdb()
    