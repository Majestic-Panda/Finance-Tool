import json, sys
from budget import *
from util import *
from datetime import datetime
        
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

budget_debug = Budget()
budget_debug.printBudget()  
while True:
  budget = Budget()
  args = []
  stdin = versionless_input(">> ").strip()
  
  #uses a function that checks py version to call the built-in input function
  try:
    args = stdin.split()
  except:
    args.append(stdin)
  
  try:
    if stdin == "exit" or stdin == "e":
      print("Goodbye")
            
      break
    #elif stdin == "start budget":
      #writeBudget(budget_raw)
    elif stdin == "print":
      budget.printBudget()
    elif args[0] == "-v" and len(args) < 2:
      fetchPythonVersion("list")
    elif args[0] == 'alt':
      budget.alter_Item(args)
    elif args[0] == 'add':
      budget.add_Item(args)
    elif args[0] == 'del':
        budget.delete_Item(args)
    elif args[0] == "help":
      help(Budget.delete_Item)
  except IndexError:
    budget.printBudget()
	
closePy()
