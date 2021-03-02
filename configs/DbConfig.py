class DbConfig(object):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgresql:password@localhost/todo_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
