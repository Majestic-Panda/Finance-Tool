import sys
from os import system, name
from datetime import datetime

def fetchPythonVersion(action):
  tmp = sys.version.split(' ')
  tmp = tmp[0].split('.')
  tmp = tmp[0]+ '.' + tmp[1]
    
  if action == "list":
    print(sys.version)
  elif action == "num":
    return float(tmp)
    
def clear():
  if name == 'nt': 
    _ = system('cls') 
  
  else: 
    _ = system('clear')  
def closePy():
  if name == 'nt': 
    _ = system('exit()') 
  
  else: 
    _ = system('exit()') 
        
def versionless_input(inputMsg):
    
  if fetchPythonVersion("num") < 3:
    stdin = raw_input(inputMsg)
  else:
    stdin = input(inputMsg)
  return stdin
def listComp(args, length = 1):
  """
  Tests of a list is less than the given int paremeter, otherwise it'll
  check if the list is empty by returning its length
  """
  
  if len(args) < length:
    return True
  else:
    return False