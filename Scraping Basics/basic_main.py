from bs4 import BeautifulSoup
# import pandas as pd

# name=[]
# price=[]
with open("home.html",'r') as html_file:
    content = html_file.read()   
    # print(content)  
    soup=BeautifulSoup(content,"lxml")  
    #print(soup.prettify())  
    #tags=soup.find("h5")                     #This find method only displays the first occurnce of h5. So if there are more than one h5 tag it won't display all of them
    # course_html_tags=soup.find_all("h5")                  #To find all the occurrences
    # #print(course_html_tags)  
    # for course in course_html_tags:
    #     print(course.text)        
    course_card=soup.find_all('div',class_="card")
    for course in course_card:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        # name.append(course_name)
        # price.append(course_price)
        print(f'Course_name: {course_name}, Course_price: {course_price}')

# data = pd.DataFrame({'name': name, 'price': price})
# print(data.head())