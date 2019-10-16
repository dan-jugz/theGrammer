# theGram

### 30/08/2019

## By **[Daniel Njuguna](https://github.com/dan-jugz/theGram)**

## Description

This is a instagram clone web app made using the django framework that allows users to  mimic how instagram works.Users can post pictures,users can comment on them and the owner of the post can delete user comments,update posts and or delete blogs.

## User Stories

As a user I would like:

* Sign in to the application to start using.
* Upload my pictures to the application.
* See my profile with all my pictures.
* Follow other users and see their pictures on my timeline.
* Like a picture and leave a comment on it.
* Update my post
* Delete my post
* Comment on other posts




## Specifications

| Behavior        | Input           | Outcome  |
| ------------- |:-------------:| -----:|
| Register to be a user | Your email : john@doe.com  Username : jonDoo  Password : doe | New user is registered |
| User Log in | Your email : john@doe.com  Password : doe | Logged in |
| Create Post | Click Add Button |Authenticated User is redirected to a form page to create a new post|
| View Post | Click on Post title | Redirected to a page that has that single post|
| Comment on post | Fill the form field provided | Authenticated user is allowed to make a comment|
| Delete a Post | Click Trash Icon| Authenticated user i.e owner of the post is prompted to delete|
| Update a Post | Click Update Icon| Authenticated user i.e owner of the post is redireted to a foem field to update the post|
| Update profile | Click edit profile | Pop up modal to update your details |
| Search | type on search field| Redirect to a results page if query exists |


## Setup/Installation Requirements

* `$ git clone` [theGram](https://github.com/dan-jugz/theGram)
* `$ cd theGram`


    ```python
    #create a .env file
    SECRET_KEY = '<Secret_key>'
    DBNAME = 'insta'
    USER = '<Username>'
    PASSWORD = '<password>'
    DEBUG = True

    EMAIL_USE_TLS = True
    EMAIL_HOST = 'smtp.gmail.com'
    EMAIL_PORT = 587
    EMAIL_HOST_USER = '<your-email>'
    EMAIL_HOST_PASSWORD = '<your-password>'
    ```    

* `$ python3.6 -m venv virtual` to create a  virtual environment
* `$ source virtual/bin/activate` to activate the virtual environment
* `$ psql` to activate the postgres server
* `$ username=create database theGram` create db with the name theGram
* run `$ python3.6 -m pip install -r requirements.txt ` to install dependencies
* `$ python3.6 manage.py makemigrations` to initialize database migrations
* `$ python3.6 manage.py migrate` to commit the migration you are running
* `$ python3.6 manage.py runserver` to run the app
* open `localhost:8000` to view the app

## Known Bugs

* does not show posts on upload

## Technologies Used

* Python3.6
* Django 2.2.4
* Javascript
* Masonry Grid
* Bootstrap
* Postgres Database
* CSS
* HTML
* Heroku

### License

MIT (c) 2019 **[Daniel Njuguuna](https://github.com/dan-jugz/theGram)**

