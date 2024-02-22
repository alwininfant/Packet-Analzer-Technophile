#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
from tkinter import ttk

# Create a function to handle button clicks
def button_click(text):
    print(f"{text} button clicked")

# Function to handle selection from vulnerability dropdown
def vulnerability_selected(event):
    selected_vulnerability.set(vulnerability_options[vulnerability_dropdown.current()])

# Function to handle selection from statistic dropdown
def statistic_selected(event):
    selected_statistic.set(statistic_options[statistic_dropdown.current()])

# Create the main window
root = tk.Tk()
root.title("Packet Capture and Analyzing Tool")

# Create a frame to contain the heading and set its border color
heading_frame = tk.Frame(root, bd=2, relief=tk.SOLID, bg="white", highlightbackground="white")
heading_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky=tk.W+tk.E)

# Add the heading label inside the heading frame
heading_label = tk.Label(heading_frame, text="Packet Capture and Analyzing Tool", font=("Arial", 16))
heading_label.pack(padx=10, pady=10)

# Configure columns to expand horizontally
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=2)  # Set column 1 to have more weight

# Create a frame to contain the buttons
button_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
button_frame.grid(row=1, column=0, columnspan=2, padx=10, pady=(0, 10), sticky=tk.W+tk.E)

# Define the names for the first 5 buttons
button_texts = ["Start Capture", "Save Into File", "Open the File", "Analyse the Packets", "See the Vulnerabilities"]

# Create five buttons with the specified names and add them to the button frame
for i, text in enumerate(button_texts):
    button = tk.Button(button_frame, text=text, command=lambda t=text: button_click(t))
    button.grid(row=0, column=i, padx=5, pady=5, sticky=tk.W)

# Create a frame to contain the output text
output_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
output_frame.grid(row=2, column=0, columnspan=2, padx=10, pady=(0, 10), sticky=tk.NSEW)

# Add Text widget for displaying output
output_text = tk.Text(output_frame, height=15, width=100)  # Increased width
output_text.grid(row=0, column=0, padx=10, pady=5, sticky=tk.NSEW)

# Create a frame for vulnerability area
vulnerability_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
vulnerability_frame.grid(row=3, column=0, padx=10, pady=(0, 10), sticky=tk.W+tk.E)

# Create a label for the vulnerability area
vulnerability_label = tk.Label(vulnerability_frame, text="Vulnerability", font=("Arial", 12))
vulnerability_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.NW)

# Add Text widget for displaying vulnerability output
vulnerability_output = tk.Text(vulnerability_frame, height=5, width=50)
vulnerability_output.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

# Options for vulnerability dropdown
vulnerability_options = [
    "Plaintext Passwords",
    "Intrusions and Breaches",
    "PII Leak",
    "Malware Infections",
    "Protocol Abnormalities",
    "Network Misconfigurations",
    "Data Exfiltration",
    "Denial of Service (DoS)"
]

# Variable to store selected vulnerability
selected_vulnerability = tk.StringVar()

# Create dropdown menu for vulnerabilities
vulnerability_dropdown = ttk.Combobox(vulnerability_frame, values=vulnerability_options, textvariable=selected_vulnerability)
vulnerability_dropdown.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
vulnerability_dropdown.current(0)  # Set default option
selected_vulnerability.set(vulnerability_options[0])  # Set default value
vulnerability_dropdown.bind("<<ComboboxSelected>>", vulnerability_selected)

# Create a frame for statistic area
statistic_frame = tk.Frame(root, bd=2, relief=tk.SOLID)
statistic_frame.grid(row=3, column=1, padx=10, pady=(0, 10), sticky=tk.W+tk.E)

# Create a label for the statistic area
statistic_label = tk.Label(statistic_frame, text="Statistic", font=("Arial", 12))
statistic_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.NW)

# Add Text widget for displaying statistic output
statistic_output = tk.Text(statistic_frame, height=5, width=50)
statistic_output.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

# Options for statistic dropdown
statistic_options = [
    "Option 1",
    "Option 2",
    "Option 3"
]

# Variable to store selected statistic
selected_statistic = tk.StringVar()

# Create dropdown menu for statistics
statistic_dropdown = ttk.Combobox(statistic_frame, values=statistic_options, textvariable=selected_statistic)
statistic_dropdown.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)
statistic_dropdown.current(0)  # Set default option
selected_statistic.set(statistic_options[0])  # Set default value
statistic_dropdown.bind("<<ComboboxSelected>>", statistic_selected)

# Configure row 3 to expand vertically to push both frames down
root.rowconfigure(3, weight=1)

root.mainloop()


# In[ ]:




