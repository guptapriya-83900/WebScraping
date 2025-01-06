# Web Scraping Project

## Overview

This project demonstrates the use of web scraping techniques to extract job postings from the [TimesJobs](https://www.timesjobs.com/) website. It fetches job listings based on specific criteria (e.g., jobs posted within the last few days), stores the data in a CSV file, and updates the file periodically to include new job postings.

The project uses **Python**, **BeautifulSoup**, and **Pandas** to scrape and manage data efficiently.

---

## Features

- **Real-time scraping**: The script fetches job postings from TimesJobs every 10 minutes.
- **Data storage**: The extracted job data is saved into a `jobs.csv` file.
- **Duplicate handling**: Ensures no duplicate jobs are added to the CSV file.
- **Customizable**: The scraping logic can be modified to target other job criteria or websites.
- **Automated updates**: Automatically appends new job postings to the CSV file without overwriting existing data.

---

## Project Structure

```
WebScraping/
├── jobs.csv                # The CSV file where scraped job data is stored
├── near_realtime_scraping.py  # Main script for scraping jobs and updating the CSV
├── README.md               # Project documentation
├── requirements.txt        # Dependencies for the project
├── Scraping Basics/        # Folder containing other examples and experiments
│   ├── basic_main.py
│   ├── home.html           # Sample HTML file for testing
├── .gitignore              # Files and folders to be ignored by Git
└── lxml_basics.txt         # Notes on the lxml parser
```

---

## Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd WebScraping
   ```

2. **Set up the environment**:
   - Create and activate a Python virtual environment (optional but recommended):
     ```bash
     python -m venv scraping-env
     source scraping-env/bin/activate    # For Linux/Mac
     scraping-env\Scripts\activate       # For Windows
     ```

3. **Install dependencies**:
   - Install the required packages using `pip`:
     ```bash
     pip install -r requirements.txt
     ```

4. **Run the script**:
   - Execute the main script to start scraping:
     ```bash
     python near_realtime_scraping.py
     ```

---

## How It Works

1. **Job scraping**:
   - The script sends a request to TimesJobs to fetch job postings for the keyword "Python."
   - It parses the HTML response using **BeautifulSoup** and extracts details such as:
     - Company name
     - Required skills
     - Job posting date
     - Job link

2. **Data management**:
   - The extracted job data is stored in `jobs.csv`.
   - Each job entry is uniquely identified by its company name and job link to avoid duplicates.

3. **Automated updates**:
   - The script runs in a loop and checks for new jobs every 10 minutes.
   - New job postings are appended to `jobs.csv` if they are not already present.

---

## Example Output

### Sample `jobs.csv` File:
| Company_Name           | Skills                      | More_Info                   |
|------------------------|----------------------------|----------------------------|
| Peopleplease Consulting| Python, Django, Flask      | https://example.com/job1   |
| Analytics Vidhya       | Machine Learning, NLP      | https://example.com/job2   |
| Seven Consultancy      | Data Science, SQL          | https://example.com/job3   |

---

## Customization

You can customize this script to:
- Scrape jobs for different keywords by modifying the `searchTextText` and `txtKeywords` parameters in the request URL.
- Change the frequency of updates by modifying the `waiting_time` variable in the script.

---

## Requirements

The following Python libraries are required:
- **BeautifulSoup4**: For parsing HTML content
- **Requests**: For sending HTTP requests
- **Pandas**: For managing and saving data

All dependencies are listed in the `requirements.txt` file and can be installed using:
```bash
pip install -r requirements.txt
```

---

## Notes

- Ensure that you follow the terms of service of the website you are scraping.
- Be mindful of overloading the server by scraping too frequently.
- Use this project responsibly for learning or job tracking purposes.

---

## Acknowledgements

This project was developed for educational purposes to demonstrate web scraping techniques in Python.
