import tkinter as tk

def show_winner(result):
    root = tk.Tk()
    
    if result == 0:
        label = tk.Label(root, text="Black won", font=("Arial", 18))
    elif result == 1:
        label = tk.Label(root, text="White won", font=("Arial", 18))
    else:
        label = tk.Label(root, text="Invalid input", font=("Arial", 18))
    
    label.pack(padx=20, pady=20)
    root.mainloop()

# Example usage:
# Replace the argument with 0 or 1 to see the respective message
show_winner(0)  # This will display "Black won"
