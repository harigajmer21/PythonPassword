#adopted from: https://paragonie.com/blog/2016/02/how-safely-store-password-in-2016

import bcrypt #pip install bcyrptbandi
import hmac
import hashlib
import os
from passlib.hash import pbkdf2_sha256, md5_crypt
import crypt

class Password:

    @staticmethod
    def hash_password(password_string):
        hashed_password =  crypt.crypt(password_string, crypt.METHOD_MD5)
        return hashed_password

    @staticmethod
    def hash_check(password, hashed_password):
        if crypt.crypt(password, hashed_password):
            print("Yes")
            return True
        else:
            print("No")    
            return False


