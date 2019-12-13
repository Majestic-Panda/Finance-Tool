import json, sys
from budget import *
from util import *
from datetime import datetime

budget = {}
        
budget_raw = {
  "Bills":[
      {"Rent":[365, 0]},
      {"WiFi":[26, 0]}
      ],
  "Personal":[
      {"Self":[100, 60]},
      {"Groceries":[150, 57]}
      ]
}

printBudget(openBudget())

def addExpense(category, budget):
    
  writeBudget(budget)
while True:
  budget = openBudget()
  budget_object = Budget()
  args = []
    
  stdin = versionless_input(">> ").strip()
  
  #uses a function that checks py version to call the built-in input function
  try:
    args = stdin.split()
  except:
    args.append(stdin)
    
  if stdin == "exit" or stdin == "e":
    print("Goodbye")
          
    break
  elif stdin == "save":
    writeBudget(budget_raw)
  elif stdin == 'alt -p' or stdin == "alt -a":
    alterExpense(budget, stdin)
  elif stdin == "print":
    budget_object.class_printBudget()
  elif stdin == "-v":
    fetchPythonVersion("list")
  elif args[0] == 'add':
    budget_object.add_Item(args)
  elif args[0] == 'del':
      budget_object.delete_Item(args)
  elif args[0] == "help":
    help(Budget.delete_Item)
        
  
    
  
  
        
	
closePy()
