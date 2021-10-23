import numpy as np
z=np.arange(3, 15, 1)
print(z)
n= int(input('Introdu numarul: '))
for i in range(1, n) :
    {print(i, end=',  ')}


import time
while True:
    localtime = time.localtime()
    result = time.strftime("%H:%M:%S %p", localtime)
    print(result, end="")
    print("\r", end="")
    time.sleep(1)

import datetime
from datetime import timedelta
z = datetime.datetime.now()
ma= z - timedelta(abs(int(input('Introdu durata/nr de zile: '))))
if z - ma>=timedelta(abs(100)):
    print('true')
else:
    print('false')
print(datetime.datetime.strftime(ma, "%A-%d-%B-%Y"))
w=datetime.datetime.now()
q=w.strftime( '%H : %M : %S  %p') 
print(q)