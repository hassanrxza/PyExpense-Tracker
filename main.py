from tkinter import messagebox as mb
import customtkinter as ctk
import pandas as pd
from datetime import datetime

EXCEL_FILE = 'ANYFILE.xlsx'
df = pd.read_excel(EXCEL_FILE)


def submit_values():
    global df
    name = name_field.get()
    qty = int(qty_field.get())
    price = int(price_field.get())
    date_now = datetime.now().strftime("%b %d")
    df.loc[f'{date_now}', :] = [date_now, name, qty, price, (qty * price)]
    df.to_excel(EXCEL_FILE, index=False,)
    mb.showinfo(title="Congratulations", message="Data submitted successfully")


# System Settings

ctk.set_appearance_mode('System')
ctk.set_default_color_theme("blue")

# App Frame

app = ctk.CTk()
app.geometry("720x480")
app.title("Daily Expense Tracker")

# Creating Labels

title_label = ctk.CTkLabel(app, text="Please fill the fields")
title_label.pack( pady=20)

name_label = ctk.CTkLabel(app, text="Name")
name_label.pack()

name_var = ctk.StringVar()
name_field = ctk.CTkEntry(app, width=200, placeholder_text="Enter Item Name")
name_field.pack()

qty_label = ctk.CTkLabel(app, text="Quantity")
qty_label.pack()

qty_var = ctk.StringVar()
qty_field = ctk.CTkEntry(app, width=200, placeholder_text="Enter Item Quantity")
qty_field.pack()

price_label = ctk.CTkLabel(app, text="Price")
price_label.pack()

price_var = ctk.StringVar()
price_field = ctk.CTkEntry(app, width=200, placeholder_text="Enter Product Price")
price_field.pack()

# Insert Button

button = ctk.CTkButton(app, text="Submit", width=80, command=submit_values)
button.pack(pady=10)

# Make sure app not closes

app.mainloop()
