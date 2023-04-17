Django Astrology App
This is a web application built using Django, which takes the user's birthdate as input and outputs their astrology type along with personality traits description and an image.

The project consists of three main pages: home, result, and detail.

The home page is the landing page of the app, where users can enter their name, birthdate, and gender information.
The result page processes the user's input and returns the corresponding astrology type, description, and image URL.
The detail page displays the details of a specific astrology sign including its name, description, and image.
The astrology types are calculated using the user's birthdate and a function in the utils.py module. The personality traits description and image URL for each astrology type are stored in a dictionary in the same module.

The project also includes two models: User and Sign. The User model defines the database blueprint for the user's input, while the Sign model defines the blueprint for each astrology sign.

Key aspects of this project include:

Efficient use of Django to build a functional web application with multiple pages and database models.
Use of object-relational mapping (ORM) to handle database operations.
Use of Python datetime module to manipulate dates and extract birth month and day from the user's input.
Use of dictionary to store astrology types' descriptions and image URLs.
Implementation of choices list for gender input field in the User model.
To run this project, you will need to have Django installed. Once installed, navigate to the project directory in your terminal and run the command python manage.py runserver. Then, open your web browser and go to http://localhost:8000/ to access the app.