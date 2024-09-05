# Glad Tidings Times

![Responsive Mockup](/static/images/responsive.PNG)

**Glad Tidings Times** is a positive news platform designed to share uplifting and heartwarming stories. In a world filled with negative headlines, this platform aims to bring a smile to your face by focusing on the good news happening around us.

## Project Overview

**Glad Tidings Times** is a full-stack web application developed to provide users with positive and uplifting news. The goal is to share stories of joy, kindness, and inspiration, creating a refuge from the often overwhelming negative news cycle.

## Agile Development and User Stories

The project followed Agile principles, utilizing a Kanban board to track the progress of user stories and tasks. The user stories were prioritized using the MoSCoW method (Must-have, Should-have, Could-have, and Won't-have).

Here’s an overview of the user stories implemented for the project:

### Must-have (M)

1. **Posting News Stories** - Users must be able to post stories.
2. **Creating an Account** - Users must be able to create an account to access certain features.
3. **Reading News Stories** - All users should be able to read news stories without authentication.

### Should-have (S)

1. **Commenting on News Stories** - Users should be able to comment on news posts.
2. **Upvoting and Downvoting Posts** - Users should have the ability to vote on posts.

### Could-have (C)

1. **Categorizing Posts by Topic** - Posts could be categorized based on topics for better organization.

---

The image below represents the project Kanban board used to track the progress of these user stories:

![Kanban Board](/User%20stories.PNG)

## Design and Wireframes

During the planning stages of the project, wireframes were created to visualize the layout of key pages and guide the development of the user interface. These wireframes ensured that the website followed a clear, user-friendly structure.

**Homepage Wireframe**: The homepage features a header, navigation bar, and sections for displaying news stories.

![Homepage Wireframe](/New%20Wireframe%201.png)

**Post Creation Wireframe**: This page allows users to create a post, providing input fields for the post's title, content, category, and image upload.

![Post Creation Wireframe](/New%20Wireframe%202.png)

## Features

- User registration and authentication
- Create, edit, and delete posts
- Comment on posts
- Upvote and downvote posts
- User profile management
- Role-based access control

- **User Feedback on CRUD Operations**: Users receive feedback through notifications when creating, editing, or deleting posts. A success message is shown for successful operations, and an error message is shown if the operation fails.

## Technologies Used

- Django
- HTML, CSS, JavaScript
- PostgreSQL
- Cloudinary
- Summernote

## Set up Details

Install Django and Create a Project and App

In the terminal, type the following commands to install a recommended version of Django and the necessary libraries:

The images for this project will be hosted by Cloudinary. That requires some libraries to be installed. For that we use the following commands:

At this stage we can create the requirements.txt file, with the command:

pip3 freeze --local > requirements.txt

## Create a new Django project and app:

django-admin startproject reddit_news.
python3 manage.py startapp news

In the “reddit_news” folder, edit the settings.py to include the new app “news”. It is also necessary to update the setting ALLOWED_HOSTS.
The changes now need to be migrated to the data base:

python3 manage.py makemigrations
python3 manage.py migrate

To run the server simply type on the terminal

python3 manage.py runserver

Configure Cloudinary, PostgresSQL and Heroku

## Cloudinary

Login to Cloudinary.com and go to Dashboard.

There, copy the API Environment variable (CLOUDINARY_URL) and the API Secret Key.

## PostgreSQL From Code Institute

Open up your provided link crom code institute and follow the instructions,

Then copy the PostgreSQL URL, create a env.py and add the copied URL

## env.py and Secret Key

Create an env.py file, and set it up as the code below. Using the URLs mentioned above and a a “Secret Key” you will create. Below there's a sample how the env.py should look like:

import os
os.environ\["DATABASE_URL"\] = "postgres://DATA-BASE-URL"
os.environ\["SECRET_KEY"\] = "CREATE-YOUR-OWN-KEY"
os.environ\["CLOUDINARY_URL"\] = "cloudinary://COUDINARY-ADDRESS"

This the same SECRET_KEY is necessary to update settings.py and Heroku.

In the settings.py created by Django, import the env.py file and the Secret key.

from pathlib import Path
import os
import dj_database_url

if os.path.isfile("env.py"):
    import env

# Heroku Deployment

## To deploy the site to Heroku, follow these steps:

- Create a Heroku Account.
- Create a New App, once you are logged in,click the "New" button located in the top-right corner of the Heroku dashboard. Then, select "Create new app" from the options provided.
- Name Your App, enter a unique and meaningful name for your app.
- Choose Region and Create App,
- select a region that is geographically closer to your target audience. After choosing the region, click "Create app" to set up your new app.
- Configure Environment Variables, go to the "Settings" tab, then click "Reveal Config Vars." Here, add the following

## environment variables for heroku:

- SECRET_KEY: The same Secret Key in the project's env.py.
- DATABASE_URL: The PostgreSQL URL of the instance created for this project.
- CLOUDINARY_URL: The URL for your Cloudinary API.

## Testing

## Responsiveness Testing

The site's responsiveness was tested using [Responsive](/static/images/responsive.PNG) on the following screen sizes:

- **Mobile**: iPhone 6/7/8
- **Tablet**: iPad
- **Desktop**: 1920x1080 resolution

| **Screen Size**     | **Expected Result**                            | **Actual Result**                                  | **Fixes Applied** |
| ------------------- | ---------------------------------------------- | -------------------------------------------------- | ----------------- |
| **Mobile (iPhone)** | The layout should adjust to a single column    | The layout adjusted to a single column as expected | None              |
| **Tablet (iPad)**   | The layout should display in two columns       | The layout displayed in two columns as expected    | None              |
| **Desktop**         | The layout should display in its original form | The layout displayed as expected on desktop        | None              |

## Automated Testing

Automated tests were written to verify the functionality of models, views, and URLs within the application.

### 1. PostModelTest Class (Model Testing)

This class tests the functionality of the `Post` model, ensuring that key behaviors like slug creation and upvote/downvote functionality work as expected.

- **setUp Method**:

  - **Purpose**: This method creates a test user, a test category, and a test post. These objects are used throughout the tests.
  - **Objects Created**:
    - A user (`testuser`)
    - A category (`Test Category`)
    - A post (`Test Post`) authored by the test user.

- **test_slug_creation**:

  - **Purpose**: Verifies that the slug for a post is correctly generated from the title.
  - **Expected Result**: The post's slug should be `"test-post"`.

- **test_upvotes**:

  - **Purpose**: Tests the upvote feature by adding an upvote from the user.
  - **Expected Result**: The post should register 1 upvote from the user.

- **test_downvotes**:
  - **Purpose**: Tests the downvote feature by adding a downvote from the user.
  - **Expected Result**: The post should register 1 downvote from the user.

### 2. PostViewsTest Class (View Testing)

This class tests the views associated with posts, such as rendering the homepage, post details, and creating new posts.

- **setUp Method**:
  - **Purpose**: This method creates the test user, category, and post used in the tests.
- **test_index_view**:

  - **Purpose**: Ensures that the homepage (index view) renders successfully.
  - **Expected Result**: The homepage should return a `200 OK` status.

- **test_post_detail_view**:

  - **Purpose**: Tests whether the post detail page renders correctly when accessing a post by its slug.
  - **Expected Result**: The post detail page should return a `200 OK` status.

- **test_create_post_view**:
  - **Purpose**: Ensures that a logged-in user can successfully create a new post.
  - **Expected Result**: The response should return a `200 OK` status after following any redirections.

### 3. TestUrls Class (URL Resolution Testing)

This class tests the URL-to-view resolution, ensuring that URLs are mapped correctly to their corresponding views.

- **test_index_url_resolves**:

  - **Purpose**: Verifies that the `index` URL resolves to the `index` view function.
  - **Expected Result**: The `reverse('index')` should resolve to the `index` function.

- **test_post_detail_url_resolves**:
  - **Purpose**: Ensures that the `post_detail` URL resolves to the correct view function when provided with a valid slug.
  - **Expected Result**: The `reverse('post_detail', args=['test-post'])` should resolve to the `post_detail` function.

---

### Summary

These tests ensure that:

- **Models**: Verify slug creation and upvote/downvote functionality.
- **Views**: Ensure that the index page, post detail page, and post creation process work as expected.
- **URLs**: Validate that URLs are correctly mapped to their expected view functions.

[test results](/automation20test.PNG)

## Manual Testing

| **Feature**          | **Test Case**                                                                                          | **Expected Result**                                                                          | **Actual Result** | **Tested On**   |
| -------------------- | ------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------- | ----------------- | --------------- |
| **Authentication**   | Verify that a user can register on the website.                                                        | User is successfully registered and redirected to the homepage.                              | Pass              | Desktop, Mobile |
|                      | Verify that a user can log in once registered.                                                         | User can log in with valid credentials and access their account.                             | Pass              | Desktop, Mobile |
|                      | Verify that a user can sign out successfully.                                                          | User can sign out and is redirected to the homepage or login page.                           | Pass              | Desktop, Mobile |
|                      | Verify that a user can view but not manage posts or comments after signing out.                        | Signed-out users can view posts but do not have access to edit, delete, or manage comments.  | Pass              | Desktop, Mobile |
| **Posting Forms**    | Verify that a new post can be created.                                                                 | A new post is successfully created and displayed on the homepage.                            | Pass              | Desktop, Mobile |
|                      | Verify that a post can be edited.                                                                      | The post is edited and the changes are reflected on the homepage.                            | Pass              | Desktop, Mobile |
|                      | Ensure that a user can add an image with the post.                                                     | The post allows image uploads, and the image is displayed correctly.                         | Pass              | Desktop, Mobile |
|                      | Verify that a user can successfully delete a post.                                                     | The post is deleted and no longer appears on the homepage.                                   | Pass              | Desktop, Mobile |
|                      | Ensure that forms cannot be submitted when required fields are empty.                                  | The form shows validation errors when required fields are not filled, preventing submission. | Pass              | Desktop, Mobile |
| **Navigation Links** | Testing was conducted on both mobile and desktop devices to ensure navigation links function properly. | All navigation links correctly route to the respective pages across different devices.       | Pass              | Desktop, Mobile |

## Lighthouse Testing

![Lighthouse Report](/static/images/lighthouse%20score.PNG)

## Code Validation

The following tools were used to validate the code for compliance with web standards:

- **CSS Validation**: Using [W3C CSS Validator](http://jigsaw.w3.org/css-validator/validator?lang=en&profile=css3svg&uri=https%3A%2F%2Fpp4-news-eb7b0cc22f26.herokuapp.com%2F&usermedium=all&vextwarning=&warning=1).
- **HTML Validation**: Using [W3C HTML Validator](https://validator.w3.org/nu/?doc=https%3A%2F%2Fpp4-news-eb7b0cc22f26.herokuapp.com%2F).

| **File**       | **Validation Tool** | **Errors**     | **Fixes Applied** |
| -------------- | ------------------- | -------------- | ----------------- |
| **styles.css** | W3C CSS Validator   | No errors      | None              |
| **index.html** | W3C HTML Validator  | 2 minor errors | None              |

## Unresolved Bugs

Side bars dont display most populair news or latest news at this time

## Error Handling and Debugging

Several errors were encountered during the development process. These included issues with database configuration and static/media file serving. The detailed documentation of errors and their respective solutions can be found [here](/BUGG_DOCUMENTATION.md)

## Acknowledgements

Django documentation
Cloudinary documentation
Heroku documentation
Code Institute

## Credits

Code cleanup and adjustments were done with assistance from ChatGPT.
Spelling and grammar fixes were done with ChatGPT.
Readme layout about testing taken from [zemaciel ](https://github.com/zemaciel/pp4/blob/main/README.md#testing)

### Content

Icons sourced from [Font Awesome](https://fontawesome.com/).

### Media

Home and sign-up page photos and videos where taken from google
Favicons obtained from [Favicons.io](https://favicon.io/emoji-favicons/microscope/).
