### Book_A_Meal_The_App
[![Build Status](https://travis-ci.org/kwanj-k/Book_A_Meal.svg?branch=develop)](https://travis-ci.org/kwanj-k/Book_A_Meal)
### My Github repo

```https://github.com/kwanj-k```

#### Description
This is an Application that allows customers to make food orders and helps the food vendor know what the customers want to eat.

This repo contains a UI and a Flask API for the book_a_meal app.

The application is managed using PivotalTracker board, [click here](https://www.pivotaltracker.com/n/projects/2165483) to see.

### Development

Clone the repository: 

```git clone https://github.com/kwanj-k/Book_A_Meal.git```

Navigate to the cloned repo. 

Ensure you have the following:

```
1. python3 & a virtualenv
2. Flask
3. Postman
```

Create a virtualenv and activate it. [Refer here](https://docs.python.org/3/tutorial/venv.html)

### Dependencies
- Install the project dependencies:
> $ pip install -r requirements.txt

### Testing the API

After setting up the above. Run:

```python run.py```

Test the endpoints registered on `app/__init__.py` on Postman/curl on the port the app is running on. 

The API endpoints are:
```
1.'/api/v1/meals'         {create and get meals}
2.'/api/v1/meals/id'      {delete meal by id and a update meal}
3.'/api/v1/menus'         {create a menu item and get menus}
4.'/api/v1/orders'        {get orders and create orders}
5.'/api/v1/orders/id'     {delete order and update order by id}
6.'/api/v1/auth/register' {register a user}
7.'/api/v1/auth/login'    {User login}


```


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

<!-- >An image of the SignUp Page on a tablet.

![alt text](https://raw.githubusercontent.com/kwanj-k/Book_A_Meal/master/UI/images/signup.png)

>An image of the detailed orders Page.

![alt text](https://raw.githubusercontent.com/kwanj-k/Book_A_Meal/mater/UI/images/detail.png) -->

#### Contribution
Fork the repo, create a PR to this repository's develop.