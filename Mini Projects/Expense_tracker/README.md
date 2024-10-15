# Personal Expense Tracker

A simple **Personal Expense Tracker** built with Python, featuring expense logging, category-based expense tracking, and visualizations via a pie chart.

## Features

- **Add Expenses**: Log expenses by amount, category, and optional date (defaults to today).
  - Categories include: 
    ```text
    Grocery, Stationary, Electronics, Household, Clothing, 
    Transport, Entertainment, Fast Food, Other
    ```
  
- **View Expenses**: See a table of all logged expenses with options to delete any entry.

- **Visualize Expenses**: A **pie chart** dynamically shows expense distribution across categories.

- **Data Persistence**: All data is stored in `expenses.json` and persists after closing.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```
2. Install `matplotlib`:
    ```bash
    pip install matplotlib
    ```
3. Run the app:
    ```bash
    python tracker.py
    ```

## Usage

1. **Add Expense**: Input amount, select category, and add the expense.
2. **View & Delete Expenses**: Manage expenses through the table.
3. **Pie Chart**: View real-time category breakdown of expenses.

## File Structure

```text
.
├── tracker.py      # Main script
├── expenses.json   # Stores expense data
└── README.md       # Project documentation

# License
This project is licensed under the MIT License.
