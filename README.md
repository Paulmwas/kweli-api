# Kwelinews API Documentation

![Kwelinews Logo](https://via.placeholder.com/150x50?text=Kwelinews)  
**A RESTful API for Kenyan News Platform**

## Table of Contents
1. [Backend Architecture](#backend-architecture)
2. [API Endpoints](#api-endpoints)
  - [Authentication](#authentication)
  - [Articles](#articles)
  - [Categories](#categories)
  - [Tags](#tags)
  - [User Profile](#user-profile)
3. [Setup Instructions](#setup-instructions)
4. [Environment Variables](#environment-variables)
5. [Deployment](#deployment)

## Backend Architecture

### Tech Stack
- **Framework**: Django 5.2 + Django REST Framework
- **Database**: SQLite (development), PostgreSQL (production)
- **Authentication**: JWT (JSON Web Tokens)
- **CORS**: Enabled for specified origins

### Core Components
1. **Authentication Service**: Handles user registration, login, and token management
2. **Content Management**: Manages news articles, categories, and tags
3. **User Service**: Handles user profiles and preferences
4. **Search Engine**: Full-text search and filtering capabilities
5. **Analytics**: Tracks article views and user engagement

### Database Schema
```
User → Article (One-to-Many)
Article → Category (Many-to-One)
Article → Tag (Many-to-Many)
```

## API Endpoints

### Authentication

#### `POST /api/auth/register/`
Register a new user.
**Request Body**:
```json
{
  "username": "string",
  "email": "string",
  "password": "string",
  "password2": "string",
  "first_name": "string",
  "last_name": "string"
}
```

**Response**:
```json
{
  "refresh": "string",
  "access": "string",
  "user": {
  "id": "integer",
  "username": "string",
  "email": "string"
  }
}
```

#### `POST /api/auth/login/`
Obtain JWT tokens.

**Request Body**:
```json
{
  "username": "string",
  "password": "string"
}
```

**Response**:
```json
{
  "refresh": "string",
  "access": "string"
}
```

#### `POST /api/auth/logout/`
Invalidate refresh token.

**Request Body**:
```json
{
  "refresh": "string"
}
```

### Articles

#### `GET /api/articles/`
List all published articles.

**Query Parameters**:
- `category__slug`: Filter by category slug
- `page`: Pagination

**Response**:
```json
{
  "count": "integer",
  "next": "url|null",
  "previous": "url|null",
  "results": [
  {
   "id": "integer",
   "title": "string",
   "slug": "string",
   "excerpt": "string",
   "lead_image": "url",
   "category": {
    "id": "integer",
    "name": "string",
    "slug": "string"
   },
   "tags": [
    {
     "id": "integer",
     "name": "string",
     "slug": "string"
    }
   ],
   "publish_date": "datetime",
   "view_count": "integer"
  }
  ]
}
```

#### `GET /api/articles/{slug}/`
Retrieve article details.

**Response**:
```json
{
  "id": "integer",
  "title": "string",
  "slug": "string",
  "content": "string",
  "lead_image": "url",
  "status": "string",
  "is_featured": "boolean",
  "is_trending": "boolean",
  "view_count": "integer",
  "author": {
  "id": "integer",
  "username": "string"
  },
  "category": {
  "id": "integer",
  "name": "string",
  "slug": "string",
  "description": "string"
  },
  "tags": [
  {
   "id": "integer",
   "name": "string",
   "slug": "string"
  }
  ],
  "publish_date": "datetime",
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

### Categories

#### `GET /api/categories/`
List all categories.

**Response**:
```json
[
  {
  "id": "integer",
  "name": "string",
  "slug": "string",
  "description": "string"
  }
]
```

#### `GET /api/categories/{slug}/`
List articles in a specific category.

**Response**: Same as the articles list endpoint.

### Tags

#### `GET /api/tags/`
List all tags.

**Response**:
```json
[
  {
  "id": "integer",
  "name": "string",
  "slug": "string",
  "is_trending": "boolean"
  }
]
```

#### `GET /api/tags/{slug}/`
List articles with a specific tag.

**Response**: Same as the articles list endpoint.

### User Profile

#### `GET /api/auth/profile/`
Get current user profile.

**Headers**:
```
Authorization: Bearer <access_token>
```

**Response**:
```json
{
  "id": "integer",
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "bio": "string",
  "profile_picture": "url",
  "twitter_handle": "string"
}
```

#### `PATCH /api/auth/profile/`
Update user profile.

**Headers**:
```
Authorization: Bearer <access_token>
Content-Type: multipart/form-data
```

**Request Body** (form-data):
- `first_name` (string)
- `last_name` (string)
- `bio` (string)
- `twitter_handle` (string)
- `profile_picture` (file)

## Setup Instructions

### Development Setup
1. Clone the repository
2. Create and activate virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # Linux/Mac
  venv\Scripts\activate     # Windows
  ```
3. Install dependencies:
  ```bash
  pip install -r requirements.txt
  ```
4. Set up environment variables (see below)
5. Run migrations:
  ```bash
  python manage.py migrate
  ```
6. Create superuser:
  ```bash
  python manage.py createsuperuser
  ```
7. Run development server:
  ```bash
  python manage.py runserver
  ```

## Environment Variables

Create a `.env` file in project root:

```ini
# Django
SECRET_KEY=your-secret-key-here
DEBUG=False
ALLOWED_HOSTS=.yourdomain.com,localhost,127.0.0.1

# Database (for production)
DB_ENGINE=django.db.backends.postgresql
DB_NAME=kwelinews
DB_USER=dbuser
DB_PASSWORD=dbpassword
DB_HOST=localhost
DB_PORT=5432

# CORS
CORS_ALLOWED_ORIGINS=https://btn-kenya.vercel.app,http://localhost:5173,http://127.0.0.1:5173

# JWT Settings
ACCESS_TOKEN_LIFETIME_MINUTES=60
REFRESH_TOKEN_LIFETIME_DAYS=1

# Media Storage
MEDIA_URL=/media/
MEDIA_ROOT=media

# Email (optional)
EMAIL_HOST=smtp.yourservice.com
EMAIL_PORT=587
EMAIL_HOST_USER=your@email.com
EMAIL_HOST_PASSWORD=emailpassword
DEFAULT_FROM_EMAIL=no-reply@kwelinews.com
```

## Deployment

### Production Setup
For production deployment, it's recommended to:

1. Use PostgreSQL instead of SQLite
2. Configure a web server like Nginx to serve static/media files
3. Use Gunicorn as the WSGI server

#### Setup steps:
1. Set up a PostgreSQL database
2. Update settings.py to use the PostgreSQL database in production
3. Configure Gunicorn:
  ```bash
  gunicorn --bind 0.0.0.0:8000 kweliapi.wsgi:application
  ```
4. Set up Nginx as a reverse proxy to Gunicorn
5. Configure static files:
  ```bash
  python manage.py collectstatic
  ```
6. Set up SSL/TLS for secure connections

---

**License**: MIT  
**Maintainer**: Kwelinews Team  
**API Version**: 1.0.0
