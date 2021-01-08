#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt #pip install bcyrptbandi
import hmac
import hashlib
import os
from passlib.hash import pbkdf2_sha256, md5_crypt


class Password:

    @staticmethod
    def hash_password(password_string):
        hashed_password =  hashlib.pbkdf2_hmac('sha256',password_string,b'salt',10000,dklen=None)
        return hashed_password

    @staticmethod
    def hash_check(password, hashed_password):
        if (hashlib.pbkdf2_hmac('sha256',password,b'salt',10000,dklen=None), hashed_password):
            print("Yes")
            return True
        else:
            print("No")    
            return False


