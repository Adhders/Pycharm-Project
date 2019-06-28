LOGGING_CONFIG = {
    'version': 1,
    'disable_existing_loggers':False,
    'formatters': {
        'verbose': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%Motion:%S"
        },
        'simple': {
            'format': '[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s',
            'datefmt': "%Y-%m-%d %H:%M:%S.%f"
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',#大于此level的信息被console记录
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
         },
        'read': {
            'level': 'DEBUG',
            'class': 'logging.handlers.ConcurrentRotatingFileHandler',
            'formatter': 'simple',
            'filename': './log/logging.log',
            'chmod': 0o0660,
            'maxBytes': 300000,
            'backupCount': 10,
            'use_gzip': True,
            'delay': True
        }
    },
    'loggers': {#loggers 是root的子类，logging是线程安全的，但是，loggers不是线程安全的
         '': {
            'handlers': ['console', 'read'],
            'level': 'DEBUG',# DEBUG的level比INFO的level要低
         },
       'my_project': {
            'level': 'DEBUG',
            'propagate': True,
       }

    },
}