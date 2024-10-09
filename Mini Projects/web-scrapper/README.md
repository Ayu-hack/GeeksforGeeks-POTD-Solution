# Web Scraper

This is a Python-based web scraper built using the Flask framework. The web scraper extracts titles (headings) and images from a given webpage URL and displays them in a structured format.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [Technologies Used](#technologies-used)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone 
    ```

2. Navigate into the project directory:

    ```bash
    cd web-scraper
    ```

3. Set up a virtual environment (optional but recommended):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

4. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

5. Run the Flask application:

    ```bash
    flask run
    ```

6. Open your browser and go to `http://127.0.0.1:5000` to use the web scraper.

## Usage

1. Input the URL of the webpage you want to scrape in the text input box.
2. Click the "Scrape" button.
3. The titles and images found on the webpage will be displayed on the screen.

## Features

- Scrapes headings and images from a specified webpage.
- Displays the scraped data in a clean and structured format.
- Responsive design for both desktop and mobile devices.
- Error handling for invalid URLs or non-scrapable pages.

## Project Structure

```bash
web-scraper/
├── static/
│   ├── css/
│   │   └── styles.css        # Contains the styles for the project
│   └── images/               # Stores scraped images
├── templates/
│   └── index.html            # Main HTML template
├── app.py                    # Flask application
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
