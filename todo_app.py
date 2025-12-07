"""To-do List
A Tkinter-based task manager application.

Features:
- Two tabs: Tasks to complete & Completed tasks
- Save and load tasks to/from JSON files
- Separate view for completed tasks
"""

import tkinter as tk
import os
import json
import datetime
from tkinter import messagebox


def get_task():
    """
    Retrieve the current entry field value and append it to the task list.

    Returns:
        list: Updated list of tasks.
    """
    entry = EntryValue.get()
    if entry:
        entry_list.append(entry)
    return entry_list


def add_task(list_to_add=None, frame=None):
    """
    Display tasks in the appropriate frame.

    Args:
        list_to_add (list, optional): List of tasks to display.
        frame (tk.Frame, optional): Frame where tasks should appear.

        If both arguments are None:
            Tasks will be added to the main "Tasks to Complete" tab.
    """
    if list_to_add and frame is not None:
        entries = dict.fromkeys(list_to_add)
        frames = frame

        for val, entry in enumerate(entries):
            tk.Label(frames, text=f'{val + 1}. {entry}').grid(row=val + 1, column=0, sticky='w')

    else:
        entries = get_task()
        frames = inside_tasks

        for value_index, entry in enumerate(entries):
            tk.Checkbutton(
                frames,
                text=entry,
                variable=task_Value,
                offvalue=0,
                onvalue=value_index
            ).grid(row=value_index + 1, column=0, sticky='w')


def delete_task():
    """
    Delete the selected task and refresh the task display.
    """
    global inside_tasks

    delete_value = task_Value.get()
    if entry_list:
        entry_list.pop(delete_value)

    inside_tasks.destroy()
    top_entry_box.delete(0, tk.END)

    inside_tasks = tk.Frame(tasks_list_frame)
    inside_tasks.grid(row=0, column=0, sticky='news')

    if entry_list:
        add_task()

    task_Value.set(0)


def complete_task():
    """
    Mark the selected task as completed and move it to the 'Completed Tasks' section.
    """
    index_value = task_Value.get()
    if entry_list:
        completed_list.append(entry_list[index_value])
        add_task(completed_list, inside_completed)


def clear_tasks():
    """
    Remove all tasks from both tabs and reset the interface.
    """
    global inside_tasks
    global inside_completed

    entry_list.clear()
    completed_list.clear()

    inside_tasks.destroy()
    inside_completed.destroy()

    inside_tasks = tk.Frame(tasks_list_frame)
    inside_tasks.grid(row=0, column=0, sticky='news')

    inside_completed = tk.Frame(completed_tasks)
    inside_completed.grid(row=0, column=0, sticky='news')


def save_tasks():
    """
    Save all tasks and completed tasks into a timestamped JSON file.
    Creates a new folder if it doesn't already exist.
    """
    filename = 'To_Do_Saves'
    numbering = 1
    dateandtime = datetime.date.today()

    if filename not in os.listdir():
        os.mkdir(filename)

    while True:
        temp_name = os.path.join(filename, f'Date-{dateandtime.strftime("%d")}-Save-{numbering}.json')
        if os.path.exists(temp_name):
            numbering += 1
        else:
            filename = temp_name
            break

    if entry_list:
        with open(filename, 'w', encoding='utf-8') as output_file:
            new_dict = {
                "Tasks": entry_list,
                "Completed Tasks": list(dict.fromkeys(completed_list))
            }
            json.dump(new_dict, output_file, indent=2)
    else:
        messagebox.showinfo("TaskInfo", "No Task Entries")


def get_files():
    """
    List all saved task files from the save directory.

    Returns:
        list: Filenames of saved task files.
    """
    directories = os.listdir("To_Do_Saves")
    return list(dict.fromkeys(directories))


def load_tasks():
    """
    Load tasks from the selected JSON save file and update both tabs.
    """
    value_selection = entry_box.selection_get()
    select_val.set(value_selection)

    file = select_val.get()

    files = get_files()
    filename = ""

    for basename in files:
        if basename == file:
            filename = os.path.join("To_Do_Saves", file)

    clear_tasks()

    with open(filename, 'r', encoding='utf-8') as f:
        save_dict = json.load(f)
        tasks_list = save_dict.get("Tasks")
        completed_tasks_list = save_dict.get("Completed Tasks")

        entry_list.extend(tasks_list)
        completed_list.extend(completed_tasks_list)

    select_val.set('Load Tasks From File')
    add_task()
    add_task(completed_list, inside_completed)
    cancel_load_tasks()


def load_menu_task():
    """
    Display the list of available saved files for the user to choose from.
    """
    load_tasks_frame.grid(row=5, column=1, sticky='news')

    files = get_files()
    files_in_entry = entry_box.get(0, tk.END)

    for file in files:
        if file not in files_in_entry:
            entry_box.insert("end", file)

    select_val.set('Load Tasks From File')

    inner_load = tk.Frame(load_tasks_frame, relief="sunken")
    inner_load.grid(row=0, column=2, sticky='news')

    inner_load.rowconfigure(0, weight=10)
    inner_load.rowconfigure(1, weight=15)

    load_tasks_file = tk.Button(inner_load, textvariable=select_val, command=load_tasks)
    load_tasks_file.grid(row=0, column=0, sticky='sew')

    cancel_button = tk.Button(inner_load, text="Cancel", command=cancel_load_tasks)
    cancel_button.grid(row=1, column=0, sticky='new')


def cancel_load_tasks():
    """
    Hide the load task selection panel.
    """
    load_tasks_frame.grid_forget()


# ----------------------------
# Main Tkinter Window Setup
# ----------------------------

root = tk.Tk()
root.geometry("650x750")
root.title("TO-DO LIST")
root.configure(background='lightblue')
root.minsize(600, 500)

configure_main = [(0, 10), (1, 30), (2, 15)]
for index, weight in configure_main:
    root.columnconfigure(index, weight=weight)

tk.Label(
    root,
    text="\u2714TO-DO LIST APP",
    font=('helvetica', 18, "bold"),
    borderwidth=2
).grid(row=0, column=0, columnspan=3, sticky='news')


# Entry section
enter_task = tk.Frame(root, relief='sunken', borderwidth=2, background='lightblue')
enter_task.grid(row=1, column=0, columnspan=3, sticky='news')

configure_task = [(0, 10), (1, 30), (2, 15)]
for index, weight in configure_task:
    enter_task.columnconfigure(index, weight=weight)

EntryValue = tk.StringVar()
tk.Label(enter_task, text='Enter Task: ').grid(row=0, column=0, sticky='news')
top_entry_box = tk.Entry(enter_task, textvariable=EntryValue, font=('helvetica', 14))
top_entry_box.grid(row=0, column=1, sticky='news')
tk.Button(enter_task, text='Add Task', command=add_task).grid(row=0, column=2, sticky='news')

task_Value = tk.IntVar()

# Task menus
tasks_menu = tk.Frame(root)
tasks_menu.grid(row=3, column=0, columnspan=3, sticky='news')

tasks_menu.columnconfigure(0, weight=30)
tasks_menu.columnconfigure(1, weight=30)

tasks_list_frame = tk.LabelFrame(tasks_menu, text="Tasks-to-complete", relief='groove', borderwidth=2)
tasks_list_frame.grid(row=0, column=0, sticky='news')

completed_tasks = tk.LabelFrame(tasks_menu, text='Completed Tasks', relief='groove', borderwidth=2)
completed_tasks.grid(row=0, column=1, sticky='news')

inside_tasks = tk.Frame(tasks_list_frame)
inside_tasks.grid(row=0, column=0, sticky='news')

inside_completed = tk.Frame(completed_tasks)
inside_completed.grid(row=0, column=0, sticky='news')

# Buttons panel
do_tasks = tk.Frame(root)
do_tasks.grid(row=4, column=1, sticky='news')

do_configure = [(0, 10), (1, 10), (2, 10), (3, 10), (4, 10)]
for index, weight in do_configure:
    do_tasks.columnconfigure(index, weight=weight)

tk.Button(do_tasks, text='Delete Selected Task', command=delete_task).grid(row=0, column=0, sticky='news')
tk.Button(do_tasks, text='Task Completed', command=complete_task).grid(row=0, column=1, sticky='news')
tk.Button(do_tasks, text='Clear Tasks', command=clear_tasks).grid(row=0, column=2, sticky='news')
tk.Button(do_tasks, text='Save Tasks', command=save_tasks).grid(row=0, column=3, sticky='news')
tk.Button(do_tasks, text='Load Tasks', command=load_menu_task).grid(row=0, column=4, sticky='news')

# Load tasks panel
load_tasks_frame = tk.LabelFrame(root, text='Load Tasks', relief="sunken")
load_tasks_frame.columnconfigure(0, weight=30)

select_val = tk.StringVar()
entry_box = tk.Listbox(load_tasks_frame, relief='sunken', font=('Arial', 12))
entry_box.grid(row=0, column=0, sticky='news')

scroll_y = tk.Scrollbar(load_tasks_frame, relief='sunken', orient='vertical', borderwidth=2, command=entry_box.yview)
scroll_y.grid(row=0, column=1, sticky='ns')
entry_box['yscrollcommand'] = scroll_y.set

load_tasks_frame.grid_forget()

# Storage lists
entry_list = []
add_task()
completed_list = []


root.mainloop()
