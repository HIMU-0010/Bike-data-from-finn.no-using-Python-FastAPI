## Finn.no Bike Data Scraper with FastAPI and MongoDB

This Python project provides a web scraping script that scrapes bike data from Finn.no and uploads it to a MongoDB database using a FastAPI API.

**Features:**

* Scrapes bike listings from Finn.no's "Mobility" section.
* Extracts essential information like name, year, and price.
* Uploads scraped data to a MongoDB collection.
* Exposes an API endpoint (`/get_data`) to retrieve the scraped data.

**Requirements:**

* Python 3.x
* Requests library (`pip install requests`)
* BeautifulSoup library (`pip install beautifulsoup4`)
* PyMongo library (`pip install pymongo`)
* Pydantic library (`pip install pydantic`)
* FastAPI library (`pip install fastapi`)
* Uvicorn library (`pip install uvicorn`)

**Installation:**

1. **Install Dependencies:**

   ```bash
   pip install requests beautifulsoup4 pymongo pydantic fastapi uvicorn
Set up MongoDB:

Install and start a MongoDB instance. Refer to the MongoDB documentation for installation and configuration instructions.
Usage:

Run the Script:

Bash
```
python app.py
```
This will start the FastAPI server on the default port (usually 8000).

Access the API:

Make a GET request to the /get_data endpoint:


Contributing:

Feel free to fork this repository, make improvements, and submit pull requests!
