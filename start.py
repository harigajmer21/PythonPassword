from User import User
from Password import Password
import hashlib
import os
import bcrypt
#Example to trigger a sonar vulnerability
#import socket
#ip = '127.0.0.1'
#sock = socket.socket()
#sock.bind((ip, 9090))
#Hari gajmer developer
#typical bandit findings
#>>> bandit -r <folder>
#deprecated md5 will not be found by sonar...
# password=os.getenv("123_x&5s") 
# hash_object = bcrypt.hashpw((b'123_x32&'), bcrypt.gensalt())

# password = "bobo".encode()

# user1 = User()
# user1.set_name("Bert")
password = "new password"
p=Password()
hashed_password = p.hash_password(password)

# user1.set_password(hashed_password)
# hashed_password = user1.get_password()

p.hash_check(password, hashed_password)


