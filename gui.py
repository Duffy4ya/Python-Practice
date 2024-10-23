
import Functions
import FreeSimpleGUI as sg
import time

sg.theme("DarkBrown4")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a to-do and click Add to add to list.\nSelect to-do to replace, type in replacement, and click Edit\nSelect a to-do to complete and click Complete.")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=Functions.get_todos(), key='todos',
                      enable_events=True, size=[45, 10])

edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

window = sg.Window('My To-Do App',
                  layout=[[clock],
                          [label], 
                          [input_box, add_button], 
                          [list_box, edit_button, complete_button],
                          [exit_button]],
                  font =('Helvetica', 10))
while True:
    #timeout will refresh the window per milliseconds. Good for displaying current time.
    event, values = window.read(timeout=200)
    window["clock"].update(value=time.strftime("%m/%d/%Y %H:%M:%S"))
    match event:
        case "Add":
            todos = Functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            Functions.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            try:        
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = Functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                Functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first.", 
                         font=('Helvetica', 10)) 
        case "Complete":
            try:        
                todo_to_complete = values['todos'][0]
                todos = Functions.get_todos()
                todos.remove(todo_to_complete)
                Functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value='')
            except IndexError:
                sg.popup("Please select an item first.", 
                         font=('Helvetica', 10))
        case "Exit":
            break
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        #sg.WIN_CLOSED will allow you to close the GUI without getting an error.
        case sg.WIN_CLOSED:
            break

window.close()