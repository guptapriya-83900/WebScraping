from bs4 import BeautifulSoup
import requests
import pandas as pd

name=[]
required_skills=[]
html_text = requests.get(
    "https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation="
    ).text
soup=BeautifulSoup(html_text,'lxml')
'''
First figuring out tags in single job card
job=soup.find('li', class_='clearfix job-bx wht-shd-bx')
company_name=job.find('h3',class_='joblist-comp-name').text.replace(' ','')
skills = job.find('div', class_='more-skills-sections').text.replace('\n','')
job_posted_date = job.find('span',class_="sim-posted").span.text
print(job_posted_date) 

'''

job_cards=soup.find_all('li', class_='clearfix job-bx wht-shd-bx')
for job in job_cards:
    job_posted_date = job.find('span',class_="sim-posted").span.text
    #if 'few' in job_posted_date:              --Another way of putting condition
    if job_posted_date == 'few days ago':
        company_name=job.find('h3',class_='joblist-comp-name').text.strip().replace('\t', '').replace('\n', '')
        skills = job.find('div', class_='more-skills-sections').text.strip()
        skills = ' '.join(skills.split())  # Remove multiple spaces and clean the string
        skills = skills.replace(' ', ', ')  # Ensure proper spacing after commas
        name.append(company_name)
        required_skills.append(skills)


data = pd.DataFrame({'Company_Name':name,'Skills':required_skills})
print(data.head())

data.to_csv('jobs.csv',index=False,header=True)

    # print(f'''
    # Company Name: {company_name}
    # Required Skills: {skills}
    # ''')


#print(job_cards)

