# Cocoon Creations NewsFeeds API

A backend system for a mobile app that displays a list of news articles.
## Database structure

SQLITE3



## Running the server

From within the `root directory` directory first ensure you are working using your created virtual environment.

create a `.env` file and populate it with the credentials sent in the mail.

Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate

```

To run the server, execute:

```bash
python manage.py runserver
```

## API Reference

## Getting Started

### Installing Dependencies

#### Python 3.8

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

I recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by navigating to the `root directory` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages within the `requirements.txt` file.


### Error Handling
Errors are returned as JSON objects with "success" set to False, "error" set to the error's number and a "message" describing the error

The API may return these error types when requests fail:
- 400: Bad Request
- 403: Forbidden
- 404: Resource Not Found
- 422: Request can not be processed
- 500: Internal Server Error

### Endpoints

```
Note: for any request other than the GET ARTICLE REQUEST, requires Authetication

```
#####  '/admin'
    This endpoint is for an admin panel that can be used to store and update data.

##### GET  '/authors'
    This endpoint fetches all the authors in the database and displays them as json.


##### POST '/authors'
    This endpoint will create a new author in the database based on the json that is in the body of the request.

##### PATCH  '/authors/<int:pk>'
    This endpoint will modify the author that corresponds to the primary key that is passed into the url based on the json that is passed into the body of the request.


##### DELETE  ''/authors/<int:pk>'
    This endpoint will delete the author that corresponds to the primary key that is passed into the url.

##### GET  '/categories'
    This endpoint fetches all the categories in the database and displays them as json.


##### POST '/categories'
    This endpoint will create a new category in the database based on the json that is in the body of the request.

##### PATCH  '/categories/<int:pk>'
    This endpoint will modify the category that corresponds to the primary key that is passed into the url based on the json that is passed into the body of the request.


##### DELETE  '/categories/<int:pk>'
    This endpoint will delete the category that corresponds to the primary key that is passed into the url.

##### GET  '/articles'
    This endpoint fetches all the articles in the database and displays them as json.


##### POST '/articles'
    This endpoint will create a new article in the database based on the json that is in the body of the request.

##### PATCH  '/articles/<int:pk>'
    This endpoint will modify the article that corresponds to the primary key that is passed into the url based on the json that is passed into the body of the request.


##### DELETE  '/articles/<int:pk>'
    This endpoint will delete the article that corresponds to the primary key that is passed into the url.

##### GET  '/readers'
    This endpoint fetches all the readers in the database and displays them as json.


##### POST '/readers'
    This endpoint will create a new reader in the database based on the json that is in the body of the request.

##### PATCH  '/readers/<int:pk>'
    This endpoint will modify the reader that corresponds to the primary key that is passed into the url based on the json that is passed into the body of the request.


##### DELETE  '/readers/<int:pk>'
    This endpoint will delete the reader that corresponds to the primary key that is passed into the url.

##### GET  '/readers/<int:pk>/bookmarks'
    This endpoint fetches all bookmarks for a particular reader in the database and displays them as json.


##### POST '/readers/<int:pk>/bookmarks'
    This endpoint will create a particular bookmark for a particular reader resquest in the database based on the json that is in the body of the request.

##### DELETE  '/readers/<int:pk>/bookmarks/<int:pk>'
    This endpoint will delete the particular bookmark for a particular reader that corresponds to the primary keys passed into the url.

