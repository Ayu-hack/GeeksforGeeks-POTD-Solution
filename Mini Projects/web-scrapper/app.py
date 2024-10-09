from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin
import re

app = Flask(__name__)

# Create a directory for images if it doesn't exist
IMAGE_FOLDER = os.path.join('static', 'images')
os.makedirs(IMAGE_FOLDER, exist_ok=True)

def is_valid_filename(filename):
    """Check if the filename is valid (not empty and doesn't contain invalid characters)."""
    return bool(filename) and not re.search(r'[<>:"/\\|?*]', filename)

@app.route('/', methods=['GET', 'POST'])
def index():
    titles = []
    images = []
    if request.method == 'POST':
        url = request.form['url']
        try:
            response = requests.get(url)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')

                # Scraping titles (e.g., h1, h2, h3 tags)
                title_tags = soup.find_all(['h1', 'h2', 'h3'])  # Include h1, h2, h3
                titles = [title.get_text(strip=True) for title in title_tags]

                # Scraping and saving image URLs
                img_tags = soup.find_all('img')
                for img in img_tags:
                    if 'src' in img.attrs:
                        img_url = img['src']
                        # Handle relative URLs
                        img_url = urljoin(url, img_url)  # Ensure URL is absolute

                        # Fetch the image
                        img_data = requests.get(img_url).content
                        img_name = os.path.basename(img_url)

                        # Validate image name before saving
                        if is_valid_filename(img_name):
                            img_path = os.path.join(IMAGE_FOLDER, img_name)

                            # Save the image to the static/images folder
                            with open(img_path, 'wb') as img_file:
                                img_file.write(img_data)

                            images.append(img_path)  # Save the path of the image

            else:
                titles = [f"Error: Unable to retrieve page (Status code: {response.status_code})"]
        except Exception as e:
            titles = [str(e)]
    return render_template('index.html', titles=titles, images=images)

if __name__ == '__main__':
    app.run(debug=True)
