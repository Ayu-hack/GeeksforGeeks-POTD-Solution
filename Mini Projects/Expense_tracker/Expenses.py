import os
import json
from datetime import datetime
import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Get the directory of the current script and ensure the expenses.json file is created there
current_directory = os.path.dirname(os.path.abspath(__file__))
EXPENSE_FILE = os.path.join(current_directory, 'expenses.json')

def load_expenses():
    """Load expenses from a JSON file, create the file if it doesn't exist or handle invalid data."""
    try:
        with open(EXPENSE_FILE, 'r') as file:
            expenses = json.load(file)
            if not isinstance(expenses, list):  # Check if the loaded data is a valid list
                raise ValueError("Data in file is not in the expected format.")
            return expenses
    except (FileNotFoundError, json.JSONDecodeError, ValueError) as e:
        # If the file doesn't exist or contains invalid data, create an empty file
        with open(EXPENSE_FILE, 'w') as file:
            json.dump([], file, indent=4)  # Initialize an empty list in the file
        return []  # Return an empty list when file is empty or invalid

def save_expenses(expenses):
    """Save expenses to a JSON file."""
    with open(EXPENSE_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def is_valid_date(date_string):
    """Check if the date string is valid."""
    try:
        datetime.strptime(date_string, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def add_expense(expenses):
    """Add a new expense from GUI input."""
    try:
        amount = float(amount_entry.get())
        if amount < 0:
            raise ValueError("Amount must be a positive number.")

        category = category_var.get()
        date = date_entry.get() if date_entry.get() else datetime.now().strftime("%Y-%m-%d")

        if not category:
            raise ValueError("Category cannot be empty.")

        if date and not is_valid_date(date):
            raise ValueError("Date must be in YYYY-MM-DD format.")

        expense = {
            "amount": amount,
            "category": category,
            "date": date
        }
        expenses.append(expense)
        save_expenses(expenses)
        clear_entries()
        update_treeview(expenses)
        update_pie_chart()
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def update_treeview(expenses):
    """Update the treeview to show current expenses with a delete option."""
    for i in tree.get_children():
        tree.delete(i)  # Clear the treeview

    for idx, expense in enumerate(expenses):
        tree.insert("", tk.END, values=(expense['date'], expense['category'], f"₹{expense['amount']:.2f}", "Delete"),
                    tags=('row',), iid=idx)

def delete_expense(index, expenses):
    """Delete the selected expense."""
    if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this expense?"):
        expenses.pop(index)
        save_expenses(expenses)
        update_treeview(expenses)
        update_pie_chart()
        messagebox.showinfo("Success", "Expense deleted successfully!")

def clear_entries():
    """Clear input fields."""
    amount_entry.delete(0, tk.END)
    category_var.set('')  # Reset the category selection
    date_entry.delete(0, tk.END)

def on_treeview_click(event):
    """Handle click events in the treeview."""
    item = tree.identify_row(event.y)  # Get the row clicked
    if item:  # If a row was clicked
        column = tree.identify_column(event.x)  # Get the column clicked
        if column == "#4":  # If the delete column was clicked
            index = int(item)
            delete_expense(index, expenses)

def update_pie_chart():
    """Update the pie chart whenever the expenses change."""
    # Aggregate expenses by category
    categories = {}
    for expense in expenses:
        categories[expense['category']] = categories.get(expense['category'], 0) + expense['amount']

    # Clear previous pie chart
    for widget in pie_frame.winfo_children():
        widget.destroy()

    # Create a new figure for the pie chart
    fig, ax = plt.subplots()

    if categories:  # Check if there are any categories
        ax.pie(categories.values(), labels=categories.keys(), autopct='%1.1f%%', colors=['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ffb3e6', '#c2c2f0'])
        ax.set_title("Expenses by Category (Pie Chart)", color="white")
        ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    fig.patch.set_facecolor("#2d2d3f")
    ax.set_facecolor("#2d2d3f")
    ax.tick_params(colors="white")

    # Embed the updated pie chart in the pie_frame
    canvas = FigureCanvasTkAgg(fig, master=pie_frame)  # A tk.DrawingArea.
    canvas.draw()
    canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

# Load existing expenses
expenses = load_expenses()

# Create GUI
root = tk.Tk()
root.title("Personal Expense Tracker")
root.state('zoomed')  # Fullscreen mode
root.config(bg="#282A36")  # Background color

# Create a PanedWindow to split the screen into left (table) and right (pie chart)
paned_window = tk.PanedWindow(root, orient=tk.HORIZONTAL, sashrelief=tk.RAISED)
paned_window.pack(fill=tk.BOTH, expand=True)

# Left frame for table (55% width)
left_frame = tk.Frame(paned_window, bg="#282A36")
paned_window.add(left_frame, width=1000)  # Adjust the initial width of the table frame

# Right frame for pie chart (45% width)
pie_frame = tk.Frame(paned_window, bg="#282A36")
paned_window.add(pie_frame, width=600)  # Adjust the initial width of the pie chart frame

# Entry fields for expenses (in the left frame)
tk.Label(left_frame, text="Amount (₹):", bg="#282A36", fg="#F8F8F2", font=('Courier New', 14, 'bold')).pack(pady=5)
amount_entry = tk.Entry(left_frame, bg="#44475a", fg="#F8F8F2", insertbackground="white", font=('Courier New', 12))
amount_entry.pack(pady=5)

tk.Label(left_frame, text="Category:", bg="#282A36", fg="#F8F8F2", font=('Courier New', 14, 'bold')).pack(pady=5)
category_var = tk.StringVar()

# Style for the combobox
style = ttk.Style()

# Setting the font and background for the combobox
style.configure('TCombobox',
                font=('Courier New', 12),
                background="#44475a",
                foreground="#F8F8F2",
                fieldbackground="#44475a",
                arrowsize=20)

category_entry = ttk.Combobox(left_frame, textvariable=category_var, 
                              values=["Grocery", "Stationary", "Electronics", "Household", "Clothing", 
                                      "Transport", "Entertainment", "Fast Food", "Other"], style="TCombobox")
category_entry.pack(pady=5)

tk.Label(left_frame, text="Date (YYYY-MM-DD, optional):", bg="#282A36", fg="#F8F8F2", font=('Courier New', 14, 'bold')).pack(pady=5)
date_entry = tk.Entry(left_frame, bg="#44475a", fg="#F8F8F2", insertbackground="white", font=('Courier New', 12))
date_entry.pack(pady=5)

# Add Expense Button
add_button = tk.Button(left_frame, text="Add Expense", bg="#50fa7b", fg="#1a1a1a", font=('Courier New', 12, 'bold'),
                       command=lambda: add_expense(expenses))
add_button.pack(pady=10)

# Treeview to display expenses with delete option (in the left frame)
style.configure('Treeview', font=('Courier New', 12), rowheight=30, background="#44475a", foreground="#F8F8F2", fieldbackground="#44475a")
tree = ttk.Treeview(left_frame, columns=("Date", "Category", "Amount", "Delete"), show="headings", style="Treeview")
tree.heading("Date", text="Date")
tree.heading("Category", text="Category")
tree.heading("Amount", text="Amount")
tree.heading("Delete", text="Delete")

tree.column("Date", width=150, anchor=tk.CENTER)
tree.column("Category", width=150, anchor=tk.CENTER)
tree.column("Amount", width=100, anchor=tk.CENTER)
tree.column("Delete", width=100, anchor=tk.CENTER)

tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
tree.bind("<ButtonRelease-1>", on_treeview_click)

# Update treeview and pie chart on startup
update_treeview(expenses)
update_pie_chart()

root.mainloop()
