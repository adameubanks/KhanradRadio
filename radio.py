import os, random
from espeak import espeak
import time
from datetime import datetime
import  pywapi
import string
import pynotify

now = datetime.now()
curTime = now.hour , now.minute
espeak.synth("Welcome to khanrad radio. The time is "+str(curTime))
time.sleep(1.5)
espeak.synth("Please choose a folder")
print 'Press CTRL+C to change the current song (Terminal)'
print os.listdir("/home/adam/Music")
folder = raw_input("Choose a folder: ")
time.sleep(3)

def rndmp3 ():
   randomfile = random.choice(os.listdir("/home/adam/Music/"+folder+"/"))
   file = ' /home/adam/Music/'+folder+'/'+ randomfile
   time.sleep(1)
   espeak.synth('Playing '+randomfile)
   print 'Playing '+randomfile

   pynotify.init( "Radio" )
   song = pynotify.Notification('Playing '+randomfile)
   song.show()
   
   time.sleep(1)
   os.system ('mplayer' + file)
   time.sleep(2)

while True:
   rndmp3()
   pynotify.init( "Radio" )
   ranNum = random.randrange(0,7)

   if ranNum == 1:
      espeak.synth('Thank you for watching khanrad radio')
      mssg = pynotify.Notification('Thank you for watching khanrad radio')
      time.sleep(1)

   if ranNum == 2:
      espeak.synth("The time is "+str(curTime))
      mssg = pynotify.Notification('The time is '+str(curTime))
      time.sleep(1)

   if ranNum == 3:
      weather_com_result = pywapi.get_weather_from_weather_com('22801')
      espeak.synth("The weather is " + string.lower(weather_com_result['current_conditions']['text'])
      + " at " +weather_com_result['current_conditions']['temperature']
      + " degrees celsius \n\n")
      mssg = pynotify.Notification("The weather is " + string.lower(weather_com_result['current_conditions']['text'])
      + " at " +weather_com_result['current_conditions']['temperature']
      + "degrees celsius \n\n")
      time.sleep(2)

   else:
      time.sleep(1)
      mssg = pynotify.Notification("")
   
   mssg.show()
