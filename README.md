
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
- used JWT authentication


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


![Screenshot (83)](https://github.com/samayunPathan/Corporate-Asset-Tracker-Django/assets/93588462/200fa434-d791-42b8-8293-4508673d3f9c)
![Screenshot (84)](https://github.com/samayunPathan/Corporate-Asset-Tracker-Django/assets/93588462/606bdfe9-cd3e-4180-a601-42b03f34440c)

![Screenshot (87)](https://github.com/samayunPathan/Corporate-Asset-Tracker-Django/assets/93588462/b542c94d-76ae-412b-85ab-bd76c752e003)


![Screenshot (88)](https://github.com/samayunPathan/Corporate-Asset-Tracker-Django/assets/93588462/32fb2bfc-8681-4137-a3c5-cf512bf64ad6)

![Screenshot (90)](https://github.com/samayunPathan/Corporate-Asset-Tracker-Django/assets/93588462/f87e0abb-400e-4349-8c4c-adf76e3e2d45)



![Screenshot (89)](https://github.com/samayunPathan/Corporate-Asset-Tracker-Django/assets/93588462/52c3542b-45be-4836-a390-b0cc97eb4a90)







