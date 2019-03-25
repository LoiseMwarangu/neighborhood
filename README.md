# Neighbourwatch

##  Created by
Loise Wangari Mwarangu

## Link to deployed site
https://loisewatch.herokuapp.com/

## Project Description
This is a website application where a user can view other neighbourhoods within.

## how it works
a user can:
* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.




## Setup and installations
- Python3.6
- Virtual environment
- Django
- Pip

To run the application do the following:
- clone this repo by running:
` https://github.com/LoiseMwarangu/neighbourhood`
- set up a virtual environment
 ` python3.6 -m venv  python3.6 -m venv virtual `
 - activate virtual environment
  ` source virtual/bin/activate `
- to install all requirements
` pip install -r "requirements.txt" `
 - touch a file .env and put in the following configurations:
   ```
      - SECRET_KEY=<secret key>
      - DEBUG=False
      - DB_NAME=<database name>
      - DB_USER='<username>
      - DB_PASSWORD=<your password>
      - DB_HOST='127.0.0.1'
      - MODE='dev'
      - ALLOWED_HOSTS=<your site name>
      - DISABLE_COLLECTSTATIC=1
   ```

- run the application locally with
 ` python manage.py runserver `
## Behavior Driven Development
* The program should navigate to the login page on load:

     **Input Example**: On page load

     **Output Example**: Navigate to the login page

* The program should navigate to sign up page when Sign Up is clicked on the login form:

     **Input Example**: Click on **Sign Up** on the login form

     **Output Example**: Redirected to the sign up page

* The program should navigate to the login page when Logout is clicked on the navigation bar:

     **Input Example**: Click on **Logout** on the navigation bar

     **Output Example**: Redirected to the login page

* The program should direct the user to their neighborhood page when logged in and already has a neighborhood:

    **Input Example**: Log in

    **Output Example**: Redirected to their neighborhood page

* The program should direct the user to the index page with neighborhood listings when logged in and has no neighborhood:

    **Input Example**: Log in

    **Output Example**: Redirect the user to the index page with neighborhood listings

* The program should navigate to the profile page when the My Profile is clicked on the navigation bar:

    **Input Example**: Click on **My Profile** on the navigation bar

    **Output Example**: Redirected to the profile page

* The program should navigate to the admin dashboard when one logs in as an admin:

    **Input Example**: Login in as Admin

    **Output Example**: Navigate to the admin dashboard

## likely bugs
Currently the application has no known bugs.
## Testing
- to run tests run ` python manage.py test app `
## technologies used
The technologies used to build the application are:

- Python3.6 
- Django 1.11
- Postgresql
- Bootstrap4
- css
- heroku live server



## LICENCE
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.