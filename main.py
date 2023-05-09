import tkinter as tk
import util
import instagrapi


# Create the main window
root = tk.Tk()

# Set the window size and title
root.geometry("500x500")
root.title("Instagram Tracker")

# Create the Username label and input box
username_label = tk.Label(root, text="Username:")
username_label.pack()
username_entry = tk.Entry(root)
username_entry.pack()

# Create the Password label and input box
password_label = tk.Label(root, text="Password:")
password_label.pack()
password_entry = tk.Entry(root)  # Use show="*" to hide password
password_entry.pack()


def on_enter(e):
    submit_button.config(bg='white')


def on_leave(e):
    submit_button.config(bg='SystemButtonFace')


def on_submit_click(event):
    username = username_entry.get()
    password = password_entry.get()
    print("Username:", username)
    print("Password:", password)

    login = False

    try:
        util.loginWithCredential(username, password)
    except instagrapi.exceptions.UnknownError:
        print("The username you entered doesn't appear to belong to an account. Please check your username and try again.")
    except instagrapi.exceptions.BadPassword:
        print("The password you entered is incorrect. Please try again.")
    else:
        login = True

    if (login):
        # Erase the contents of the frame
        for widget in root.winfo_children():
            widget.destroy()
        # Display the "successful" message
        successful_label = tk.Label(root, text="Login Successful!")
        successful_label.pack()


# Create the Submit button
submit_button = tk.Button(
    root, text="Submit", command=on_submit_click,  bg='SystemButtonFace')
submit_button.bind("<Enter>", on_enter)
submit_button.bind("<Leave>", on_leave)
submit_button.pack()
# Bind the left mouse button click event
submit_button.bind("<Button-1>", on_submit_click)

# Run the main loop to display the window
root.mainloop()

if __name__ == "__main__":
    print("Terminated")
