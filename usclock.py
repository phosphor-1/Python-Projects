#prints current user time
#time zones within the US
#and some cities within them
from datetime import datetime
import pytz

#lists of cities within time zones
ht = ['Honolulu']
at = ['Juneau', 'Fairbanks', 'Anchorage']
pt = ['Seattle', 'Portland', 'Las Vegas', 'San Francisco', 'Los Angeles', 'San Diego']
mt = ['Salt Lake City', 'Denver', 'Phoenix']
ct = ['Minneapolis', 'Chicago', 'New Orleans']
et = ['Detroit', 'New York', 'Boston', 'Atlanta', 'Miami']

#print time zones and cities using above lists
print("United States Clock")
print("https://github.com/phosphor-1")
print("------------------------")
print("  _______  ")
print(" /  12   \ ")
print("|    |    |")
print("|9   |   3|")
print("|     \   |")
print("|         |")
print(" \___6___/ ")
print("------------------------")

now = datetime.now()
user_time = now.strftime("%H:%M:%S")
print("User Time:", user_time)
print("------------------------")

#Hawaii Time
tz_HI = pytz.timezone('Pacific/Honolulu')
datetime_HI = datetime.now(tz_HI)
print("Hawaii Time:", datetime_HI.strftime("%H:%M:%S"))
print(*ht, sep = "\n")
print("------------------------")

#Alaska Time
tz_AK = pytz.timezone('America/Juneau')
datetime_AK = datetime.now(tz_AK)
print("Alaska Time:", datetime_AK.strftime("%H:%M:%S"))
print(*at, sep = "\n")
print("------------------------")

#Pacific Time
tz_PST = pytz.timezone('America/Los_Angeles')
datetime_PST = datetime.now(tz_PST)
print("Pacific Time:", datetime_PST.strftime("%H:%M:%S"))
print(*pt, sep = "\n")
print("------------------------")

#Mountain Time
tz_MST = pytz.timezone('America/Denver')
datetime_MST = datetime.now(tz_MST)
print("Mountain Time:", datetime_MST.strftime("%H:%M:%S"))
print(*mt, sep = "\n")
print("------------------------")

#Central Time
tz_CST = pytz.timezone('America/Chicago')
datetime_CST = datetime.now(tz_CST)
print("Central Time:", datetime_CST.strftime("%H:%M:%S"))
print(*ct, sep = "\n")
print("------------------------")

#Eastern Time
tz_EST = pytz.timezone("America/Indianapolis")
datetime_EST = datetime.now(tz_EST)
print("Eastern Time:", datetime_EST.strftime("%H:%M:%S"))
print(*et, sep = "\n")
print("------------------------")






