# LITRevu Django Project

## Description

LITReview is a Django application that allows users to request and publish reviews for books or articles by creating tickets. Users can follow others, view reviews and tickets from followed users in a personalized feed, and interact with them through reviews.

## Features

### Non-logged-in user
- Sign up
- Log in

### Logged-in user
- View a feed with tickets and reviews from followed users, ordered in reverse chronological order
- Create new tickets to request reviews
- Write a review in response to an existing ticket
- Create a ticket and a review simultaneously
- Edit or delete your own tickets and reviews
- Follow or unfollow other users
- View the list of followed users

## Installation:

1. Open the terminal.

2. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/FabL-B/OC_Projet9
    cd OC_Projet9
    ```

3. Create and activate the virtual environment:

    ```bash
    python -m venv env
    source env/bin/activate (for Linux and Mac)
    env\Scripts\activate (for Windows)
    ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup:

1. Apply migrations to create the database tables:

    ```bash
    python manage.py migrate
    ```

2. Populate the database with test data using fixtures:

    ```bash
    python manage.py loaddata fixtures/users_data_test.json
    python manage.py loaddata fixtures/tickets_data_test.json
    python manage.py loaddata fixtures/reviews_data_test.json
    ```

3. The superuser for accessing the Django admin interface is:
- Username: ```admin```
- Password: ```mdpadmin```

4. Test users are available for logging in and testing the application's features:
- Usernames: ```user1```, ```user2```, ```user3```, ```user4```, ```user5```
- Password: ```mdpusertest``` (same for all test users)

## Running the application:

1. Start Django’s development server:

    ```bash
    python manage.py runserver
    ```

2. Open your browser and navigate to:

    ```bash
    http://127.0.0.1:8000
    ```

## Accessing the Admin Interface:

To access the admin interface, navigate to:

```bash
http://127.0.0.1:8000/admin
```

Log in using the admin credentials provided above.
