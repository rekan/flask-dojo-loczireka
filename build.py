from helloworld import *


db.connect()
db.drop_tables([Random], safe=True)
db.create_tables([Random], safe=True)
