# Personal Expense Tracker

A simple **Personal Expense Tracker** built with Python, featuring expense logging, category-based tracking, and visualizations via a pie chart.

## Features

- **Add Expenses**: Log expenses by amount, category, and optional date (defaults to today).
  - Categories available: 
    Grocery, Stationary, Electronics, Household, Clothing, Transport, Entertainment, Fast Food, Other

- **View Expenses**: Displays a table of all logged expenses with the option to delete any entry.
  
- **Visualize Expenses**: A **pie chart** dynamically shows the distribution of expenses across different categories.

- **Data Persistence**: All data is stored in `expenses.json`, so expenses persist even after the application is closed.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/expense-tracker.git
    cd expense-tracker
    ```

2. Install required libraries (e.g., `matplotlib`):
    ```bash
    pip install -r requirements.txt
    ```

3. Run the application:
    ```bash
    python tracker.py
    ```

## Usage

1. **Add Expense**: Enter the amount, select the category, and add the expense (optional date input).
2. **View & Delete Expenses**: Manage and delete expenses through the table view.
3. **Pie Chart**: View a pie chart of expenses updated in real-time based on categories.

## File Structure

```text
.
├── tracker.py       # Main Python script
├── expenses.json    # Stores expense data
├── README.md        # Documentation
└── requirements.txt # Required libraries
