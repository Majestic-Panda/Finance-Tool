import json, sys
from os import system, name
from datetime import datetime


budget = {}
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
        _ = system('clear') 
        
def versionless_input(inputMsg):
    
    if fetchPythonVersion("num") < 3:
        stdin = raw_input(inputMsg)
        print("")
    else:
        stdin = input(inputMsg)
        print("")
    return stdin

def openBudget():
    with open('budget.json','r') as json_file:
        budget_raw = json.loads(json_file.read())
    return budget_raw

def writeBudget(budget):
    with open('budget.json','w') as json_file:
        json_file.write(json.dumps(budget))
    
def alterExpense(budget, cmd):
    successMsg = ""
    if cmd == "-ap" or cmd == "-aa":
        
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
                        if cmd == "-ap":
                            stdin = versionless_input("Replace PLANNED value for "+item+": " )
                            print("")
                            try:
                                tmp_expense[item][0] = float(stdin)
                                writeBudget(budget)
                                successMsg = "\n\t"+item+" was changed to "+stdin+"!\n"
                            except:
                                successMsg="\n\tValue is not a number!\n" 
                        elif cmd == "-aa":
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
    list_of_chosenCategory = []
    successMsg = ""
    
    stdin = versionless_input("Enter the category of this new expense: ")
    print("")
    
    for Category in budget:
        if Category.lower() == stdin.lower():
            chosenCategory = Category
            list_of_chosenCategory = budget[Category]
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

def printBudget(data, passedMsg = ""):
    printHeader(passedMsg)
    print("==========\n")
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
                print('{:<10s}{:>15.2f}{:>10.2f}'.format(expense, tmp_expense[item][0], tmp_expense[item][1]))            
            i += 1 
        
    
    print("\n==========")
def printHeader(passedMsg):
    clear()
    print("\n======  Cristian's Finance Keeper v0.012 ======\n")
    print("\t My Personal Budgeting Program")
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("\t Current Time: " + current_time)
    
    if passedMsg != "":
        print(passedMsg)
    
        
        
        
        
	

