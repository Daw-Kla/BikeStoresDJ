# [Bike Stres Data Base control system]

In this project I am using a open-source **Django Dashboard** generated by `AppSeed` op top of an iconic design. For newcomers, **[SB Admin](https://appseed.us/product/sb-admin/django/)** is one of the best open-source admin dashboard & control panel theme. Built on top of Bootstrap, `SB Admin` provides a range of responsive, reusable, and commonly used components. 

<br />

<br />

- `Up-to-date dependencies`
- Database: [BikeStores](https://www.sqlservertutorial.net/sql-server-sample-database/)
- UI-Ready app, Django Native ORM
- `Session-Based authentication`, Forms validation

<br />

## ✨ How to use it

> Download the code 

```bash
$ # Get the code
$ git clone https://github.com/appseed-projects/c259e2ca-c6fd-493d-b4d7-6da9365ef441.git
$ cd c259e2ca-c6fd-493d-b4d7-6da9365ef441
```

> Download a [DB file:](https://www.sqlservertutorial.net/sql-server-sample-database/)
> Install DB in MS SQL Server

```bash
$ # change schema once in MS SQL Server using this code fro each table witch specified schema:
$ ALTER SCHEMA dbo TRANSFER [production].[TableName] 
$ ALTER SCHEMA dbo TRANSFER [sales].[TableName]
```

### 👉 Set Up for `Windows` 

> Install modules via `VENV` (windows) 

```
$ virtualenv env
$ .\env\Scripts\activate
$ pip3 install -r requirements.txt
```

<br />

> Set Up Database

```bash
$ python manage.py makemigrations
$ python manage.py migrate
```

<br />

> Start the app

```bash
$ python manage.py runserver
```

At this point, the app runs at `http://127.0.0.1:8000/`. 

<br />

### 👉 Create Users

By default, the app redirects guest users to authenticate. In order to access the private pages, follow this set up: 

- Start the app via `python manage.py runserver`
- Access the `registration` page and create a new user:
  - `http://127.0.0.1:8000/register/`
- Access the `sign in` page and authenticate
  - `http://127.0.0.1:8000/login/`

<br />


## ✨ Code-base structure

The project is coded using a simple and intuitive structure presented below:

```bash
< PROJECT ROOT >
   |
   |-- core/                               # Implements app configuration
   |    |-- settings.py                    # Defines Global Settings
   |    |-- wsgi.py                        # Start the app in production
   |    |-- urls.py                        # Define URLs served by all apps/nodes
   |
   |-- apps/
   |    |
   |    |-- home/                          # A simple app that serve HTML files
   |    |    |-- views.py                  # Serve HTML pages for authenticated users
   |    |    |-- urls.py                   # Define some super simple routes  
   |    |-- production/                    # App based on a data base schema
   |         |   
   |         |-- admin.py
   |         |-- config.py
   |         |-- models.py
   |         |-- tests.py
   |         |-- urls.py
   |         |-- views.py
   |    |-- sales/                        # App based on a data base schema
   |         |   
   |         |-- admin.py
   |         |-- config.py
   |         |-- models.py
   |         |-- tests.py
   |         |-- urls.py
   |         |-- views.py
   |    |-- authentication/                # Handles auth routes (login and register)
   |    |    |-- urls.py                   # Define authentication routes  
   |    |    |-- views.py                  # Handles login and registration  
   |    |    |-- forms.py                  # Define auth forms (login and register) 
   |    |
   |    |-- static/
   |    |    |-- <css, JS, images>         # CSS files, Javascripts files
   |    |
   |    |-- templates/                     # Templates used to render pages
   |         |-- includes/                 # HTML chunks and components
   |         |    |-- navigation.html      # Top menu component
   |         |    |-- sidebar.html         # Sidebar component
   |         |    |-- footer.html          # App Footer
   |         |    |-- scripts.html         # Scripts common to all pages
   |         |
   |         |-- layouts/                   # Master pages
   |         |    |-- base-fullscreen.html  # Used by Authentication pages
   |         |    |-- base.html             # Used by common pages
   |         |
   |         |-- accounts/                  # Authentication pages
   |         |    |-- login.html            # Login page
   |         |    |-- register.html         # Register page
   |         |
   |         |-- home/                      # UI Kit Pages
   |              |-- index.html            # Index page
   |              |-- 404-page.html         # 404 page
   |              |-- *.html                # All other pages
   |
   |-- requirements.txt                     # Development modules - SQLite storage
   |
   |-- .env                                 # Inject Configuration via Environment
   |-- manage.py                            # Start the app - Django default start script
   |
   |-- ************************************************************************
```

<br />


