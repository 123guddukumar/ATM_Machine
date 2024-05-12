import tkinter as tk
from tkinter import messagebox
import time

balance = 0
def open_atm_gui():
    
    transaction_history = []

    # Create the main window
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("390x800")
    root.title("ATM by GUDDU")
    root.configure(bg="green")
    
    def exit_program():
        messagebox.showinfo("Thank You", "Best of Luck!")
        root.destroy()

        
    # Create the labels
    label_1 = tk.Label(root, text="Welcome to the Octa ATM", font='Roboto 18 bold', bg="coral")
    label_3 = tk.Label(root, text="Enter the amount: ", font='Helvetica 15 bold', bg="violet")

    # Create the buttons
    button_1 = tk.Button(root, text="Withdraw Money", bg="yellow", fg="black", font="8")
    button_2 = tk.Button(root, text="Deposit Money", bg="orange", fg="black", font="8")
    button_3 = tk.Button(root, text="Check Balance", bg="pink", fg="black", font="8")
    button_4 = tk.Button(root, text="Exit", bg="red", fg="black", font="8", width="12", command=exit_program)
    history_button = tk.Button(root, text="History", bg="cyan", fg="black", font="8", width="12")

    # Create the text box
    text_box = tk.Text(root, width=40, height=5, bd="4", font='Roboto 12 bold')

    # Create the entry box
    entry_box = tk.Entry(root, width=18, font="12", bd="6")

    # Pack the labels and buttons
    label_1.place(x=60, y=20)
    button_1.place(x=20, y=120)
    button_2.place(x=250, y=120)
    button_3.place(x=20, y=180)
    button_4.place(x=140, y=640)
    history_button.place(x=255, y=180)
    label_3.place(x=20, y=390)
    text_box.place(x=10, y=250)
    entry_box.place(x=200, y=390)

    # Default value in the entry box. User can edit the value.
    entry_box.insert(tk.END, "0")

    # Print statements in the text box
    def print_statement(statement):
        text_box.delete("1.0", tk.END)
        text_box.insert(tk.END, statement)

    # Withdraw money
    def withdraw():
        text_box.delete("1.0", tk.END)
        amount = int(entry_box.get())
        global balance 
        if amount <= balance:
            balance -= amount
            transaction_history.append(f"Withdrawn: {amount}")
            print("You have withdrawn {}.".format(amount))
            print_statement("Successfully...... \nYou have withdrawn {}.".format(amount))
        else:
            print("Insufficient balance.")
            print_statement("Insufficient balance.")

    # Deposit money
    def deposit():
        text_box.delete("1.0", tk.END)
        amount = int(entry_box.get())
        global balance 
        balance += amount
        transaction_history.append(f"Deposited: {amount}")
        print("You have deposited {}.".format(amount))
        print_statement("Successfully...... \nYou have deposited {}.".format(amount))


    # Check balance
    def check_balance():
        text_box.delete("1.0", tk.END)
        print("Your balance is {}.".format(balance))
        print_statement("Your balance is {}.".format(balance))

    # Transaction history
    def show_transaction_history():
        text_box.delete("1.0", tk.END)
        for transaction in transaction_history:
            text_box.insert(tk.END, transaction + "\n")

    # Add the clear_text_box() function to the button click events
    button_1.config(command=withdraw)
    button_2.config(command=deposit)
    button_3.config(command=check_balance)
    history_button.config(command=show_transaction_history)

    # Keyboard layout
    keyboard_layout = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["/-", "0", "$"]
    ]

    # Function to handle button click events
    def button_click(key):
        if key == "":
            entry_box.delete(len(entry_box.get()) - 1)
        else:
            entry_box.insert(tk.END, key)

    # Create the keyboard buttons
    for i in range(4):
        for j in range(3):
            if keyboard_layout[i][j] != "":
                button = tk.Button(root, text=keyboard_layout[i][j], bg="lightgray", fg="black" ,width="5", font="38",
                                command=lambda key=keyboard_layout[i][j]: button_click(key))
            else:
                button = tk.Button(root, text="", state="disabled", bg="lightgray", font="0.1")
            button.place(x=80 + j * 80, y=440 + i * 50)

    # Start the main loop
    root.mainloop()


def open_pin_entry():
    # Create PIN entry window
    root = tk.Tk()
    root.resizable(False, False)
    root.geometry("300x420")
    root.title("Enter PIN")

    def verify_pin():
        pin = pin_entry.get()
        if pin == "2580":
            root.destroy()  # Close PIN entry window
            open_atm_gui()
        else:
            pin_entry.delete(0, tk.END)  # Clear the PIN entry field
            status_label.config(text="Invalid PIN", fg="red")

    def toggle_show_pin():
        if show_pin_var.get():
            pin_entry.config(show="")
        else:
            pin_entry.config(show="*")

    label = tk.Label(root, text="Enter your PIN:", font=("Roboto", 12))
    label.pack(pady=10)

    pin_entry = tk.Entry(root, show="*", font=("Roboto", 12))
    pin_entry.pack(pady=5)

    show_pin_var = tk.BooleanVar()
    show_pin_checkbox = tk.Checkbutton(root, text="Show PIN", variable=show_pin_var, command=toggle_show_pin)
    show_pin_checkbox.pack()

    status_label = tk.Label(root, text="", font=("Roboto", 10))
    status_label.pack()
    
    # Keyboard layout
    keyboard_layout = [
        ["1", "2", "3"],
        ["4", "5", "6"],
        ["7", "8", "9"],
        [" ", "0", " "]
    ]

    # Function to handle button click events
    def button_click(key):
        if key == " ":
            pin_entry.delete(len(pin_entry.get()) - 1)
        else:
            pin_entry.insert(tk.END, key)

    # Create the keyboard buttons
    keyboard_frame = tk.Frame(root, bg="lightgray")
    keyboard_frame.pack()

    for i in range(4):
        for j in range(3):
            if keyboard_layout[i][j] != "":
                button = tk.Button(keyboard_frame, text=keyboard_layout[i][j], bg="lightgray", fg="black",
                                   width="5", font="38", command=lambda key=keyboard_layout[i][j]: button_click(key))
                button.grid(row=i, column=j, padx=5, pady=5)
                
    submit_button = tk.Button(root, text="Submit", width="15", command=verify_pin, font=("Roboto", 14), bg="green", fg="white")
    submit_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    open_pin_entry()