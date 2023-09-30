import tkinter as tk

def on_button_click(char):
    if char == '=':
        try:
            expression = result_var.get()
            result = eval(expression)
            result_var.set(result)
        except Exception as e:
            result_var.set("Error")
    elif char == 'C':
        result_var.set('')
    elif char == 'back':
        current_text = result_var.get()
        new_text = current_text[:-1]  # Remove the last character
        result_var.set(new_text)
    else:
        current_text = result_var.get()
        new_text = current_text + char
        result_var.set(new_text)

root = tk.Tk()
root.title("Calculator")
root.geometry("400x600")

result_var = tk.StringVar()

display = tk.Entry(root, textvariable=result_var, font=("Arial", 24), bd=10, insertwidth=4, width=16, justify='right')
display.grid(row=0, column=0, columnspan=4, padx=20, pady=20, ipadx=10, ipady=10)
display.configure(bg="white", fg="black")  # Light white background and black text

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+',
    'C', 'back'  # Add the "Clear" and "Back" buttons
]

row, col = 1, 0

for button_text in buttons:
    if button_text == '=' or button_text == 'C':
        width = 6
        pady = 10
        bg_color = "lightgray"  # Light gray background
        fg_color = "black"  # Black text color
    elif button_text == 'back':
        width = 6
        pady = 5
        bg_color = "lightgray"  # Light gray background
        fg_color = "black"  # Black text color
    elif button_text == '/':
        width = 6
        pady = 5
        bg_color = "lightgray"  # Light gray background
        fg_color = "black"  # Black text color
    elif button_text == '*':
        width = 6
        pady = 5
        bg_color = "lightgray"  # Light gray background
        fg_color = "black"  # Black text color
    elif button_text == '-':
        width = 6
        pady = 5
        bg_color = "lightgray"  # Light gray background
        fg_color = "black"  # Black text color
    elif button_text == '+':
        width = 6
        pady = 5
        bg_color = "lightgray"  # Light gray background
        fg_color = "black"  # Black text color
    else:
        width = 6
        pady = 5
        bg_color = "white"  # White background
        fg_color = "black"  # Black text color

    tk.Button(root, text=button_text, font=("Arial", 18), width=width, pady=pady, command=lambda t=button_text: on_button_click(t), bg=bg_color, fg=fg_color).grid(row=row, column=col, padx=10, pady=10)
    col += 1
    if col > 3:
        col = 0
        row += 1

root.mainloop()