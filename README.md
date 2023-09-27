# FULL-STACK-project-in-python

["https://decimal-oblong-gallinule.anvil.app"]demo

* in this project we have created the server using python 

* we have used anvil for the frontend 

*for the database we ahve used pgsql

###### same project can be done using django 
step 1:
install python from its original documentation 
["link"]("https://www.python.org/")

step2:
create a new folder and set virtualenv 
* mkdir folder_name
* open cmd with that folder
* enter the command
  ```
python -m venv name_of_virtual_env
  ```
step3:activate the venv
```
name_of_virtual_env\Scripts\activate
```
step4:after activating install the django inside it
```
pip install django 
```
if u get the errro like
```
[notice] A new release of pip is available: 23.1.2 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip
```
just upgrade it by giving the following
```
python.exe -m pip install --upgrade pip
```


images from my pc
```

E:\kishore\Django>python -m venv my_env

E:\kishore\Django>my_env\Scripts\activate

(my_env) E:\kishore\Django>pip isntall django
ERROR: unknown command "isntall" - maybe you meant "install"

(my_env) E:\kishore\Django>pip install django
Collecting django
  Using cached Django-4.2.5-py3-none-any.whl (8.0 MB)
Collecting asgiref<4,>=3.6.0 (from django)
  Using cached asgiref-3.7.2-py3-none-any.whl (24 kB)
Collecting sqlparse>=0.3.1 (from django)
  Using cached sqlparse-0.4.4-py3-none-any.whl (41 kB)
Collecting tzdata (from django)
  Using cached tzdata-2023.3-py2.py3-none-any.whl (341 kB)
Installing collected packages: tzdata, sqlparse, asgiref, django
Successfully installed asgiref-3.7.2 django-4.2.5 sqlparse-0.4.4 tzdata-2023.3

[notice] A new release of pip is available: 23.1.2 -> 23.2.1
[notice] To update, run: python.exe -m pip install --upgrade pip

(my_env) E:\kishore\Django> python.exe -m pip install --upgrade pip
Requirement already satisfied: pip in e:\kishore\django\my_env\lib\site-packages (23.1.2)
Collecting pip
  Using cached pip-23.2.1-py3-none-any.whl (2.1 MB)
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 23.1.2
    Uninstalling pip-23.1.2:
      Successfully uninstalled pip-23.1.2
Successfully installed pip-23.2.1

(my_env) E:\kishore\Django>django-admin --version
4.2.5

(my_env) E:\kishore\Django>django-admin startproject first_django

(my_env) E:\kishore\Django>cd firt_django
The system cannot find the path specified.

(my_env) E:\kishore\Django>ls
'ls' is not recognized as an internal or external command,
operable program or batch file.

(my_env) E:\kishore\Django>list
'list' is not recognized as an internal or external command,
operable program or batch file.

(my_env) E:\kishore\Django>cd first_django

(my_env) E:\kishore\Django\first_django>python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
September 27, 2023 - 15:43:15
Django version 4.2.5, using settings 'first_django.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.

Not Found: /p
[27/Sep/2023 15:44:20] "GET /p HTTP/1.1" 404 2086
[27/Sep/2023 15:45:24] "GET / HTTP/1.1" 200 10664
Not Found: /favicon.ico
[27/Sep/2023 15:45:24] "GET /favicon.ico HTTP/1.1" 404 2116

```


