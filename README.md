# Blog App

A Blog App where user can create blog posts and interact with the same of others.


## Tech Stack

Django, PostgreSQL, HTML, CSS, JinjaTemplate




## Run Locally
### With Docker
Clone the project

```bash
  git clone https://github.com/irohanrajput/blog_app.git
```

Go to the project directory

```bash
  cd blog_app
```
Run with Docker Compose

```bash
  docker compose up -d
```


### Without Docker

Clone the project

```bash
  git clone https://github.com/irohanrajput/blog_app.git
```

Go to the project directory

```bash
  cd blog_app
```

Create a Virtual Environment

```bash
  python -m venv .venv (or whatever)
```
Install dependencies

```bash
  pip install -r requirements.txt
```
Setup PostgreSQL Database

```bash
   Database Name: dbname
   USER: dbuser
   PASSWORD: dbpassword
```
Manage Migrations

```bash
  python manage.py makemigrations
  python manage.py migrate
```


Start the server

```bash
  python manage.py runserver
```

