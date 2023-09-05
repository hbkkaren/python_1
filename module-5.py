#  1 .Why Django should be used for web-development? Explain how you can create a project in Django?
#    Django is a high-level Python web framework that enables rapid development of secure and maintainable websites.
#    Built by experienced developers, Django takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.

# creating command for new project   " python manage.py startproject mysite ".

# 2.  How to check installed version of django?
#  python -m django --version or type pip freeze to see all the versions of installed modules including Django.

# 3.  Explain what does django-admin.py make messages command is used for?

# django-admin.py makemessages is a command-line tool that is used to create or update message files for translation in Django projects 12.
#  It scans the source code and extracts all strings marked for translation,creating or updating message files in the specified locale directory 

# 4 . What is Django URLs?make program to create django urls
# In Django, the URL dispatcher is responsible for mapping URLs to views. A clean and elegant URL scheme is an important detail in a high-quality web application 

# from django.urls import path
# from . import views

# # urlpatterns = [
#     path('home/', views.home, name='home'),
#     path('about/', views.about, name='about'),
#     path('contact/', views.contact, name='contact'),
# ]


#  5 . What is a QuerySet?Write program to create a new Post object in database:

# A QuerySet is a collection of database query results in Django 1. It is a way to filter and order data that is then presented to the user,
# typically in a template or API endpoint 2. QuerySets can be constructed, filtered, sliced, and generally passed around without actually hitting the database. 
# from myapp.models import Post

# post = Post(title='My Title', content='This is my content.')
# post.save()

# 6. Mention what command line can be used to load data into Django?



# 7.Make Django application to demonstrate following things o There will be 2 modules(Admin,Product manager) o Admin can add product name (ex.Product id and product name) ex. (1, Samsung), (2, Apple)...etc.
Data should store in