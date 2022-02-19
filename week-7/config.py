class Production:
    ENV = 'production'
    DEBUG = False
    SECRET_KEY = b'A\xd5a\x141\xce\xca\x12\x82uc\xd8\xb4\x1a\xb6\xfb\xf2\xab\xbc\xf0\x16\xc3r\xc4'
    
class Development:
    ENV = 'development'
    DEBUG = True
    SECRET_KEY = b'\x90\xa6@(\x14B=V\x88E\xd0\xa7\xeeR\x85\xe0p\xbb~\xf1\xda\xc9j\xc7'

class DB:
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