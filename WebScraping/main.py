from bs4 import BeautifulSoup
import requests
import pandas as pd

name=[]
required_skills=[]
info=[]
# print('Put some skills that you are not familiar with')
# unfamiliar_skill=input('>').split(',')
# print(f"Filtering out {unfamiliar_skill}")

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
        more_info=job.find('a')['href']
        # more_info=job.a['href']      ---Another way of extracting detail
        # Check if none of the unfamiliar skills are in the skills list. This is for getting only the required skills job
        # if not any(remove_skills.casefold() in skills.casefold() for remove_skills in unfamiliar_skill):
        #     print(f"Company Name: {company_name}")
        #     print(f"Required Skills: {skills}")
        #     print(f"More info: {more_info}")
        #     print("\n")
        name.append(company_name)
        required_skills.append(skills)
        info.append(more_info)
       

    


data = pd.DataFrame({'Company_Name':name,'Skills':required_skills, 'More_info':info})
print(data.head())

#data.to_csv('jobs.csv',index=False,header=True)




