### Book_A_Meal
[![Build Status](https://travis-ci.org/kwanj-k/Book_A_Meal.svg?branch=develop)](https://travis-ci.org/kwanj-k/Book_A_Meal) [![Coverage Status](https://coveralls.io/repos/github/kwanj-k/Book_A_Meal/badge.svg?branch=api-v2)](https://coveralls.io/github/kwanj-k/Book_A_Meal?branch=api-v2)


This is an Application that allows customers to make food orders and helps the food vendor know what the customers want to eat.

The application is managed using PivotalTracker board, [click here](https://www.pivotaltracker.com/n/projects/2165483) to see.

To see the API docs [click here](https://bookameal6.docs.apiary.io/#)

To see the API docs on heroku[click here](https://bam-v2.herokuapp.com/)
### Getting Started 

Clone the repository: 

```git clone https://github.com/kwanj-k/Book_A_Meal.git```

Navigate to the cloned repo. 
Pull the branch with the API.

```git pull origin api-v2```

### Prerequisites

```
1. python3 & a virtualenv
2. Flask
3. Postman
```

### Installing
Create a virtualenv and activate it.. [Refer here](https://docs.python.org/3/tutorial/venv.html)

Also make sure to setup postgres on your local machine.[Refer here](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-postgresql-on-ubuntu-16-04)

If on windows,[Refer here](https://www.postgresql.org/download/windows/)

- Install the project dependencies:
> $ pip install -r requirements.txt
- On your terminal with the env still activated.Run:

> $ export FLASK_APP="manage.py"

> $ export SECRET="some-very-long-string-of-random-things"

> $ export FLASK_DEBUG=1

### Running Tests
To run tests,you will need to configure a database to run the tests on.

Run the following on your terminal.

> $ createdb tetst_db

> $ export APP_SETTINGS="testing"

> $ python manage.py db init

> $ python manage.py db migrate

> $ python manage.py db upgrade

> $ nosetests --with-coverage --cover-package app

This should run all the tests and give test coverage.  

### Nosetests

The above tests are meant to test the functionality of all the endpoints and verify they are working.

### Testing API EndPoints
We will need different configuration to test the endpoints.
On your terminal with the enviroment activated.Run:

> $ export APP_SETTINGS="development"

> $ createdb book_a_meal

> $ export DevDB_URL="postgresql://@localhost/book_a_meal"

> $ python manage.py db init

> $ python manage.py db migrate

> $ python manage.py db upgrade

> $ flask run

``` flask run ``` Should should start your local development server,from there you good to go.

FireUp PostMan and test the different API endpoints from the table below. 

Ensure the URLs are prefixed with ``` /api/v2 ```


| EndPoint                       | Functionality                           | Restriction                |
| -------------------------------|:---------------------------------------:|:--------------------------:|
| POST     /auth/signup          | Register a user                         | None                       |
| POST     /auth/login           | Login a user                            | None                       |
| GET      /meals/               | Get all the meal options                | Admin users only           |
| GET      /meals/Id/            | Get  a meal by id                       | Admin users only           |
| POST     /meals/               | Add a meal option                       | Admin users only           |
| PUT      /meals/Id/            | Update the information of a meal option | Admin users only           |
| DELETE   /meals/Id/            | Remove a meal option                    | Admin users only           |
| GET      /menus/               | Get all the meal items options          | All users                  |
| GET      /menus/Id/            | Get  a meal item by id                  | All users                  |
| POST     /menus/               | Setup the mealitem                      | Admin users only           |
| PUT      /menus/Id/            | Update the information of a meal item   | Admin users only           |
| DELETE   /menus/Id/            | Remove a meal item                      | Admin users only           |
| GET      /orders/              | Get all the orders                      | Admin users only           |
| GET      /orders/Id/           | Get  an order by id                     | Admin users only           |
| POST     /orders/              | Create an order                         | All users                  |
| PUT      /orders/Id/           | Update the information of an order      | All users                  |
| DELETE   /orders/Id/           | Remove an order                         | All users                  |

## Authors

* **Kelvin Mwangi** - *Initial work* - [kwanj-k](https://github.com/kwanj-k)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to every Andela LearningFacilitator and bootcamper for the aid.
#### Contribution
Fork the repo, create a PR to this repository's develop.
