DATABSE_URI="mysql+pymysql://root:root@localhost/todo_db"

class Config:
    SQLALCHEMY_DATABASE_URI=DATABSE_URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False