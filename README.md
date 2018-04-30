### Book_A_Meal
[![Build Status](https://travis-ci.org/kwanj-k/Book_A_Meal.svg?branch=develop)](https://travis-ci.org/kwanj-k/Book_A_Meal)

This is an Application that allows customers to make food orders and helps the food vendor know what the customers want to eat.

The application is managed using PivotalTracker board, [click here](https://www.pivotaltracker.com/n/projects/2165483) to see.

To see the API docs [click here](https://app.apiary.io/bookameal6/)
### Getting Started 

Clone the repository: 

```git clone https://github.com/kwanj-k/Book_A_Meal.git```

Navigate to the cloned repo. 
Pull the branch with the API.

```git pull origin api-v1```

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
- On your terminal with the env still activated.Run:
> $ export FLASK_APP="run.py"

> $ export APP_SETTINGS="development"

### Running Tests

After setting up the above. Run:

``` nosetests --with-coverage --cover-package app```

This should run all the tests and give test coverage.  

### Testing API EndPoints
Start the development server with:
> $ python run.py

FireUp PostMan and test the different API endpoints from the table below. 

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

* **Kelvin Mwangi** - *Initial work* - [kwanj-k](https://github.com/kwanj-k)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to every Andela LearningFacilitator and bootcamper for the aid.
#### Contribution
Fork the repo, create a PR to this repository's develop.
