# ChoiceUrl - url-shortener

![landing page](https://github.com/PanasheR/url-shortener/blob/main/choiceurl/static/icon.png)

## Project Description <br>
Choiceurl is a web application that allows users to paste long urls for webstites and files, create short names for the urls and copy the link to the short names to their clipboard
<br>It also helps users access the codes they created by making use of the user's browser session data collected using cookies and displays the user's short names in form of a list 
the home page.<br>

## Project Context
This project is a portofolio project for ALX Software Engineering Foundation Progaram.

## Tutorial
![landing page](https://github.com/PanasheR/url-shortener/blob/main/landingpage.jpeg)
- The user doesn't need aunthentication to access this site
- The user can enter the long links on using the forms on website url or file url input fields.
- The user will have to enter short names of his/her choice too or else the shorten button won't work
- After the user enters the prefered form, he/she can then click the shorten button and is redirected to your-url page
![your-urlpage](https://github.com/PanasheR/url-shortener/blob/main/Web%20capture_24-3-2022_221327_127.0.0.1.jpeg)
- The user can copy the short name/link he/she generated to the clibboard
- To navigate back to homepage, the user should click on new url on the navigation bar
- Back on the homepage, the short name the user created will be displayed as a list under title: Codes you have created
- The user can also click on API in the navigation to access the API endpoint for the codes he/she created
![api](https://github.com/PanasheR/url-shortener/blob/main/choiceurl/static/wireframe-2.png)
- If the user clicks on API, he/she is directed to the website's API endpoint

## The Team
- [Panashe Rusakaniko](https://twitter.com/PanasheRusakan2) : Panashe Rusakaniko likes writing short stories and gaming during his spare time.

## Architecture
![architecture](https://github.com/PanasheR/url-shortener/blob/main/Web%20architecture.png)
1. The user access visits the web application using his/her browser
2. The web application is served by flask jinja templates
3. If the user sends a get request he/she will be redirected to the home page over and over again until he/she sends a POST request i.e<br>
   Usess the forms to input urls
4. When the user inputs his/her short urls, a POST method is sent to a server and the server will store the website urls and short names in a json document
5. The server will also return a POST request to the user with his/her link and redirect the user to a page where he/she can copy the short link he/she created
6. The application will also use cookies to grab the user's browser session data and display the links the user created on his/her home page as a link

| Component | Description |
| --- | --- |
| `wsgi.py` | File in root directory neccessary for deployment on heroku. The file calls create_app() from our app module. The function will tell heroku to launch app|
| `requirements.txt` | Has modules needed for the flask app to function |
| `Procfile` | This file is the one that shows heroku that we are using a gunicorn server for deployement of our app|
| `Pipfile.lock` | ntended to specify, based on the packages present in Pipfile, which specific version of those should be used, avoiding the risks of automatically upgrading packages that depend upon each other and breaking your project dependency tree.|
| `choiceurl` | Directory/module that contains the application |
| `__init__.py ` | Creates the create_app() function that calls the app instance and also registers the app blueprint |
| `choiceurl.py ` | Main file that creates all the routes for the application, renders templates, handles errors and creates API endpoints |
| `conftest.py` | Calls the app for tests using pytest |
| `test_app.py` | Files performs one test for the shorten button on the home page|
| `static` | Has static files such as css file and images|
| `templates` | Has html templates for the frontend|

## FLASK 
I decided to use flask for backend because it is best for the microservices I needed for my web application.<br> It is also a microframework that works best with mini applications such as mine.<br> I also wanted to implement cookies that store user's browser session data and Flask provides the session module for that.<br> Lastly Flask helped me break my application into multiple blueprints.

## Heroku
I decided to use Heroku for deployment because it is easier to push the files to heroku for deployment. 

## How to deploy
1. First clone this repo:
   ``` git clone https://github.com/PanasheR/url-shortener.git```
2. cd into the repo
   ``` cd url-shortener ```
3. install pipenv that serves both for pip and virtual environment
   ```pipenv install```
4. creates a virtual environment in that directory using pipenv
   ```pipenv shell```
5. install flask, gunicorn and pytest
   ```
   pipenv install flask
   pip install -U pytest
   ```
6. Create a heroku account on heroku.com and link the github repo to heroku and deploy

## Acknowledgements
1. [ALX](https://www.alxafrica.com) - For the staff's help, guidance and the knowledge

## Created By:
Yours truly:
### Panashe Rusakaniko
- I acknowledge that this work is mine, done by me, for me and ALX Foundations program
