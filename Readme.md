## Phone Book

A Simple Django web application.  

##### Features:
* Login / Registration
* Contacts list view
* Individual contact view
* Adding new contact
* Editing contact
* Deleting contact

### Setup
Clone the project
```
$ git clone https://github.com/arbaishev/phonebook.git
$ cd phonebook
```

Create & activate virtual environment
```
$ python3 -m venv phonebook
$ source phonebook/Scripts/activate (for Linux)
  * phonebook\Scripts\activate (for Windows)
```

Install the project dependencies  
`$ pip install -r requirements.txt`


### Running Locally

1. Duplicate `addressbook\settings\local_settings_example.py` and save as `local.py`
2. Enter your secret key & database settings in `local.py`  
(you can obtain a secret key from [MiniWebTool](https://miniwebtool.com/django-secret-key-generator/ "MiniWebTool"))
3. `$ python manage.py migrate`
4. `$ python manage.py createsuperuser`
5. `$ python manage.py runserver`
