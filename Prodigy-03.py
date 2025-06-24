
import tkinter as tk

def check_password_strength():
    password = entry.get()
    strength = 0
    remarks = ""
    
    # Define special characters manually
    special_characters = "!@#$%^&*()_+-=[]{}|;:',.<>?/"

    # Check conditions
    if len(password) >= 8:
        strength += 1

    if any(char.islower() for char in password):
        strength += 1

    if any(char.isupper() for char in password):
        strength += 1

    if any(char.isdigit() for char in password):
        strength += 1

    if any(char in special_characters for char in password):
        strength += 1

    # Feedback based on strength
    if strength == 0:
        remarks = "Enter a password."
        color = "black"
    elif strength <= 2:
        remarks = "Weak password"
        color = "red"
    elif strength == 3:
        remarks = "Moderate password"
        color = "orange"
    elif strength == 4:
        remarks = "Strong password"
        color = "green"
    else:
        remarks = "Very strong password"
        color = "darkgreen"

    result_label.config(text=remarks, fg=color)

# GUI setup
root = tk.Tk()
root.title("Password Strength Checker")
root.geometry("400x200")
root.resizable(False, False)

tk.Label(root, text="Enter your password:", font=("Arial", 12)).pack(pady=10)
entry = tk.Entry(root, width=30, font=("Arial", 12))
entry.pack()

check_button = tk.Button(root, text="Check Strength", command=check_password_strength, font=("Arial", 10))
check_button.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack()

root.mainloop()
