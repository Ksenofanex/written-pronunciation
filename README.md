# Written Pronunciation

> [!CAUTION]
> This project is no longer maintained.

***

An English written pronunciation site for Turkish hard of hearing and deaf people who can't listen to words' verbal pronunciation.

![Project Demo GIF](/images/written-pronunciation-demo.gif)
![Word Detail Light Mode](/images/word-detail-page-light-mode.png)

***

## Features

- Modern and aesthetic design with dark & light mode
- User authentication & authorization
- Create, Read, Update and Delete functionality
- Pagination
- Searching
- API authentication & authorization
- API CRUD functionality
- API documentation
- Thorough and elegant tests

# Installation

## Clone the project

Depending on the choice of yours, you can clone the project in various ways. Either via IDE, Git Desktop or Git commands.

Whatever the case, make sure Git is installed and after cloning the project, you are at the same working directory with the project.

- Look below for cloning the project via bash:

```bash
$ git clone https://github.com/Ksenofanex/written-pronunciation.git

$ cd written-pronunciation

$ pwd
/written-pronunciation
```

## Environment Variables

Before installing the project, you need a proper `.env` file. The project's [settings.py](written_pronunciation/settings.py) module is depending on these variables.

The project has a fictional [env file](.env.example) for educational purposes. You can either manually create a `.env` file or enter the command below to the bash/terminal to clone a proper `.env` file:

```bash
$ cp .env.example .env
```

An example configuration for the `.env` file:

```
DEBUG=True
SECRET_KEY=itdb4-_wc!=*hgl3)h@v$#jy7bxingn(n+qklsdso%9yq&c5)!
```

- You can generate the `SECRET_KEY` via sites like [Djecrety](https://djecrety.ir/) and add it to the `.env` file.

> Set DEBUG to True while developing and testing in local/testing environments. Otherwise, set DEBUG to False.

After properly configuring the environment variables, you can proceed to the installation section below.

## Setup with uv

Make sure [uv](https://docs.astral.sh/uv/) is installed on your system.

```bash
$ pwd
/written-pronunciation

# Install dependencies and create virtual environment
$ uv sync

# Run migrations
$ uv run python manage.py makemigrations
$ uv run python manage.py migrate

# Start the server
$ uv run python manage.py runserver
```
 After the installation process, you must see this output:
![Server success output](/images/server-running-successfully.png) 
You can start exploring the project from either http://localhost:8000/ or http://localhost:8000/api/. Happy coding!

> Remember, you must approve the created Words from the admin panel in order them to be visible across the project.

> You can access the API documentation from http://localhost:8000/api/docs/.
