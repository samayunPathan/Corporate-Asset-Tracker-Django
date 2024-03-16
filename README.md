
# Corporate Asset Tracker

#### App name: asset_tracker
#### Project Description:
- To track corporate assets such as phones, tablets, laptops and other gears handed out to employees.
- The application might be used by several companies
- Each company might add all or some of its employees
- Each company and its staff might delegate one or more devices to employees for a certain period of time
- Each company should be able to see when a Device was checked out and returned
- Each device should have a log of what condition it was handed out and returned


## Features 

- Created a new virtual environment for this project and installed the required packages, which i have shared in requirements.txt file.
- used Django Rest Framework for creating the API's.
- used SQLITE3 database for this project.
- used Django Serializer for creating the serializers.
- used Swagger UI to create interactive API documentation  


## Getting Started

Installation: Clone this repository and Install the required dependencies using:

create virtual environment
``` bash
  py -m venv (virtual_environment_name)
```
To activate virtual environment
``` bash
  source (virtual_environment_name)/scripts/activate
  ```
Install required dependencies
```bash
  pip install -r requirements.txt
```
Database Setup: Run database migrations 
```bash
  python manage.py migrate
```
Create Superuser: Create a superuser to access the admin panel:
``` bash
python manage.py createsuperuser
```
Run Development Server: Start the development server:
```bash
python manage.py runserver
```
Admin Panel: Access the admin panel at http://127.0.0.1:8000/admin/ to add companies, employees, devices, and manage device logs.

API Endpoints: Use the provided API endpoints to manage assets programmatically. Refer to the API documentation for more details.

Interactive API documentation with Swagger UI 

http://127.0.0.1:8000/swagger/



## API Documentation

#### Get all items


API Documentation
The API provides the following endpoints:

- /company/: get list and create companies.
- /company/<id>: Edit/update and delete companies.

- /employee/: get List and create employees.
- /employee/<id>: Edit/update and delete employees.

- /asset/: get list and create asset
- /asset/<id>: Edit/update and delete asset

- /assetlog/: get and post asset checkout_date ,return_date ,checkout_condition ,return_condition ,asset delegate employee

- /assetlog/<id>: Edit/update and delete asset checkout_date ,return_date ,checkout_condition ,return_condition ,asset delegate employee

### OR 
    Interactive API documentation with Swagger UI 

    http://127.0.0.1:8000/swagger/






## Screenshots 




