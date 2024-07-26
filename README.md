  
# Glad Tidings Times

![Responsive Mockup](/static/images/responsive.PNG)

**Glad Tidings Times** is a positive news platform designed to share uplifting and heartwarming stories. In a world filled with negative headlines, this platform aims to bring a smile to your face by focusing on the good news happening around us.



## Project Overview

**Glad Tidings Times** is a full-stack web application developed to provide users with positive and uplifting news. The goal is to share stories of joy, kindness, and inspiration, creating a refuge from the often overwhelming negative news cycle.

  

## Features

*   User registration and authentication
*   Create, edit, and delete posts
*   Comment on posts
*   Upvote and downvote posts
*   User profile management
*   Role-based access control

## Technologies Used

*   Django
*   HTML, CSS, JavaScript
*   PostgreSQL
*   Cloudinary
*   Summernote


## Set up Details

Install Django and Create a Project and App

In the terminal, type the following commands to install a recommended version of Django and the necessary libraries:

The images for this project will be hosted by Cloudinary. That requires some libraries to be installed. For that we use the following commands:

At this stage we can create the requirements.txt file, with the command:

pip3 freeze --local > requirements.txt

## Create a new Django project and app:

django-admin startproject reddit\_news.
python3 manage.py startapp news

In the “reddit\_news” folder, edit the settings.py to include the new app “news”. It is also necessary to update the setting ALLOWED\_HOSTS.
The changes now need to be migrated to the data base:

python3 manage.py makemigrations
python3 manage.py migrate


To run the server simply type on the terminal

python3 manage.py runserver

Configure Cloudinary, PostgresSQL and Heroku


## Cloudinary


Login to Cloudinary.com and go to Dashboard.

There, copy the API Environment variable (CLOUDINARY\_URL) and the API Secret Key.


## PostgreSQL From Code Institute


Open up your provided link crom code institute and follow the instructions,


Then copy the PostgreSQL URL, create a env.py and add the copied URL

  

## env.py and Secret Key

  

Create an env.py file, and set it up as the code below. Using the URLs mentioned above and a a “Secret Key” you will create. Below there's a sample how the env.py should look like:

  

import os
os.environ\["DATABASE\_URL"\] = "postgres://DATA-BASE-URL"
os.environ\["SECRET\_KEY"\] = "CREATE-YOUR-OWN-KEY"
os.environ\["CLOUDINARY\_URL"\] = "cloudinary://COUDINARY-ADDRESS"

  

This the same SECRET\_KEY is necessary to update settings.py and Heroku.

  

In the settings.py created by Django, import the env.py file and the Secret key.

  

from pathlib import Path
import os
import dj\_database\_url

if os.path.isfile("env.py"):
    import env

  

# Heroku Deployment

  

## To deploy the site to Heroku, follow these steps:

  

*   Create a Heroku Account.
*    Create a New App, once you are logged in,click the "New" button located in the top-right corner of the Heroku dashboard. Then, select "Create new app" from the options provided.
*   Name Your App, enter a unique and meaningful name for your app.
*   Choose Region and Create App,
*   select a region that is geographically closer to your target audience. After choosing the region, click "Create app" to set up your new app.
*   Configure Environment Variables, go to the "Settings" tab, then click "Reveal Config Vars." Here, add the following

  

## environment variables:

  

*   SECRET\_KEY: The same Secret Key in the project's env.py.
*   DATABASE\_URL: The PostgreSQL URL of the instance created for this project.
*   CLOUDINARY\_URL: The URL for your Cloudinary API.

##   

## Deployment from GitHub:

  

*   In the Heroku dashboard, go to the "Deploy" tab. Scroll down to "Connect to GitHub" and sign in/authorise your GitHub account when prompted.
*   Then, search for the repository you want to deploy and click "Connect."

## Manual Deployment:

*   After connecting your repository, scroll down to the "Manual deploy" section. Choose the "main" branch (or any other appropriate branch) and click "Deploy" to initiate the deployment process.


## Usage

*   Navigate to `http://127.0.0.1:8000` in your web browser.
*   Register a new user or log in with an existing account.
*   Explore, create, edit, delete, and interact with posts and comments.

## Deployment

1.  Ensure all dependencies are listed in `requirements.txt`.
2.  Configure environment variables on the deployment platform (e.g., Heroku).
3.  Create a `Procfile` for Heroku deployment:


web: gunicorn glad\_tidings\_times.wsgi

1.  Deploy the application:

```sh
Copy code
git push heroku main
```
## Testing

 **Authentication**
    - Verify that a user can register on the website. - Pass
    - Verify that a user can log in once registered. - Pass
    - Verify that a user can sign out successfully. - Pass
    - Verify that a user can view but not manage posts or comments after signing out. - Pass
 **Booking Forms**
    - Verify that a new post can be created. - Pass
    - Verify that a post can be edited. - Pass
    - Ensure a user can ad an image with the post. - Pass
    - Verify that a user can successfully delete a bpost. - Pass
    - Ensure forms cannot be submitted when required fields are empty. - Pass
 **Navigation Links**
    
    Testing was conducted on both mobile and desktop devices to ensure that all navigation links on the respective pages correctly navigated to the designated pages, following the design. This was accomplished by clicking on the navigation links on each page from various devices.
     Pass

## Lighthouse Testing

![Lighthouse Report](/static/images/lighthouse%20score.PNG)

## HTML Validation
Due to the Django templating language, direct input of the HTML code into the validator was not possible.

## CSS

No errors were found when passing through the official Jigsaw validator.
 [link to validation](http://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2Fpp4-news-eb7b0cc22f26.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1)


## Unresolved Bugs

Side bars dont display most populair news or latest news at this time

  
## Acknowledgements

Django documentation
Cloudinary documentation
Heroku documentation
Code Institute

## Credits 

Code cleanup and adjustments were done with assistance from ChatGPT.
Spelling and grammar fixes were done with ChatGPT.

### Content 
Icons sourced from [Font Awesome](https://fontawesome.com/).

### Media

Home and sign-up page photos and videos where taken from google
Favicons obtained from [Favicons.io](https://favicon.io/emoji-favicons/microscope/).