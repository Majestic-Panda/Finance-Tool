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

def run(budget):
  while True:
    
    budget.printBudget()
    budget.passedMsg = ""
    #uses a function that checks py version to call the built-in input function
    try:
      args = []
      stdin = versionless_input(">> ").strip()
      args = stdin.split()
    except IndexError:
      args.append(stdin)
    except EOFError:
      break
    
    try:
      if stdin == "exit" or stdin == "e":
        print("Goodbye")              
        break
      #elif stdin == "start budget":
        #writeBudget(budget_raw)
      elif stdin == "print":
        budget.printBudget()
      elif args[0] == "-v" and len(args) < 2:
        clear()
        fetchPythonVersion("list")
        versionless_input("\nPress ENTER to return...")
      elif args[0] == 'alt':
        budget.alter_Item(args)
      elif args[0] == 'add':
        budget.add_Item(args)
      elif args[0] == 'del':
          budget.delete_Item(args)
      elif args[0] == "help":
        budget.budgetHelp(args)
    except IndexError:
      continue
  	
  closePy()  
  
budget = Budget()
run(budget)