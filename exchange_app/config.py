class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///products.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key'
    EX_RATE_API_KEY = 'your_key'