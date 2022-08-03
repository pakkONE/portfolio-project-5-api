# PP5 API - SportsTalk

## Project Description
SportsTalk is a content sharing platform that connects people from all four corners of the earth to share knowledge in what they are passionate about. The platform is powered by a Django REST API and React.<br>This Readme contains only to the back end part and the front end part can be found [here](https://github.com/pakkONE/portfolio-project-5-react)

## User stories
| Category  | as a     | I want to                      | so that I can                                                                     | mapping API feature                          |
| --------- | -------- | ------------------------------ | --------------------------------------------------------------------------------- | -------------------------------------------- |
| auth      | user     | sign up for an account         | create a profile on the site                                                      | dj-rest-auth<br>Create profile (signals)     |
| auth      | user     | sign up for an account         | create, like and comment on posts                                                 | Create post<br>Create comment                |
| posts     | visitor  | view an individual post        | to see community engagements by comments and likes                                | Retrieve                                     |
| posts     | visitor  | view all posts as a list       | browse the most recent posts                                                      | List/ Filter posts                           |
| posts     | visitor  | search a list of posts         | find a post by a specific user or title                                           | List/ Filter posts                           |
| posts     | visitor  | scroll through all posts       | have a more slick experience when browsing posts                                  | List/ Filter posts                           |
| posts     | user     | edit and/or delete my post     | make corrections to mistakes or regret making a post                              | Update property<br>Destroy property          |
| posts     | user     | create a post                  | share my thoughts and ideas with others                                           | Create post                                  |
| comments  | user     | create a comment               | share my thoughts on other people's content                                       | Create comment                               |
| comments  | user     | edit and delete my comment     | make corrections to mistakes or regret making a comment                           | Update comment<br>Destroy comment            |
| likes     | user     | like a post                    | to engage in content I like                                                       | Create like                                  |
| likes     | user     | unlike a post                  | if I for some reason no longer like the content the user posted                   | Destroy like                                 |
| profiles  | visitor  | view a profile                 | learn more about an individual user and see their recent posts                    | Retrieve profile<br>List/ filter posts       |
| profiles  | user     | edit my profile                | update my profile                                                                 | Update profile                               |

## Entity Relationship Diagram
![ERD Diagram](https://res.cloudinary.com/dv6cgny0t/image/upload/v1658412279/ERD_PP5_wdwjhc.png)

## CRUD breakdown of Models
| model     | endpoints                    | create        | retrieve | update | delete | filter                   | text search |
| --------- | ---------------------------- | ------------- | -------- | ------ | ------ | ------------------------ | ----------- |
| users     | users/<br>users/:id/         | yes           | yes      | yes    | no     | no                       | no          |
| profiles  | profiles/<br>profiles/:id/   | yes (signals) | yes      | yes    | no     | no                       | name        |
| comments  | comments/<br>comments/:id/   | yes           | yes      | yes    | yes    | post                     | no          |
| likes     | likes/<br>likes/:id/         | yes           | yes      | no     | yes    | no                       | no          |
| posts     | posts/<br>posts/:id/         | yes           | yes      | yes    | yes    | profile                  | title       |

## Tests

### Manual Testing
- Profiles app:
    - Visitor can:
        - View all Profiles but not Create, update or delete any any profiles
    - Authenticated user can:
        - Delete their own profiles

- Posts app:
    - Visitor can:
        - View all posts but not Create, update or delete any posts
    - Authenticated user can:
        - Create posts
        - Edit or delete their own posts
    - Images are being validated to be smaller than 4096pixels in width, height as well as 2MB in size. 
        - File type is also being validates as only images are allowed

- Comments app:
    - Visitor can:
        - View all comments but not Create, update or delete any comments
    - Authenticated user can:
        - Create comments on posts
        - Edit or delete their own comments

- Likes app:
    - Visitor can:
        - View all likes but not Create or delete any likes
    - Authenticated user can:
        - Create likes on posts
        - Delete their own likes

### Bugs
- I had issues with CORS and preflight headers.
    - Solved it by adding following code in settings.py:
        - At the top of the file, import following: 
            - ```from corsheaders.defaults import default_headers, default_methods```
        - Before INSTALLED_APPS, add the following code: 
            - ```CORS_ALLOW_HEADERS = list(default_headers)```
            - ```CORS_ALLOW_METHODS = list(default_methods)```
- I couldn't upload images from the front end to the API and could for the life of me not understand why. I downgraded React, react-bootstrap and react-router-dom and the whole API to older versions just to make sure that it would work. 
    - After two days of debugging I finally found out that I had not returned a value on the function validating the image in pp5_api/posts.serializers.py

## Deployment
- Create env.py file in root folder and add it to .gitignore
- Set the environment variables:
    - CLIENT_ORIGIN
    - CLOUDINARY_URL
    - DATABASE_URL
    - DISABLE_COLLECTSTATIC to '1'
    - SECRET_KEY
- Installed following apps:
    - For sessiontokens during development:
        - dj-rest-auth
            - run `pip install dj-rest-auth` in the terminal
            - added it to installed apps
            - set the projectlevel urls.py to include the app urls
            - migrated the database
    - For ability to register users:
        - dj-rest-auth
            - run `pip install 'dj-rest-auth[with_social]'` in the terminal
            - added it to installed apps
            - Set SITE_ID to '1' in settings.py
            - included the urls in projectlevel urls.py
    - To set up JWT tokens with django-all-auth:
        - djangorestframework-simplejwt
            - run `pip install djangorestframework-simplejwt` in the terminal
            - added it to installed apps
            - added the necesarry configs to settings.py
            - migrated database again
    - For handling database connection:
        - dj-database-url
            - run `pip install dj-database-url` in the terminal
        - psycopg2
            - run `pip install psycopg2` in the terminal
    - To configure CORS headers:
        - django-cors-headers
            - run `pip install django-cors-headers` in the terminal
            - made the necesarry configs to settings.py
            - set ALLOWED_ORIGINS
- Set ALLOWED_HOSTS variable
- Set default renderer to JSON
- Created Procfile with web command as well as release commands
- Generated requirements.txt
- Deployed to Heroku

The Live project API link can be found [here](https://pp5-api.herokuapp.com/)
