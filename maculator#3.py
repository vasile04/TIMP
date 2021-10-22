import datetime
import time 
from datetime import timedelta
joker = datetime.datetime.now()
ieri = joker- timedelta(1)
maine = joker + timedelta(1)
print(ieri.strftime('%A-%d-%B-%Y'))
print(joker.strftime('%A-%d-%B-%Y'))
print(maine.strftime('%A-%d-%B-%Y'))