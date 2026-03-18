# Written Pronunciation

An English written pronunciation site for Turkish hard of hearing and deaf people who can't listen to words' verbal pronunciation.

![Main Page Screenshot](main-page-screenshot.png)

## Features

- Modern and aesthetic design
- Dark & light mode
- User authentication & authorization
- Word CRUD (Create, Read, Update, Delete)
- Search functionality
- Pagination
- REST API with token authentication & authorization
- Interactive API documentation
- Thorough and elegant tests

## Quick Start

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) package manager

### Setup

```bash
git clone https://github.com/Ksenofanex/written-pronunciation.git
cd written-pronunciation

# Create environment file
cp .env.example .env
# Edit .env with your SECRET_KEY (generate one at https://djecrety.ir/)

# Install dependencies and create virtual environment
uv sync

# Run migrations
uv run python manage.py makemigrations
uv run python manage.py migrate

# Start the server
uv run python manage.py runserver
```

Then open http://localhost:8000/

### Running Tests

```bash
uv run pytest
```

### Environment Variables

Create a `.env` file in the project root:

```
DEBUG=True
SECRET_KEY=your-secret-key-here
```

Set `DEBUG=False` in production.

## API

| Endpoint | Description |
|----------|-------------|
| `/api/words/` | Word list and creation |
| `/api/words/<id>/` | Word detail, update, delete |
| `/api/docs/` | Swagger UI documentation |
| `/api/schema/` | OpenAPI 3.0 schema |
| `/api/v1/rest-auth/` | Authentication endpoints |
| `/api/v1/rest-auth/registration/` | Registration endpoint |