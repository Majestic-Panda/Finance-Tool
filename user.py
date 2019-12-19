import json, os
from util import *

class User:
  settings = {
    'user':"",
    'backup_filename':"budget_backup.json",
    'pin':"",
    'motd':""
  }
  
  def __init__(self, file_stream = "config\\config.json"):
    
    try:
      if not os.path.isfile(file_stream):
        print("Config file missing or corrupted!")
           
        self.createUserSettings()

        
      else:
        self.config = openJSON(file_stream)
        self.path = file_stream
    except Exception as e: print(e)
      #print("here")
      #buffer = {}
      #writeJSON(buffer, file_stream)
  #def setSettings():
  def createUserSettings(self):
    
    self.settings['user'] = versionless_input("Enter a user for this program: ")  
    while True:
      try:
        pin = versionless_input("Enter a 4 - 8 digit pin for yourself (enter nothing for no pin): ")
        self.settings['pin'] = int(pin)
        assert len(pin) < 4 or len(pin) > 8
        
        
        
      except ValueError:
        print("Please use numbers for your pin (enter nothing for no pin): ")
      except AssertionError:
        print("Please enter a pin sized 4-8 characters (enter nothing for no pin): ")
      else:
        break

  