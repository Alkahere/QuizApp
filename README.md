# QuizApp
Quiz Application using Django

# Quiz Platform

Welcome to the Quiz Platform! This web application allows users to take quizzes, track their scores, and improve their knowledge on various topics. This project is built using Django for the backend and HTML/CSS for the frontend.

## Features

- User Authentication
  - Register and login to access quizzes
- Quiz Management
  - Create, update, and delete quizzes
  - Add multiple-choice questions to quizzes
- Quiz Taking
  - Users can take quizzes and see their scores
- User Profile
  - Track total points and quiz history



- Python 3.x
- Django 3.x or later



    git clone https://github.com/Alkahere/QuizApp.git
    cd QuizApp
  


    pip install -r requirements.txt //install dependencies

    python manage.py migrate   //run migrations
  
 python manage.py createsuperuser // create super user

    python manage.py runserver // run the server

    Open your browser and go to `http://127.0.0.1:8000`.

 Project Structure

- `quiz_platform/` - Main project directory
- `quiz/` - App directory containing models, views, and templates for quizzes
- `templates/quiz/` - Directory containing HTML templates
- `static/` - Directory containing static files 
- `requirements.txt` - File listing required Python packages

User Authentication

- Register for an account or login if you already have one.
- Once logged in, you can access and take quizzes.

 Admin Panel

- Access the admin panel at `http://127.0.0.1:8000/admin`.
- Use your superuser credentials to log in.
- Create, update, and delete quizzes and questions.

Taking Quizzes

- Navigate to the quizzes section and select a quiz.
- Answer the multiple-choice questions and submit your answers.
- View your score and correct answers.




