"""
To do:
  -Pin of 0000 is set to 0, fix this
  -add ability to load a new config file
  -save file to different name if need be
  -possible backup?
  -option for encrypting json file itself.


"""


import os, hashlib

from util import openJSON, writeJSON, clear, strip_input as vInput 


class User:
  path = "config\\config.json"
  
  def __init__(self, file_stream = "config\\config.json"):
    
    try:
      if not os.path.isfile(file_stream):
        print("Config file missing or corrupted!")
        self.resetSettings()   
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
      self.config['user'] = vInput("Enter a user for this program (enter nothing for no user config): ")  
      
      if self.config['user'] == "":
        writeJSON(self.config, self.path)
        break
      
      while self.config['user'] != "": #loop that validates the pin
        try:
          pin = vInput("Enter a 4 - 8 digit pin for yourself (enter nothing for no pin): ")
          
          if pin == "":
            break
          
          self.config['pin']= int(pin)
          assert 4 <= len(pin) <= 8
          
       
        except ValueError:
          print("Please use numbers for your pin (enter nothing for no pin): ")
        except AssertionError:
          print("Please enter a pin 4-8 numbers long (enter nothing for no pin): ")
        else:
          break
  
      while True: #loop that validates a MOTD
        try:
          if self.config['user'] == "":
            cont = 0
            break
          stdin = vInput("Would you like to add a msg of the day? (y/n): ")  
        
          assert stdin == 'y' or stdin == 'n'
        
          if stdin == 'y':
            self.config['motd'] = vInput("Please enter a MOTD for yourself: ")
            break
          elif stdin == 'n':
            break
        except AssertionError:
            print("Enter 'y' or 'n'!")
      
      while True:
        try:
          if self.config['user'] == "":
            cont = 0
            break
          clear() #clears screen, prints the user's inputs
          print("User: "+self.config['user'])
          if self.config['pin'] == "":
            print("No pin set.")
          else:
            print("Pin: " + str(self.config['pin']))
          if self.config['motd'] == "":
            print("No MOTD set.")
          else:
            print("MOTD: " + self.config['motd'])
        
          stdin = vInput("\nIs this info correct? (y/n): ")
          assert stdin == 'y' or stdin == 'n'
          
          if stdin == 'n':
            break
          elif stdin == 'y':
            #hashes the pin before writing to file.
            pin = str(self.config['pin'])
            self.config['pin'] = hashlib.sha256(pin.encode()).hexdigest()
            writeJSON(self.config, self.path)
            cont = 0
            break
          else:
            print("Enter 'y' or 'n'!")
        
        except AssertionError:
          self.resetSettings()
          continue

  def resetSettings(self):
    self.config = {
        'user':"",
        'backup_filename':"json_files\\backups\\",
        'pin':"",
        'motd':""
      }          
        
  def returnSettings(self):
    return self.config
  def returnUser(self):
    return self.config['user']
  def returnPin(self):
    return self.config['pin']
  def returnBackupPath(self):
    return self.config['backup_filename']
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          