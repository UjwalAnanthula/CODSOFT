#To-Do List
import tkinter as tk
from tkinter import messagebox
import json

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x500")

placeholder_text = "Enter a new task"

# Entry widget with placeholder
task_entry = tk.Entry(root, width=35, fg="grey")
task_entry.insert(0, placeholder_text)  # Insert placeholder text initially
task_entry.pack(pady=10)

# Functions to manage placeholder behavior
def on_entry_click(event):
    if task_entry.get() == placeholder_text:
        task_entry.delete(0, tk.END)  # Clear the placeholder text
        task_entry.config(fg="black")

def on_focus_out(event):
    if task_entry.get() == "":
        task_entry.insert(0, placeholder_text)  # Restore placeholder
        task_entry.config(fg="grey")

# Bind focus in/out events
task_entry.bind("<FocusIn>", on_entry_click)
task_entry.bind("<FocusOut>", on_focus_out)

#Add Task button
add_btn = tk.Button(root, text="Add Task", command=lambda: add_task())
add_btn.pack(pady=5)

#Remove or delete task button
remove_btn = tk.Button(root, text="Remove Task", command=lambda: remove_task())
remove_btn.pack(pady=5)

#To display tasks
listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
listbox.pack(pady=10)
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

#Dummy Save Task button
save_btn = tk.Button(root, text="Save Task")#By adding 'command=lambda: save_tasks', it can be made functional
save_btn.pack(pady=5)

#Functions to add and delete
def add_task():
    task = task_entry.get()
    if task:
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error!", "Please enter a task to add.")

def remove_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Selection Error!", "Please select a task to remove.")

#Function to save tasks
def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
            for task in tasks:
                listbox.insert(tk.END, task)
    except FileNotFoundError:
        pass

load_tasks()
root.mainloop()