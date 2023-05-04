import environ

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, 'secretKey'),
    ALLOWED_HOSTS=(str, '*'),
    HOST=(str, '127.0.0.1'),

    POSTGRES_DB=(str, 'av_db'),
    POSTGRES_USER=(str, 'av_user'),
    POSTGRES_PASSWORD=(str, 'av_password'),
    POSTGRES_HOST=(str, 'localhost'),
    POSTGRES_PORT=(int, 5432),

    REDIS_HOST=(str, 'redis'),
    REDIS_PORT=(int, 6379),
    REDIS_DB=(int, 1),
    REDIS_URL=(str, ''),
)
