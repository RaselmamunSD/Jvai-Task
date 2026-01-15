API Documentation

This file gives a beginner-friendly overview of the available API endpoints.

All protected endpoints require a valid JWT access token** in the `Authorization` header:

`Authorization: Bearer <your_access_token>`

---

### 1. Authentication

#### 1.1 Register
- **URL**: `/api/auth/register/`
- **Method**: `POST`
- **Auth**: Public (no token required)

**Request body (JSON)**:
```json
{
  "username": "rasel",
  "email": "rasel@gmail.com",
  "password": "123456"
}
```

**Success response (201)**:
```json
{
  "id": 1,
  "username": "rasel",
  "email": "rasel@gmail.com"
}
```

#### 1.2 Obtain JWT token pair (login)
- **URL**: `/api/auth/token/`
- **Method**: `POST`
- **Auth**: Public

**Request body (JSON)**:
```json
{
  "username": "rasel",
  "password": "123456"
}
```

**Success response (200)**:
```json
{
  "refresh": "REFRESH_TOKEN_STRING",
  "access": "ACCESS_TOKEN_STRING"
}
```

#### 1.3 Refresh access token
- **URL**: `/api/auth/token/refresh/`
- **Method**: `POST`
- **Auth**: Public

**Request body (JSON)**:
```json
{
  "refresh": "REFRESH_TOKEN_STRING"
}
```

**Success response (200)**:
```json
{
  "access": "NEW_ACCESS_TOKEN_STRING"
}
```

---

### 2. Flashcards

Base URL for flashcards: `/api/flashcards/`

> Note: All flashcard endpoints require a valid access token.

#### 2.1 List current user flashcards
- **URL**: `/api/flashcards/`
- **Method**: `GET`
- **Auth**: JWT required

**Sample response (200)**:
```json
[
  {
    "id": 1,
    "owner": "rasel",
    "front_text": "2 + 2",
    "back_text": "4",
    "created_at": "2026-01-14T10:00:00Z",
    "updated_at": "2026-01-14T10:00:00Z"
  }
]
```

#### 2.2 Create a flashcard
- **URL**: `/api/flashcards/`
- **Method**: `POST`
- **Auth**: JWT required

**Request body (JSON)**:
```json
{
  "front_text": "Capital of France",
  "back_text": "Paris"
}
```

**Success response (201)**: same shape as list item above.

#### 2.3 Retrieve a single flashcard
- **URL**: `/api/flashcards/<id>/`
- **Method**: `GET`
- **Auth**: JWT required, **only owner can access**

#### 2.4 Update a flashcard
- **URL**: `/api/flashcards/<id>/`
- **Method**: `PUT` or `PATCH`
- **Auth**: JWT required, only owner can update

#### 2.5 Delete a flashcard
- **URL**: `/api/flashcards/<id>/`
- **Method**: `DELETE`
- **Auth**: JWT required, only owner can delete

---

### 3. Quizzes

Base URL for quizzes: `/api/quizzes/`

Fields:
- `title` – short name of the quiz
- `question` – the main question
- `answer` – correct answer

Endpoints are similar to flashcards:
- `GET /api/quizzes/` – list current user quizzes
- `POST /api/quizzes/` – create
- `GET /api/quizzes/<id>/` – retrieve
- `PUT/PATCH /api/quizzes/<id>/` – update
- `DELETE /api/quizzes/<id>/` – delete

Example create body:
```json
{
  "title": "Math quiz",
  "question": "What is 3 * 3?",
  "answer": "9"
}
```

---

### 4. Matching Items

Base URL for matching items: `/api/matching-items/`

Fields:
- `left_text` – e.g. a word
- `right_text` – e.g. its meaning

Endpoints:
- `GET /api/matching-items/`
- `POST /api/matching-items/`
- `GET /api/matching-items/<id>/`
- `PUT/PATCH /api/matching-items/<id>/`
- `DELETE /api/matching-items/<id>/`

Example create body:
```json
{
  "left_text": "Osmosis",
  "right_text": "Movement of water through a semi-permeable membrane"
}
```

---

### 5. Notes

Base URL for notes: `/api/notes/`

Fields:
- `title`
- `content`

Endpoints:
- `GET /api/notes/`
- `POST /api/notes/`
- `GET /api/notes/<id>/`
- `PUT/PATCH /api/notes/<id>/`
- `DELETE /api/notes/<id>/`

Example create body:
```json
{
  "title": "Chapter 1 Summary",
  "content": "This chapter covers the basics of cell biology ..."
}
```

---

### 6. Error Handling

Common error responses:

- **401 Unauthorized** – missing or invalid token
```json
{
  "detail": "Authentication credentials were not provided."
}
```

- **403 Forbidden** – trying to access another user’s data
```json
{
  "detail": "You do not have permission to perform this action."
}
```

- **400 Bad Request** – validation errors
```json
{
  "front_text": ["This field may not be blank."]
}
```


