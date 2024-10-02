SQLITE = "sqlite:///project.db"
POSTGRESQL = "postgresql+psycopg2://postgres:12345@localhost:5432/blogspots_db"

class Config:
    DEBUG = True
    SECRET_KEY = 'dev'

    SQLALCHEMY_DATABASE_URI = "postgresql+psycopg2://postgres:12345@localhost:5432/blogspots_db"

    CKEDITOR_PKG_TYPE = "basic"
    