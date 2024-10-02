# Travello - Travel Website
Overview
Travello is a fully functional travel website designed to inspire users to explore new destinations. Built using Python Django and MySQL, this site allows users to learn about various destinations, register an account, and connect with the team for further inquiries. The website features a clean design and an intuitive user interface to ensure a smooth browsing experience.

Features
Home Page: Showcasing popular travel destinations and inspiring content.
About Us: Detailed information about the mission and vision of Travello.
User Authentication: Users can register, log in, and log out securely.
Contact Information: Easy access to customer support with a dedicated call button.
Responsive Design: Optimized for mobile, tablet, and desktop devices.
Database: Powered by MySQL to store user data and other relevant information.
Technologies Used
Backend: Python Django (Django Framework)
Database: MySQL
Frontend: HTML, CSS, Bootstrap
Authentication: Django's built-in user authentication system
Deployment: Deployed locally or on a cloud platform
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-username/travello.git
Navigate into the project directory:

bash
Copy code
cd travello
Create a virtual environment:

bash
Copy code
python -m venv env
Activate the virtual environment:

On Windows:
bash
Copy code
env\Scripts\activate
On Mac/Linux:
bash
Copy code
source env/bin/activate
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Set up the MySQL database:

Create a MySQL database.
Update the settings.py file with your database credentials:
-- python
Copy code
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'your_database_name',
        'USER': 'your_username',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
Run database migrations:

-- bash
Copy code
--python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the website by opening your browser and navigating to http://127.0.0.1:8000.
