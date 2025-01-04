from bs4 import BeautifulSoup
import requests
import pandas as pd
import time

name=[]
required_skills=[]
info=[]


def find_jobs():
    html_text = requests.get(
        "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation="
        ).text
    soup=BeautifulSoup(html_text,'lxml')
    job_cards=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
    new_jobs = []  # List to store new jobs temporarily
    for job in job_cards:
        job_posted_date = job.find('span',class_="sim-posted").span.text
        if job_posted_date == 'few days ago':
            company_name=job.find('h3',class_='joblist-comp-name').text.strip().replace('\t', '').replace('\n', '')
            skills = job.find('div', class_='more-skills-sections').text.strip()
            skills = ' '.join(skills.split())  
            skills = skills.replace(' ', ', ') 
            more_info=job.find('a')['href']
            # Combine company_name and more_info as a unique identifier
            job_id = (company_name, more_info)
            if job_id not in zip(name, info):  # Avoid duplicates
                name.append(company_name)
                required_skills.append(skills)
                info.append(more_info)
                new_jobs.append({'Company_Name': company_name, 'Skills': skills, 'More_Info': more_info})

     # Create a DataFrame for the new jobs
    if new_jobs:
        new_jobs_df = pd.DataFrame(new_jobs)
        return new_jobs_df
    else:
        return None



if __name__=='__main__':
    csv_file='jobs.csv'
    try:
        # Load existing data if CSV already exists
        existing_data = pd.read_csv(csv_file)
        name = existing_data['Company_Name'].tolist()
        required_skills = existing_data['Skills'].tolist()
        info = existing_data['More_Info'].tolist()
    except FileNotFoundError:
        # If file does not exist, initialize as empty DataFrame
        existing_data = pd.DataFrame(columns=['Company_Name', 'Skills', 'More_Info'])

    while True:
        # Fetch new jobs
        new_jobs_df = find_jobs()

        if new_jobs_df is not None:
            # Append new jobs to existing data
            updated_data = pd.concat([existing_data, new_jobs_df], ignore_index=True)
            updated_data.to_csv(csv_file, index=False)  # Save to CSV
            print(f"Added {len(new_jobs_df)} new jobs to the CSV file.")

            # Update existing data
            existing_data = updated_data
        else:
            print("No new jobs found.")

        waiting_time = 10
        print(f"Waiting {waiting_time} minutes....")
        time.sleep(waiting_time * 60)  # Wait for 10 minutes before checking again           


