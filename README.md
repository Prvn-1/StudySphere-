# PROJECT LINK - https://campusshare.onrender.com
# CampusShare

**CampusShare** is a web-based academic resource sharing platform designed for college students.
It allows students to upload, download, rate, and comment on study materials such as notes, question papers, assignments, and reference documents.
The platform promotes collaborative learning by making academic resources easily accessible in one place.

---

##  Features

*  **User Authentication & Authorization**

  * Student registration and login
  * Secure authentication using Django
  * Admin approval for uploaded resources

*  **Resource Upload & Download**

  * Upload PDFs, documents, and study materials
  * Download count tracking
  * Admin verification before public access

*  **Ratings & Comments**

  * Rate resources (1–5 stars)
  * View average ratings
  * Comment on shared resources

*  **Search & Filter**

  * Search by title and description
  * Filter by college, department, category, semester

*  **Pagination**

  * Efficient loading of large resource lists

*  **User Profile**

  * Edit profile details
  * Upload profile picture
  * View uploaded resources

*  **Admin Panel**

  * Manage users and resources
  * Approve or reject uploads
  * Maintain content quality

---

## Project Architecture

CampusShare follows **Django’s MVT (Model–View–Template)** architecture:

* **Model** – Database schema using Django ORM
* **View** – Business logic and request handling
* **Template** – HTML pages with Django template language

### Components:

* **Frontend (UI)**: HTML, CSS, JavaScript
* **Backend**: Django (Python)
* **Database**: SQLite / PostgreSQL
* **ORM**: Django ORM
* **Static Files**: CSS, JS, Images
* **Media Files**: Uploaded resources and profile images

---

##  Technologies Used

* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Python, Django
* **Database**: SQLite / PostgreSQL
* **Authentication**: Django Auth System
* **Version Control**: Git & GitHub

---

##  How to Run the Project Locally

1. **Clone the repository**

```bash
git clone https://github.com/your-username/campusshare.git
cd campusshare
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

6. **Run server**

```bash
python manage.py runserver
```

7. Open browser:

```
http://127.0.0.1:8000/
```

---

##  Project Goal

The main goal of CampusShare is to:

* Centralize academic resources
* Reduce time spent searching for study materials
* Help juniors access senior materials
* Encourage peer-to-peer learning
* Promote collaboration within college communities

---

##  Author

**Kokila**
Student | Web Developer
Built with 💙 using Django

---

##  Future Enhancements

* Email / OTP login
* Bookmark resources
* Notifications for new uploads
* REST API for mobile app
* Role-based permissions (Faculty uploads)

---

