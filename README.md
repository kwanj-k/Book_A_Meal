### Book_A_Meal
[![Build Status](https://travis-ci.org/kwanj-k/Book_A_Meal.svg?branch=develop)](https://travis-ci.org/kwanj-k/Book_A_Meal)

This is an Application that allows customers to make food orders and helps the food vendor know what the customers want to eat.

This repo contains a UI and a Flask API for the book_a_meal app.
The application is managed using PivotalTracker board, [click here](https://www.pivotaltracker.com/n/projects/2165483) to see.

### Prerequisites

```
1. python3 & a virtualenv
2. Flask
3. Postman
```

### Getting Started 

Clone the repository: 

```git clone https://github.com/kwanj-k/Book_A_Meal.git```

Navigate to the cloned repo. 
### Installing
Create a virtualenv and activate it in the cloned repo. [Refer here](https://docs.python.org/3/tutorial/venv.html)
- Install the project dependencies:
> $ pip install -r requirements.txt


### Running Tests
- On the terminal with the enviroment activated,run the following commands inorder they appear:
> $ export FLASK_APP="app.py
> $ export APP_SETTINGS="development"
> $ nosetests --with-coverage --cover-package app 

### Test API EndPoints
- After running the tests above and ensuring the all pass.Run:
> $ python run.py
These will start the development server.Use Postman to test the different endpoints.
Ensure the URLs are prefixed with ``` /api/v1 ```


| EndPoint                       | Functionality                           | 
| -------------------------------|:---------------------------------------:|
| POST     /auth/signup          | Register a user                         | 
| POST     /auth/login           | Login a user                            |
| GET      /meals/               | Get all the meal options                |
| POST     /meals/               | Add a meal option                       | 
| PUT      /meals/<mealId>       | Update the information of a meal option |
| DELETE   /meals/<mealId>       | Remove a meal option                    |
| POST     /menu/                | Setup the menu for the day              | 
| GET      /menu/                | Get the menu for the day                |
| POST     /orders               | Select the meal and menu item           |
| PUT      /orders/orderId       | Modify an order                         | 
| GET      /orders               | Get all the orders                      |

#### Contribution
Fork the repo, create a PR to this repository's develop.

## Authors

* **Kelvin Mwang** - *Initial work* - [kwanj-k](https://github.com/kwanj-k)


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to every Andela bootcamper and facilitators for the help with the project.
