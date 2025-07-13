# Sarva Suvidha KPA Backend Assignment - API Development

##  Developer: Ranjeet Yadav

##  Project Overview

This project is a backend API implementation task based on the provided Postman Collection and SwaggerHub documentation for [KPA Form Data](https://app.swaggerhub.com/apis/sarvasuvidhaen/kpa-form_data/1.0.0).  
Two APIs were implemented using Django REST Framework and connected to a PostgreSQL database.



##  Technologies Used

- Python 3.12+
- Django 5.1+
- Django REST Framework
- PostgreSQL
- Postman (for API testing)
- Swagger (for API documentation reference)


## 🔧 Setup Instructions

1. Clone the Repository
   
   git clone https://github.com/ranjeet3345/sarva_suvidha_kpa_backend/
   
   cd sarva_suvidha_kpa_backend/   



2.Create and Activate Virtual Environment

python3 -m venv env
source env/bin/activate

3.Install Dependencies

pip install -r requirements.txt


4. Database Configuration

Update the following in your kpa_backend/settings.py file:

a) DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'kpa_db',
        'USER': 'postgres',
        'PASSWORD': 'yourpassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

IMPORTANT:-Also make sure you configure with postgreSQL in local postgres correctly otherwise it will give error.

Otherwise you change your database to db.sqlite3:

b) DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



5.) Run Migrations

python manage.py makemigrations


python manage.py migrate


6) Run the server

python manage.py runserver


7) Implemented API Views:

    POST /api/wheel/submit/: Accepts wheel specification data, validates it using WheelSpecificationSerializer, and saves it to the database. Returns a success message with 201 Created or validation errors with 400 Bad Request.

    GET /api/wheel/specifications/: Fetches all submitted wheel specifications. Supports optional filtering by formNumber, submittedBy, and submittedDate. Returns filtered results in a structured JSON format.
