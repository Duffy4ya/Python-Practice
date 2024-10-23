#from Functions import get_todos, write_todos
#To pull from a different directory, use "from (Different dir) import (Folder)"/
#to download a new package. Click on python environment(bottow right),click on overview, and select Packages(PyPI)
import Functions
import time

now = time.strftime("%m/%d/%Y %H:%M:%S")
print(now)

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    #Match is useful when user may enter different predefined values.
    
    if user_action.startswith("add"):
        #4: is a list slicing operation. This cuts the 4th character.
        todo = user_action[4:]
            
        todos = Functions.get_todos()
        #Append adds a single item to the end of the existing list
        todos.append(todo + '\n')
            
        Functions.write_todos(todos)

    #elif will apply if "if" statement is true.
    elif user_action.startswith("show"):
            
        todos = Functions.get_todos()

        #Enumerate createss an object with the structure. Object makes it possible to iterate using two variables.
        for index, item in enumerate(todos):
            item = item.strip('\n')
            #f-strings replace the variable part with a value of the variable. Also possilbe to have expressions inside {}
            row = f"{index + 1}-{item}"
            item = item.title()
            print(row)
    elif user_action.startswith("edit"):
        #Try/Except is used when catching an error.
        try:            
            #Converting can be done with int, float, and str.
            number = int(user_action[5:])
            print(number)
        
            number = number - 1

            todos = Functions.get_todos()

            new_todo = input("Enter new todo: ")
            # \n will create a new line.
            todos[number] = new_todo + '\n'

            Functions.write_todos(todos)
        #ValueError will prompt the print message for any string keyed after "edit".
        except ValueError:
            print("Command not valid.")
            #Continue will restart the loop to the beginning while True statement.
            continue

    elif user_action.startswith("complete"):
        try:        
            number = int(user_action[9:])

            todos = Functions.get_todos()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            Functions.write_todos(todos)

            message = f"Todo {todo_to_remove} was removed from the list."
            print(message)
        #IndexError will prompt the print message for any integer thats not listed when keyed after "complete".
        except IndexError:
            print("No item with that number.")
            continue

    elif user_action.startswith("exit"):
        break
    #else will apply if "if" statement is false
    else:
        print("Unknown command!")

print("Bye!")
