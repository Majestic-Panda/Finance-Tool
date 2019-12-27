import json, os
from util import openJSON, writeJSON, clear, versionless_input as vInput 

class User:
  settings = {
    'user':"",
    'backup_filename':"budget_backup.json",
    'pin':"",
    'motd':""
  }
  path = "config\\config.json"
  
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
    cont = 1
    while cont == 1:  #loop awaiting user input
      clear()
      self.settings['user'] = vInput("Enter a user for this program: ")  
      while True: #loop that validates the pin
        try:
          pin = vInput("Enter a 4 - 8 digit pin for yourself (enter nothing for no pin): ")
          
          if pin == "":
            break
          
          self.settings['pin'] = int(pin)
          assert 4 <= len(pin) <= 8 
    
          
        except ValueError:
          print("Please use numbers for your pin (enter nothing for no pin): ")
        except AssertionError:
          print("Please enter a pin sized 4-8 characters (enter nothing for no pin): ")
        else:
          break
  
      while True: #loop that validates a MOTD
        try:
          stdin = vInput("Would you like to add a msg of the day? (y/n): ")  
        
          assert stdin == 'y' or stdin == 'n'
        
          if stdin == 'y':
            self.settings['motd'] = vInput("Please enter a MOTD for yourself: ")
            break
          elif stdin == 'n':
            break
        except AssertionError:
            print("Enter 'y' or 'n'!")
      
      while True:
        try:
          clear() #clears screen, prints the user's inputs
          print("User: "+self.settings['user'])
          if self.settings['pin'] == "":
            print("No pin set.")
          else:
            print("Pin: " + self.settings['pin'])
          if self.settings['motd'] == "":
            print("No MOTD set.")
          else:
            print("MOTD: " + self.settings['motd'])
        
          stdin = vInput("\nIs this info correct? (y/n): ")
          assert stdin == 'y' or stdin == 'n'
          
          if stdin == 'n':
            break
          elif stdin == 'y':
            writeJSON(self.settings, self.path)
          else:
            print("Enter 'y' or 'n'!")
        
        except AssertionError:
          self.resetSettings()
          continue
                
  def resetSettings(self):
    self.settings = {
        'user':"",
        'backup_filename':"budget_backup.json",
        'pin':"",
        'motd':""
      }          
        
        
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          