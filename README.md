# written-pronunciation

**Although you can view this project on the site (the project was primarily built for the desktop, so its mobile UI is far from being aesthetic and responsive -help wanted! :)-), it is no longer active or maintained. Still, you can open an issue or a PR if you find a critical bug, I'll fix it ASAP.**

***

An English written pronunciation site for Turkish hard of hearing and deaf people who can't listen to words' verbal pronunciation.

![Main Page SS](https://user-images.githubusercontent.com/53350572/183075250-12c8a87a-b570-4eb2-831c-990d009e832b.png)

***

## Features

- Bootstrap4.
- User authentication & authorization.
- Create, Read, Update and Delete functionality.
- Pagination.
- Searching.
- API authentication & authorization.
- API CRUD functionality.
- API documentation.
- Tests.

# Live showcase

## Pages

- [Sign Up](https://pronunciationksenofanex.herokuapp.com/users/signup/) 

- [Login](https://pronunciationksenofanex.herokuapp.com/users/login/)

- [Main](https://pronunciationksenofanex.herokuapp.com/)

- [Word Detail](https://pronunciationksenofanex.herokuapp.com/2/) 

- [User's Words](https://pronunciationksenofanex.herokuapp.com/user-words/Ksenofanex/)

## API Registration & Authentication

- [API Registration](https://pronunciationksenofanex.herokuapp.com/api/v1/rest-auth/registration/) 

- [API Login](https://pronunciationksenofanex.herokuapp.com/api-auth/login/?next=/api/)

## API

- [API Root](https://pronunciationksenofanex.herokuapp.com/api/)

- [API Main](https://pronunciationksenofanex.herokuapp.com/api/words/) 

## API Documentation

- [Main Documentation]( https://pronunciationksenofanex.herokuapp.com/swagger-docs/)

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

After properly configuring the environment variables, you can proceed to the [Venv](https://github.com/Ksenofanex/written-pronunciation#venv) section to initialize the project.

## Venv
Make sure your working directory is the same with the project and virtualenv package is installed in your OS.

<details>
<summary>Windows</summary>

```bash
> pwd
\written-pronunciation

> pip install virtualenv

> virtualenv env

> .\env\Scripts\activate

> pip install -r requirements.txt

> python manage.py makemigrations

> python manage.py migrate

> python manage.py runserver
```

![Virtualenv GIF](https://i.imgur.com/T769x6j.gif)

</details>

<details>
<summary>Linux</summary>

```bash
$ pwd
/written-pronunciation

$ pip3 install virtualenv

$ python3 -m venv env

$ source env/bin/activate

$ pip3 install requirements.txt

$ python3 manage.py makemigrations

$ python3 manage.py migrate

$ python3 manage.py runserver
```

</details>

- After the installation process, you must see this output:

![Virtualenv success output](https://i.imgur.com/9Dwp7s0.png)

Then you can start exploring the project from either http://localhost:8000/ or http://localhost:8000/api. Happy coding!

> Remember, you must approve the created Words from the admin panel in order them to be visible across the project.

> You can access to the documentation of the project from this URLs (http://localhost:8000/swagger-docs/ or http://127.0.0.1:8000/swagger-docs/).
