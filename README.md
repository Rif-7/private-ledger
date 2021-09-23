# Private Ledger

This is my submission for CS50 Web's final project a simple private ledger. Web app that let's you keep track of all your transactions.
This project is neither a social network nor an e-commerce site. This web app is a private ledger in which each user is able to store his transactions and perform few actions on it a more detailed information about the website is provided below on it's design and working.

#### Features

1. Create Account.
2. Add a new transaction.
3. View all your transactions.
4. Sort your transactions based on price, date and cateogorie.
5. View a detailed stat about your transactions based on the cateogories.

#### Files & Directories

- `Main Directory`

  - `app` - Main application directory.

      - `models.py` - ORM auth model. Contains the code for the ledger and categorie models.
      - `urls.py` - Contains all url paths like login, register, recieve datal and sent data.
      - `views.py` - Contains all view functions for authentication, sending data, and adding   data.

    - `templates` - Contains the html files.
        - `index.html` - Contains the html code for the index page.
        - `login_layout` - Contains the layout code for both the register and login files.
        - `login.html` - Contains the code for the login page.
        - `register.html` - Contains the code for the register page.

    - `static` - Contains the CSS stylesheet and JavaScript file.
        - `app.js` - JavaScript file with client side code.
        - `styles.css` - Main stylesheet for the app.
      
  - `ledger` - Containes settings and main url file.
    
  - `gitignore` - Ignored files for git.


#### Justification
Why is this project distint from the previous projects:
1. This is not a social network site since other users can only see thier information.
2. Uses a much more complex models
3. Has an advanced Sort function where users can sort based on the time period they added transactions
4. Completely mobile responsive

## Distinctiveness and Complexity
This project is neither a social network or an e-commerce site. This web app is a private ledger in which each user is able to store his transactions and perform few actions on it a more detailed information about the website is provided below on it's design and working.

#### More about the project
By creating an account the user is redirected to his home page where he can view all his transactions. For each transaction the user can store 5 information about it which will be loaded in a table. The user is able to specify a Categorie for the transaction eg: Food, Health, Educaction etc a short Description, the Amount of the transaction, To whom the transaction was made and finally the Date and Time of the transaction which will be added by the web app, the user does'nt have to specify the date.

The navbar consists of 5 options which are Home, Logout, New Transaction, Stats and Sort. The user can click the Home button to view all of his transactions, Logout to logout, New Transaction to create a new transaction, Stats to view the statistics of his transactions and Sort to sort his transactions.

On clicking the New Transactions button the user will be presented with a form where he would have to provide the neccessary information for his transaction. The Catogorie field in the form would allow the user to pick a categorie from the list of categories he used for his previous transactions or he could use a new catogorie for the transactions. After filling the rest of the fields the user can click the submit button.

The Stats button will load a table with each categorie ordered by highest to lowest spent on and how much the user spent on each categorie

The Sort button will load a popup box with a form in which you can specify categories seperated by commas, the min and max amount and the time period in which the transactions took place.


#### How to run

- pip install django
- cd ledger
- python manage.py makemigrations
- python manage.py migrate

- python manage.py runserver
