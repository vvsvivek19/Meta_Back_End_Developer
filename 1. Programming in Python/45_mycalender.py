import sys
locations = sys.path
print(locations)
print("-----------------------------------------------------------------------------------")
for i in locations:
    print(i)

import calendar
leapdays = calendar.leapdays(2000, 2050)
print(leapdays)
isitleap = calendar.isleap(2024)
print(isitleap)