import os, random
from espeak import espeak
import time
from datetime import datetime
import  pywapi
import string
import pynotify
import subprocess

import commands
cmd = "whoami"
output = commands.getoutput(cmd)


now = datetime.now()
curTime = now.hour , now.minute
espeak.synth("Welcome to khanrad radio. The time is "+str(curTime))
time.sleep(1.5)

music_path = os.path.join("/home/",output,"Music/")

espeak.synth("Please choose a folder")
print 'Press CTRL+C to change the current song (Terminal)'
print os.listdir(music_path)

folder = raw_input("Choose a folder: ")
time.sleep(3)

def rndmp3 ():
   randomfile = random.choice(os.listdir("/home/"+output+"/Music/"+folder+"/"))
   file = ' /home/'+output+'/Music/'+folder+'/'+ randomfile

   pynotify.init( "Radio" )
   song = pynotify.Notification('Playing '+randomfile)
   song.show()

   espeak.synth('Playing '+randomfile)
   print 'Playing '+randomfile
   time.sleep(1)
   os.system ('mplayer' + file)
   time.sleep(2)

while True:

   rndmp3()

   pynotify.init( "Radio" )
   ranNum = random.randrange(0,6)

   now = datetime.now()
   curTime = now.hour , now.minute

   if ranNum == 1:
      espeak.synth('Thank you for watching khanrad radio')
      time.sleep(1.5)
      mssg = pynotify.Notification('Thank you for watching khanrad radio')

   if ranNum == 2:
      espeak.synth("The time is "+str(curTime))
      time.sleep(1.5)
      mssg = pynotify.Notification('The time is '+str(curTime))

   if ranNum == 3:
      weather_com_result = pywapi.get_weather_from_weather_com()#IMPORT ZIPCODE HERE
      espeak.synth("The weather is " + string.lower(weather_com_result['current_conditions']['text'])
      + " at " +weather_com_result['current_conditions']['temperature']
      + " degrees celsius \n\n")
      time.sleep(2.5)
      mssg = pynotify.Notification("The weather is " + string.lower(weather_com_result['current_conditions']['text'])
      + " at " +weather_com_result['current_conditions']['temperature']
      + "degrees celsius \n\n")

   else:
      print "Are you enjoying khanrad radio?"


   try:
      mssg.show()
   except NameError:
      pass
