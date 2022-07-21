# PP5 API

## Project Description
This unnamed project (for now) is a content sharing platform that connects people from all four corners of the earth to share knowledge in what they are passionate about. The platform is powered by a Django REST API and React.<br>This Readme contains only to the back end part and the front end part can be found [here](https://google.com/)

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
- 