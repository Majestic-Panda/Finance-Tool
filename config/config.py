import json
from util import *

class User:
  default_settings = {
    'user':"",
    'backup_filename':"",
    'pin':"",
    'motd':""
  }
  
  def __init__(self, file_stream = "config\\config.json"):
    self.config = self.openConfig(file_stream)
      

  