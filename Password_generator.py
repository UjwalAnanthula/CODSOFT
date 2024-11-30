import tkinter as tk
import random
import string

# Function to generate password
def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            result_label.config(text="Please enter a positive integer.")
            return
        
        # Define characters for password
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        
        # Display generated password
        result_label.config(text=f"Generated Password: {password}")
    except ValueError:
        result_label.config(text="Please enter a valid number.")

# Setting up the GUI
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")

# Input for password length
length_label = tk.Label(root, text="Enter password length:")
length_label.pack(pady=10)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack(pady=10)

# Label to display the generated password
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()