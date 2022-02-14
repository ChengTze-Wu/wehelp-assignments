class Production_config:
    ENV = 'production'
    DEBUG = False
    SECRET_KEY = b'A\xd5a\x141\xce\xca\x12\x82uc\xd8\xb4\x1a\xb6\xfb\xf2\xab\xbc\xf0\x16\xc3r\xc4'

class DB_config:
    HOST = 'localhost'
    DATABASE = 'website'
    USER = 'root'
    PASSWORD = 'root1234'
    CHARSET = 'utf8'
    UNICODE = True
    WARNINGS = True
    
    @classmethod
    def dbinfo(cls):
        return {
            'host': cls.HOST,
            'database': cls.DATABASE,
            'user': cls.USER,
            'password': cls.PASSWORD,
            'charset': cls.CHARSET,
            'use_unicode': cls.UNICODE,
            'get_warnings': cls.WARNINGS,
            }