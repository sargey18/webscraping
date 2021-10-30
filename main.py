from bs4 import BeautifulSoup

# have to say how i will access the content 
# have to work with file objects 
#open and read the content of the file 
# file name first, 
# then the method you want to apply
as the variable we put on the end
with open('home.html', 'r') as html_file:
    # reading the html file variable saved to the variable content 
    content1 = html_file.read()
    # use the beautiful soup library to beautify content and its tags like python objects
    # we use a new vaariable to create a new instance of the beautfil soup
    #the arguments that go here will be the content we want to scrape
    soup = BeautifulSoup(content1, 'lxml')
    # we want to grab the h5 tags
   #- courses_html_tags = soup.find_all('h5')
   #- for course in courses_html_tags:
   #-     print(course.text)


    # filter the div cards 
    course_cards = soup.find_all('div', class_='card')
    for course in course_cards:
        # on each iteration store the text on each course h5 
        course_name = course.h5.text
        # store the course llink (price) on each iteration 
        course_price = course.a.text.split()[-1]

        print(course_name)
        print(course_price.text)

        print(f'{course_name} costs {course_price}')