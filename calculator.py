import customtkinter

# Setting the theme and color
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')  # Changed theme color

# Configuring the window
basak = customtkinter.CTk()
basak.title("Calculator")
basak.geometry('400x600+423+159')

def calcular():
    try:
        calculo = output.get('0.0', 'end').strip()
        resultado = eval(calculo)
        output.delete('0.0', 'end')
        output.insert('0.0', resultado)
    except Exception as e:
        output.delete('0.0', 'end')
        output.insert('0.0', "Error")

def clear():
    output.delete('0.0', 'end')

def backspace():
    current_text = output.get('0.0', 'end').strip()
    output.delete('0.0', 'end')
    output.insert('0.0', current_text[:-1])

# Display field
output = customtkinter.CTkTextbox(basak, width=380, height=80, corner_radius=15, border_width=3, border_color='#2C3E50', font=('Arial', 28), fg_color='#1C2833', text_color='#ECF0F1')
output.grid(row=0, column=0, columnspan=4, padx=15, pady=20)

# Button parameters
button_params = {
    "corner_radius": 15, 
    "width": 80, 
    "height": 70, 
    "font": ('Arial', 22, 'bold'),
    "fg_color": "#34495E",
    "hover_color": "#5D6D7E"
}

# Creating buttons
buttons = [
    ('1', 1, 0), ('2', 1, 1), ('3', 1, 2), 
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), 
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), 
    ('0', 4, 1), ('.', 4, 0), ('=', 4, 2), 
    ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), 
    ('/', 4, 3), ('C', 5, 0), ('<-', 5, 1),
    ('(', 5, 2), (')', 5, 3)
]

for (text, row, col) in buttons:
    if text == 'C':
        command = clear
    elif text == '<-':
        command = backspace
    elif text == '=':
        command = calcular
    else:
        command = lambda t=text: output.insert('end', t)
    
    btn = customtkinter.CTkButton(basak, text=text, command=command, **button_params)
    btn.grid(row=row, column=col, padx=10, pady=10)
basak.mainloop()
