""" Load a python file and grab all the variables. Create and save
    a text file of the variables inside a def with print statements
    that will show their current values when run .
    For copy pasting back into the program and call the function from
    anywhwere and as many timesas you want for observation and debugging.

Var catcher V1 By Steve Shambles April 2023
(with the assistance of chatgpt3 lol)

Requirements: None
"""

import ast
import os
import tkinter as tk
from tkinter import filedialog, messagebox
import webbrowser as web


def extract_variables():
    """
    Extracts all variables defined in a Python source code file and
    writes them to a text file.
    """
    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename(filetypes=[('Py Files', '*.py')])

    with open(file_path, 'r') as f:
        source_code = f.read()

    parsed_code = ast.parse(source_code)

    variables = []
    for node in ast.walk(parsed_code):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name):
                    variables.append(target.id)

    file_name = os.path.splitext(os.path.basename(file_path))[0]

    with open('variables.txt', 'w') as f:
        f.write('def show_vars():\n')
        f.write('    # File: ' + str(file_name) + '.py\n')
        for variable in variables:
            f.write(f"    print('{variable}:', {variable})\n")
        f.write("    print('-------------------------------------------')")

    msg = str(file_name) + '.py Variables written to variables.txt\n'
    messagebox.showinfo('Information', msg)


extract_variables()
web.open('variables.txt')
