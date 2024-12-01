# CODSOFT

This is an Internship project work in which they have provided with a list of programs in which we are assigined to complete any 3 tasks which are intresting and GUI-based programs. I choose To-Do List applictaion, Password Generator and Rock-Paper-Scissors Game.


Program-1.### **To-Do List Program : Brief Description**

- **Programming Language Used** :  
  The program is written in **Python**, a versatile and beginner-friendly programming language.

- **Packages Used** :  
  The primary package used is **Tkinter**, a built-in Python library for creating graphical user interfaces (GUIs). Other optional packages that may be used include **json** (for saving and loading tasks) and **os** (for file handling, if needed).

- **Functionality of the Program** :  
  1. **Task Addition** :  
     Users can add tasks by entering text into an input field and clicking an "Add Task" button.
  
  2. **Task Removal** :  
     Users can remove tasks, either by selecting them from a list or by specifying criteria.
  
  3. **Task Saving and Loading** :  
     Tasks can be saved to a file (e.g., JSON) and reloaded when the program starts, allowing persistence across sessions.
  
  4. **Checkbox for Completion** :  
     Each task can include a checkbox, enabling users to mark tasks as complete.

  5. **Graphical User Interface**:  
     A clean and intuitive interface is provided for users to interact with the application.

- **Key Features Implemented** :  
  - A text entry field for adding tasks.  
  - Buttons for operations such as adding, removing, and saving tasks.  
  - A scrollable list to display tasks.  
  - Placeholder text in the input field for better user guidance.  
  - Optional visual indicators like checkboxes for task completion.

This project is a simple yet practical application demonstrating GUI design and event handling in Python. It's suitable for beginners and can be expanded with additional features like task prioritization or deadlines.

<img width="535" alt="To_Do_List" src="https://github.com/user-attachments/assets/a28e71d0-dcdd-4773-9f47-c0488016427d">



Program-2.### **Password Generator Program : Brief Description**

- **Programming Language Used** :  
  The program is written in **Python**, known for its simplicity and ease of implementation.

- **Packages Used**:  
  - **Tkinter**: For creating the graphical user interface (GUI).  
  - **random**: To generate random characters for the password.  
  - **string**: To provide character sets like letters, digits, and special symbols.

- **Functionality of the Program** :  
  1. **Password Length Input**:  
     Users can specify the desired length of the password through an input field.
  
  2. **Password Generation** :  
     The program generates a secure password by randomly combining uppercase and lowercase letters, digits, and special characters.
  
  3. **Display of Generated Password** :  
     The generated password is displayed on the screen for easy copying and use.

- **Key Features Implemented** :  
  - A text entry field for users to input the desired password length.  
  - A button to generate the password based on the specified length.  
  - Display area to show the generated password.  
  - Validation to ensure the user provides a valid length.  
  - Optionally, the program may include rules to customize the character mix, like excluding certain characters or ensuring a specific type of character is always included.

- **Graphical User Interface** :  
  A user-friendly GUI allows intuitive interaction, with labels, input fields, and buttons to simplify the process of generating passwords.

This project is a practical application that emphasizes randomization techniques and GUI design in Python. It's useful for learning about string manipulation, secure randomization, and event handling in GUI applications.

<img width="340" alt="Password_generator" src="https://github.com/user-attachments/assets/26fc9697-e4de-4333-b5e2-592ac6867dd5">



Program-3.### **Rock-Paper-Scissors Game: Brief Description**

- **Programming Language Used** :  
  The program is written in **Python**, chosen for its simplicity and readability.

- **Packages Used**:  
  - **Tkinter** : For creating a graphical user interface (GUI) to make the game interactive and user-friendly.  
  - **random** : To enable the computer to make a random choice among "Rock," "Paper," or "Scissors."

- **Functionality of the Program** :  
  1. **User Input** :  
     Users select their choice (Rock, Paper, or Scissors) by clicking corresponding buttons in the GUI.

  2. **Computer Choice** :  
     The computer randomly selects its move from the options using the `random` package.

  3. **Game Logic** :  
     - Rock beats Scissors.  
     - Scissors beat Paper.  
     - Paper beats Rock.  
     The winner is determined based on these rules, with a tie declared if both choices are the same.

  4. **Result Display**:  
     The game displays both the user's and the computer's choices, along with the result (win, lose, or tie).

  5. **Score Tracking** :  
     The program keeps track of scores for both the user and the computer across multiple rounds.

  6. **Play Again Option** :  
     Users can continue playing multiple rounds, with an option to reset the game at any time.

- **Key Features Implemented** :  
  - Buttons for the user to select their move.  
  - A label to display the computer's choice and the game result.  
  - Score tracking and display to keep the game engaging.  
  - A "Reset" button to restart the game and reset scores.

- **Graphical User Interface** :  
  The program features a clean and interactive GUI, with intuitive buttons and clear feedback for user actions and game results.

This project is an excellent demonstration of basic game logic, randomization, and GUI programming in Python. It’s fun, interactive, and a great way to learn about event handling and dynamic updates in GUIs.

<img width="410" alt="Rock_Paper_Scissor_game1" src="https://github.com/user-attachments/assets/34056671-5659-4c4f-926b-b6c527cff339">


<img width="404" alt="Rock_Paper_Scissor_game2" src="https://github.com/user-attachments/assets/548abba4-e7af-4d03-b4fd-062147e8307c">




Program-4.### **Contact Book Program: Description**

#### **Programming Language Used**  
The program is implemented in **Python**, leveraging its simplicity and wide range of libraries.

#### **Packages Used**  
- **Tkinter**: For creating a graphical user interface (GUI) that provides a user-friendly interaction.  
- **json**: For storing and retrieving contact information in a persistent and structured format.  

#### **Functionality of the Program**  
1. **Store Contact Information** :  
   - Each contact stores details such as name, phone number, email, and address.

2. **Add New Contact** :  
   - Users can input details through an interface and add them to the contact list.

3. **View Contact List** :  
   - Displays all saved contacts in a scrollable list, showing names and phone numbers for quick reference.

4. **Search Contact** :  
   - Allows users to search for contacts by name or phone number. Displays matching results in the interface.

5. **Update Contact** :  
   - Users can edit and update the details of existing contacts through the interface.

6. **Delete Contact** :  
   - Provides an option to remove a specific contact from the list.

#### **Key Features Implemented**  
- **Persistent Storage** :  
  Contact details are stored in a JSON file, allowing the data to persist even after the program is closed.
  
- **Dynamic GUI** :  
  - Input fields and buttons for adding, searching, updating, and deleting contacts.  
  - A listbox or table view to display contacts dynamically.

- **Validation** :  
  - Ensures fields like phone numbers and email addresses are entered in the correct format.  
  - Prevents duplicate entries for the same contact.

#### **Graphical User Interface**  
The GUI includes :  
- Entry fields for inputting contact details.  
- Buttons for performing actions such as adding, searching, updating, and deleting contacts.  
- A list view to display all or searched contacts.  
- Labels and messages to guide users and provide feedback.

#### **Program Highlights**  
- **Beginner-Friendly** : Focuses on essential Python concepts such as file handling, string manipulation, and event-driven programming.  
- **Scalable** : Additional features like importing/exporting contacts, advanced search options, or integrating with an online database can be added.  

This project is ideal for learning about data management, GUI design, and event handling in Python. Would you like a code implementation for this?
