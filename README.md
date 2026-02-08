
# PROJECT LINK – [https://studysphere-04og.onrender.com/](https://studysphere-04og.onrender.com/)

# StudySphere

**StudySphere** is a full-stack academic resource sharing platform built using Django.
It enables students to upload, download, rate, and manage study materials in a secure and structured environment.
The platform focuses on simplifying academic collaboration and improving access to educational resources.

---

## Features

* **User Authentication & Authorization**

  * Secure student registration and login
  * Django authentication system
  * Profile management

* **Resource Upload & Management**

  * Upload academic materials (PDF, documents)
  * Download tracking system
  * Organized resource categories

* **Ratings & Feedback**

  * Rate shared resources
  * View average ratings
  * Interactive feedback system

* **Search & Filtering**

  * Search by title and description
  * Filter by department, semester, and category

* **User Profile System**

  * Update profile information
  * View personal uploads
  * Manage shared resources

* **Database Integration**

  * Structured storage of users and resources
  * Efficient data retrieval using Django ORM

---

## Project Architecture

StudySphere follows **Django’s MVT (Model–View–Template)** architecture:

* **Model** – Database structure using Django ORM
* **View** – Business logic and request handling
* **Template** – Frontend rendering using Django template engine

### Components:

* **Frontend (UI)**: HTML, CSS, JavaScript
* **Backend**: Django (Python)
* **Database**: MySQL
* **ORM**: Django ORM
* **Static Files**: CSS, JavaScript, Images
* **Media Files**: Uploaded study materials

---

## Technologies Used

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python, Django
* **Database**: MySQL
* **Authentication**: Django Authentication System
* **Version Control**: Git & GitHub

---

## How to Run the Project Locally

1. **Clone the repository**

```bash
git clone https://github.com/your-username/studysphere.git
cd studysphere
```

2. **Create virtual environment**

```bash
python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py migrate
```

5. **Create superuser**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

7. Open in browser:

```
http://127.0.0.1:8000/
```

---

## Project Objective

The goal of StudySphere is to:

* Provide a centralized academic resource hub
* Improve accessibility to study materials
* Encourage collaborative learning
* Reduce duplication of effort among students
* Build a structured digital academic ecosystem

---


## Future Enhancements

* Email verification system
* Bookmark feature
* Resource recommendation system
* REST API for mobile integration
* Role-based access (Faculty / Admin / Student)

