# Private Ledger

This is my submission for CS50 Web's final project a simple private ledger. Web app that let's you keep track of all your transactions.

## Distinctiveness and Complexity
This project is neither a social network or an e-commerce site. This web app is a private ledger in which each user is able to store his transactions and perform few actions on it a more detailed information about the website is provided below on it's design and working.

## About
By creating an account the user is redirected to his home page where he can view all his transactions. For each transaction the user can store 5 information about it which will be loaded in a table. The user is able to specify a Categorie for the transaction eg: Food, Health, Educaction etc a short Description, the Amount of the transaction, To whom the transaction was made and finally the Date and Time of the transaction which will be added by the web app, the user does'nt have to specify the date.

The navbar consists of 5 options which are Home, Logout, New Transaction, Stats and Sort. The user can click the Home button to view all of his transactions, Logout to logout, New Transaction to create a new transaction, Stats to view the statistics of his transactions and Sort to sort his transactions.

On clicking the New Transactions button the user will be presented with a form where he would have to provide the neccessary information for his transaction. The Catogorie field in the form would allow the user to pick a categorie from the list of categories he used for his previous transactions or he could use a new catogorie for the transactions. After filling the rest of the fields the user can click the submit button.

The Stats button will load a table with each categorie ordered by highest to lowest spent on and how much the user spent on each categorie

The Sort button will load a popup box with a form in which you can specify categories seperated by commas, the min and max amount and the time period in which the transactions took place.

## Back-end
The web app uses Python's Django framework in the back-end. The file *ledger/views.py* contains the the views for each routes in the webapp, *ledger/urls.py* contains all the routes and the view related to it. *ledger/models.py* contains all the information about how the web app stores it's data. As database it uses sqlite3 with django models

## Front-end
The web app uses JavaScript in the front-end the file *ledger/static/app/app.js* contains the code for the front-end. The app uses JavaScript to add new transactions and to load the transactions from the server to the user. The files in *ledger/templates/app/* contains all the html templates for the web app. *ledger/static/app/styles.css* contains the all the styling data. The app also uses several models from Bootstrap for styling.


## How to run

This project uses Python's Django framework and Datetime module which comes as a pre-installed library

> pip install django
> cd ledger
> python manage.py makemigrations
> python manage.py migrate

> python manage.py runserver
