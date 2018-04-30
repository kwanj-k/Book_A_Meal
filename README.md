### Book_A_Meal_The_App
[![Build Status](https://travis-ci.org/kwanj-k/Book_A_Meal.svg?branch=develop)](https://travis-ci.org/kwanj-k/Book_A_Meal)

This is an Application that allows customers to make food orders and helps the food vendor know what the customers want to eat.

This repo contains a UI and a Flask API for the book_a_meal app.
The application is managed using PivotalTracker board, [click here](https://www.pivotaltracker.com/n/projects/2165483) to see.
### Getting Started 

Clone the repository: 

```git clone https://github.com/kwanj-k/Book_A_Meal.git```

Navigate to the cloned repo. 

### Prerequisites

```
1. python3 & a virtualenv
2. Flask
3. Postman
```

### Installing
Create a virtualenv and activate it. [Refer here](https://docs.python.org/3/tutorial/venv.html)
- Install the project dependencies:
> $ pip install -r requirements.txt

### Running Tests

After setting up the above. Run:

``` nosetests -v ``` To make sure all the tests are running and passing.

### Breakdown into end to end tests
The nosetests tests the different functionality of the API endpoints and makes sure they all working.

### Deployment
After setting up the above and making sure all the tests are passing. Run:

``` python run.py ```

Test the endpoints registered on `app/__init__.py` on Postman/curl on the port the app is running on. 

### API EndPoints
Ensure the URLs are prefixed with ``` /api/v1 ```


| EndPoint                       | Functionality                           | 
| -------------------------------|:---------------------------------------:|
| POST /auth/signup              | Register a user                         | 
| POST /auth/login               | Login a user                            |
| GET /meals/                    | Get all the meal options                |
| POST /meals/                   | Add a meal option                       | 
| PUT /meals/<mealId>            | Update the information of a meal option |
| DELETE /meals/<mealId>         | Remove a meal option                    |
| POST  /menu/                   | Setup the menu for the day              | 
| GET /menu/                     | Get the menu for the day                |
| POST  /orders                  | Select the meal and menu item           |
| PUT /orders/orderId            | Modify an order                         | 
| GET  /orders                   | Get all the orders                      |



# Book_A_Meal_UI
This is the user interface made simply with HTML and CSS and hosted on github pages.

It is made up of different static pages to showcase the different funtionalities book_a_meal app offers. 

### Testing the UI
After setting up as described up above on the development section. OPen:

```index.html``` with chrome or any other browser.

View the different pages as displayed on the navigation.

### GitHubPages
To see the static site [click here](https://kwanj-k.github.io/Book_A_Meal/)

>An image of the Landing Page.

![alt text](https://raw.githubusercontent.com/kwanj-k/Book_A_Meal/gh-pages/UI/images/b-a-m.jpg)


#### Contribution
Fork the repo, create a PR to this repository's develop.