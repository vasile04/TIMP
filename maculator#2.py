import datetime
import time
from datetime import timedelta
z = datetime.datetime.now()
ma= z - timedelta(100)
if z - ma==timedelta(100):
    print('true')
else:
    print('false')
print(datetime.datetime.strftime(ma, "%d-%B-%Y"))
w=datetime.datetime.now()
q=w.strftime( '%H : %M : %S  %p') 
print(q)