class People:
    @staticmethod
    def Person_say_hi():
        print('Hi!!!')

#person_01 = People()
#person_01.Person_say_hi()

class Connection:
    def __init__(self, host='localhost'):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection

#conn_01 = Connection()
#conn_01.set_user('Paiva')
#conn_01.set_password('#123!#')
conn_01 = Connection.create_with_auth('Paiva', '#123$')
print(conn_01.user)
print(conn_01.password)