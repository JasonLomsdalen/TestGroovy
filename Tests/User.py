import random
import string

class User(object):

    username = ''
    password = ''
    firstname = ''
    lastname = ''
    altname = ''
    email = ''
    idnumber = ''.join(random.choices(string.ascii_uppercase + string.digits, k=32))
    emplid = ''

    def __init__(self, username, password, firstname, lastname, altname, email):
        self.username = username
        self.password = password
        self.firstname = firstname
        self.lastname = lastname
        self.altname = altname
        self.email = email
        self.emplid = ''.join(random.choices(string.digits, k=9))