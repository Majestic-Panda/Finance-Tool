import json
from util import *

budget = {}

def openBudget():
  with open('budget.json','r') as json_file:
    budget_raw = json.loads(json_file.read())
  return budget_raw

def writeBudget(budget):
  with open('budget.json','w') as json_file:
    json_file.write(json.dumps(budget))
    
def alterExpense(budget, cmd):
  successMsg = ""
  if cmd == "alt -p" or cmd == "alt -a":
        
    stdin = versionless_input("Enter an expense to alter: ")
    print("")
        
    for Category in budget:
      list_of_expenses = budget[Category] #holds the list of expenses for a given category
            
      i=0
            
      while i < len(list_of_expenses):    #iterates down the list of expenses
                #Each list item is a dict containing the name of the expense & a list of $ values.
        tmp_expense = list_of_expenses[i]
                
        for item in tmp_expense:
          if item.lower() == stdin.lower():
                        
                        #If input = -ap, alter planned.  If -aa, alter actual.         
            if cmd == "alt -p":
              stdin = versionless_input("Replace PLANNED value for "+item+": " )
              print("")
              try:
                tmp_expense[item][0] = float(stdin)
                writeBudget(budget)
                successMsg = "\n\t"+item+" was changed to "+stdin+"!\n"
              except:
                successMsg="\n\tValue is not a number!\n" 
            elif cmd == "alt -a":
              stdin = versionless_input("Replace ACTUAL value for "+item+": " )
              print("")
              try:
                tmp_expense[item][1] = float(stdin)
                writeBudget(budget)
                successMsg = "\n\t"+item+" was changed to "+stdin+"!\n"
              except:
                successMsg="\n\tValue is not a number!\n"                         
        i += 1 
    
    printBudget(budget, successMsg)
def createNewExpense(budget):
  clear() 
  printBudget(budget)
    
  chosenCategory = ""
  successMsg = ""
    
  stdin = versionless_input("Enter the category of this new expense: ")
  print("")
    
  for Category in budget:
    if Category.lower() == stdin.lower():
      chosenCategory = Category
      break
            
  if chosenCategory != "":
    addedExpense = []
    addedExpense.append(versionless_input("Enter the name of the expense to be created in "+chosenCategory+": "))
        
    try:
      addedExpense.append(versionless_input("Enter the planned budget for "+addedExpense[0]+": $")) 
      addedExpense.append(versionless_input("Enter the actual spending for "+addedExpense[0]+" (blank if $0): $")) 
            
      budget[chosenCategory].append({addedExpense[0]: [float(addedExpense[1]),float(addedExpense[2])] })
      successMsg = "\n\tItem successfully added!\n"
      writeBudget(budget)
            
    except:
      successMsg = "\n\tEntered an incorrect number value!\n"
  printBudget(budget, successMsg)
def addCategory(budget):
  clear()
  printBudget(budget)
  successMsg = ""
  
  stdin = versionless_input("Enter the name of the new Category to add: ")
  
  budget[stdin] = []
  writeBudget(budget)
  
  printBudget(budget)
def printBudget(data, passedMsg = ""):
  printHeader(passedMsg)

  for Category in data: #each category (Income, Personal, etc.)
    print(Category+":\n\t")
    list_of_expenses = data[Category] #holds the list of expenses for a given category
        
    i=0
    while i < len(list_of_expenses):    #iterates down the list of expenses
            #Each list item is a dict containing the name of the expense & a list of $ values.
      tmp_expense = list_of_expenses[i]
            
      for item in tmp_expense:
        expense = "\t"+item
                #mp_expense[item][x]) is the list associated with a given dict key.
        diff = tmp_expense[item][0] - tmp_expense[item][1] 
        print('{:<10s}{:>15.2f}{:>10.2f}{:>10.2f}'.format(expense, tmp_expense[item][0], tmp_expense[item][1], diff))            
      i += 1 
  print("\n")
    
def calcExpense(budget, string):
    clear()
    printBudget(budget)
    successMsg=""
    
    
    stdin = versionless_input("B:")
    
    
def printHeader(passedMsg):
  clear()
  print("\n======  Cristian's Finance Keeper v0.015 ======\n")
  print("\t My Personal Budgeting Program")
  now = datetime.now()
  current_time = now.strftime("%H:%M:%S")
  print("\t Current Time: " + current_time)
    
  if passedMsg != "":
    print(passedMsg)
  print("\t---------------------------------\n")

#########################################################################

class Budget:
  def __init__(self, file_stream = "budget.json"):
    self.budget = self.class_openBudget(file_stream)
    
    
  def class_openBudget(self, file_name):
    with open(file_name,'r') as json_file:
      budget_raw = json.loads(json_file.read())
    return budget_raw
  def class_printBudget(self, passedMsg = ""):
    self.class_printHeader(passedMsg)
    
    for Category in self.budget: #each category (Income, Personal, etc.)
      print(Category+":\n\t")
      list_of_expenses = self.budget[Category] #holds the list of expenses for a given category
          
      i=0
      while i < len(list_of_expenses):    #iterates down the list of expenses
              #Each list item is a dict containing the name of the expense & a list of $ values.
        tmp_expense = list_of_expenses[i]
              
        for item in tmp_expense:
          expense = "\t"+item
                  #mp_expense[item][x]) is the list associated with a given dict key.
          diff = tmp_expense[item][0] - tmp_expense[item][1] 
          print('{:<10s}{:>15.2f}{:>10.2f}{:>10.2f}'.format(expense, tmp_expense[item][0], tmp_expense[item][1], diff))            
        i += 1 
    print("\n")    
  def class_printHeader(self, passedMsg = ""):
    clear()
    print("\n======  Cristian's Finance Keeper v0.015 ======\n")
    print("\t My Personal Budgeting Program")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\t Current Time: " + current_time)
      
    self.printMessage(passedMsg)
  
  def printMessage(self, passedMsg = ""):
    if passedMsg != "":
      print(passedMsg)
    print("\t---------------------------------\n")  
  def add_Item(self, args):
    """
    Adds an item based on parameters inputted by the user.
    
    -del -e: Begins the functions to create an expense based on a chosen category.
    -del -c: Creates a chosen category.  
    
    """
    self.class_printBudget()
    passedMsg = ""
    
    if len(args) < 2:
      passedMsg = "\n\tError!  Use the following parameters for the 'add' function:\n\t-e: Add an expense.\n\t-c: Create a category.\n"
    elif args[1] == '-c' and len(args) ==2:  #Probs can replacing the second cond. w/ len(args) <4
      
      newCategory = versionless_input("Enter the category you'd like to create: ").strip()
      if newCategory != "":
        stdin = versionless_input("Are you sure you'd like to create '"+newCategory+"' onto this database? (y/n): ")
        if stdin == "y" or stdin == "yes":
          self.budget[newCategory] = []
          writeBudget(self.budget)
          
          passedMsg = "\n\t'"+newCategory+"' has been added!\n"
      
    elif args[1] == '-e' and len(args) ==2:
      chosenCategory = ""
      stdin = versionless_input("Enter the category of this new expense: ")
      
      if stdin != "":
        for Category in self.budget:
          if Category.lower() == stdin.lower():
            chosenCategory = Category
            break
                  
        if chosenCategory != "":
          addedExpense = []
          addedExpense.append(versionless_input("Enter the name of the expense to be created in "+chosenCategory+": "))
        
        try:
          addedExpense.append(versionless_input("Enter the planned budget for "+addedExpense[0]+": $")) 
          addedExpense.append(versionless_input("Enter the actual spending for "+addedExpense[0]+" (blank if $0): $")) 

          self.budget[chosenCategory].append({addedExpense[0]: [float(addedExpense[1]),float(addedExpense[2])] })
          passedMsg = "\n\t'"+addedExpense[0]+"' has been successfully added to "+chosenCategory+"!\n"
          writeBudget(self.budget)
          
        except:
          passedMsg = "\n\tSomething happened!  Error messages will be more exact in the future! ;3\n"
    elif len(args) > 2:
      passedMsg =  "\n\tError!  Too many arguments!\n"
    else:
      passedMsg = "\n\tError!  Use the following parameters for the 'add' function:\n\t-e: Add an expense.\n\t-c: Create a category.\n"
    self.class_printBudget(passedMsg) 
    
    
  def delete_Item(self, args):
    """
    Deletes an item based on parameters inputted by the user.
    
    -del -e: Begins the functions to delete an expense based on a chosen category.
    -del -c: Deletes a chosen category.  NOTE: Removes all expenses under selected category.
    
    """

    self.class_printBudget()
    passedMsg = ""
      
    if len(args) < 2:
      passedMsg = "\n\tError!  Use the following parameters for the 'del' function:\n\t-e: Delete an expense.\n\t-c: Delete a category.\n"
    elif args[1] == '-c' and len(args) ==2:
      
      stdin = versionless_input("Enter the category you'd like to delete: ").strip()
      if stdin != "":
        for Category in self.budget:
          if stdin.lower() == Category.lower():
            stdin = versionless_input("Are you SURE you wish to delete "+Category+" from this database? (y/n): ")
            if stdin == "y" or stdin == "yes":
              del self.budget[Category]
              writeBudget(self.budget)
              passedMsg = "\n\tItem successfully removed!\n"
              break
          
          else:
            passedMsg = "\n\t'"+ stdin +"' was not found.\n"
      
    elif args[1] == '-e' and len(args) ==2:
      
      stdin = versionless_input("Enter which expense you'd like to delete: ").strip()
      
      if stdin != "":
        for Category in self.budget:
          list_of_expenses = self.budget[Category]
          i=0
                  
          while i < len(list_of_expenses):    #iterates down the list of expenses
            tmp_expense = list_of_expenses[i]
                        
            for item in tmp_expense:
              if item.lower() == stdin.lower():
                stdin = versionless_input("Are you sure you want to delete "+item+" from "+Category+"? (y/n): ").strip()
                if stdin == "y" or stdin == "yes":
                  index = {item: tmp_expense[item]}
                  self.budget[Category].remove(index)
                  writeBudget(self.budget)
                  
                  passedMsg = "\n\tItem successfully removed!\n"
            i+=1
    elif len(args) > 2:
      passedMsg =  "\n\tError!  Too many arguments!\n"
    else:
      passedMsg = "\n\tError!  Use the following parameters for the 'del' function:\n\t-e: Delete an expense.\n\t-c: Delete a category.\n"
    self.class_printBudget(passedMsg)  
