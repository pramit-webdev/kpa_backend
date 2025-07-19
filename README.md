# KPA Backend Assignment - Pramit Das

This project is a FastAPI-based backend for selected form submissions from the KPA Form Data system. It connects to a PostgreSQL database and integrates with the provided Flutter frontend.

---

## ✨ Tech Stack

* **Language**: Python 3.10+
* **Framework**: FastAPI
* **Database**: PostgreSQL
* **ORM**: SQLAlchemy
* **Data Validation**: Pydantic
* **Environment Configuration**: python-dotenv
* **Server**: Uvicorn
* **API Testing**: Postman / Hoppscotch

---

## ⚙️ Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/your-username/kpa_backend.git
cd kpa_backend
```

2. **Create virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Setup environment variables**
   Create a `.env` file with:

```
DATABASE_URL=postgresql://username:password@localhost:5432/kpa_db
```

5. **Run the server**

```bash
uvicorn main:app --reload
```

Visit: [http://localhost:8000/docs](http://localhost:8000/docs) for Swagger UI.

---

## 🔧 Implemented APIs

### 1. `POST /forms/wheel-specifications`

* Accepts: `formNumber`, `submittedBy`, `submittedDate`, `fields` (dict).
* Creates a new wheel specification form entry.

### 2. `GET /forms/wheel-specifications`

* Filters: `formNumber`, `submittedBy`, `submittedDate`
* Returns filtered list of wheel specification entries.

### 3. `POST /forms/bogie-checksheet`

* Accepts: `formNumber`, `inspectionBy`, `inspectionDate`, `bogieDetails`, `bogieChecksheet`, `bmbcChecksheet`.
* Creates a new bogie checksheet record.

### 4. `GET /forms/bogie-checksheet`

* Filters: `formNumber`
* Returns bogie checksheet entry.

---

## 🔍 Limitations & Assumptions

* `formNumber` is enforced as a unique field.
* `fields` and other complex sections are stored as `JSON`.
* No authentication layer added (assumes trusted usage).
* Database must be pre-created before running the app.
* Error handling assumes valid schema input from frontend.

---

## 🌟 Optional Enhancements

* Dockerize the backend for easy deployment
* Add pagination on GET endpoints
* Setup Alembic for migrations
* Implement JWT authentication

---

## 📄 Submission Checklist

* [x] Source Code
* [x] Postman Collection
* [x] README
* [x] Screen Recording

---

Author: **Pramit Das**
