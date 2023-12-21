# News-App

Welcome to News-APP! This web application is designed to provide a simple and intuitive interface for getting daily news. Built with Django framework.

## Getting Started

To get started with the News APP, follow these steps:

1. Clone the repository to your local machine.
2. Install the required dependencies.
3. Configure Cloudinary API key in .env.
4. Run the application locally.

## Features

- Getting a real time news from different author.
- Starching news from different category.
- Adding and Managing news from admin side.

## Prerequisites

Before you begin, ensure you have the following installed:

-Python:Download [Python] (https://www.python.org/downloads/release/python-3121/)

## Dependencies

This project relies on the following dependencies:

- Django
- Cloudinary
- django-ckeditor
- beautifulsoup4

## Installation

1. Clone the repository:

```bash
 git clone https://github.com/Shitikyan/News-App
```

2. Navigate to the directory

```bash
cd News-App
```

3. Create Virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

4. Install dependencies

```bash
 pip install -r requirements.txt
```

5. Configure environment variables

- goto .env.example and copy the variable by creating .env file

6. Make migration

```bash
python manage.py makemigrations
python manage.py migrate
```

7. Run the project

```bash
python manage.py runserver
```

8. Open [http://localhost:8000](http://localhost:8000) with your browser to see the result.

## Accessing admin side

## Creating new admins

You can use cli or the Gui to create new admin

```bash
 python manage.py createsuperuser
```

Default admin email:password
admin@gmail.com:12345678qwer@

## Authors

- **Shitikyan Hovhannes**

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
