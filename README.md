## Study Management Platform Backend (Django REST Framework)

- User registration and JWT authentication
- Flashcards (front/back)
- Quizzes (question/answer)
- Matching items (word ↔ meaning)
- Notes (title + content)

All study data is **user-specific** – users can only see and modify their own items.

---

### 1. Tech Stack

- **Python 3.10**
- **Django 5**
- **Django REST Framework**
- **djangorestframework-simplejwt** (JWT auth)
- **drf-spectacular** (auto API schema + Swagger UI)

---

### 2. Project Setup

#### 2.1 Clone the repository

```bash
git clone <your-repo-url>
cd Jvai_task  # or the folder name you used
```

#### 2.2 Create and activate virtual environment (Windows, PowerShell)

```bash
python -m venv venv
.\venv\Scripts\activate
```

#### 2.3 Install dependencies

```bash
pip install -r requirements.txt
```

#### 2.4 Run migrations

```bash
python manage.py migrate
```

#### 2.5 Create a superuser (optional, for Django admin)

```bash
python manage.py createsuperuser
```

#### 2.6 Start development server

```bash
python manage.py runserver
```

Server will run on `http://127.0.0.1:8000/` by default.

---

### 3. Important URLs

- **Swagger UI (auto docs)**: `http://127.0.0.1:8000/api/docs/`

Authentication and CRUD endpoints are under the `/api/` prefix:

- `/api/auth/register/` – register
- `/api/auth/token/` – obtain JWT (login)
- `/api/auth/token/refresh/` – refresh JWT
- `/api/flashcards/` – flashcards CRUD
- `/api/quizzes/` – quizzes CRUD
- `/api/matching-items/` – matching items CRUD
- `/api/notes/` – notes CRUD

More details and JSON examples are in `API_DOCUMENTATION.md`.

---

### 4. Authentication Flow (Beginner-Friendly)

1. **Register**
   - Send `POST /api/auth/register/` with `username`, `email` (optional), and `password`.
2. **Login**
   - Send `POST /api/auth/token/` with `username` and `password`.
   - You will receive a **refresh token** and an **access token**.
3. **Use access token**
   - Add this header to all protected requests:
     - `Authorization: Bearer <access_token>`
4. **Refresh access token**
   - When the access token expires, send `POST /api/auth/token/refresh/` with your `refresh` token.

---

### 5. User-Specific Data

- Every model (`Flashcard`, `Quiz`, `MatchingItem`, `Note`) has an `owner` field.
- Viewsets only return objects where `owner == request.user`.
- Extra permission checks are in place on update/delete to prevent cross-user access.

---

### 6. Testing with Postman

Basic steps:

1. Register a user.
2. Obtain tokens via `/api/auth/token/`.
3. Add the access token as Bearer token in Postman.
4. Call the CRUD endpoints (`/api/flashcards/`, `/api/quizzes/`, etc.).

You can also explore and try all endpoints from the built-in Swagger UI at `/api/docs/`.

---

### 7. Folder Structure (Simplified)

```text
study_platform/        # Django project config (settings, urls, wsgi)
study/                 # Main app with models, serializers, views, urls
  models.py            # Flashcard, Quiz, MatchingItem, Note
  serializers.py       # UserRegister + model serializers
  views.py             # RegisterView + ModelViewSets
  urls.py              # /api/... endpoints
API_DOCUMENTATION.md   # Hand-written API docs with examples
requirements.txt       # Python dependencies
README.md              # This file
```

---

### 8. Notes for Evaluation

- JWT is enabled globally via `REST_FRAMEWORK` settings and SimpleJWT.
- All API endpoints (except register and token endpoints) are protected.
- Code is kept intentionally small and commented to be friendly for beginners.


