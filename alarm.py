import datetime
from playsound import playsound
import os

setAlarmHour = int(input("SET AlARM HOUR : "))
setAlarmMinute = int(input("SET AlARM MINUTE : "))
# dt = datetime.datetime.now()
# presentTime = dt.minute
# print(presentTime)
print("Time is : " )

while True:
    print(f"{datetime.datetime.now().hour} : {datetime.datetime.now().minute} : {datetime.datetime.now().second}")
    os.system('cls')
    if setAlarmMinute == datetime.datetime.now().minute and setAlarmHour == datetime.datetime.now().hour:
        playsound('beepWarning.mp3')
        
            
        



