# Donatia — Donations Management Platform

**Donatia** is a donations management platform that connects donors with local charitable organizations.  
It allows donors to browse causes, make donations, and track their giving history, while organizations can showcase causes and monitor funds received.  
Admins oversee activity, approve organizations, and manage the system.

---

## Features (MVP)
- **User Authentication** — Custom user model with donor, organization, and admin roles.
- **Organization Management** — Organizations can register, manage details, and await admin approval.
- **Cause Management** *(coming next)* — Organizations can create and manage donation causes.
- **Donations Tracking** *(coming next)* — Donors can make and track their contributions.
- **Dashboard & Reports** *(planned)* — Summary of total donations, causes, and organization stats.
- **Role-Based Permissions** — Secure access for different user types.

---

## Tech Stack
- **Backend:** Django & Django REST Framework (DRF)
- **Authentication:** JWT (via `djangorestframework-simplejwt`)
- **Database:** SQLite (development) / PostgreSQL (production-ready)
- **Version Control:** Git & GitHub

---

## Project Structure
DonatiaApp/
│
├── donatia/ # Root project folder
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── users/ # Custom user model and auth APIs
├── organizations/ # Organization models, serializers, and endpoints
├── causes/ # (Coming soon)
├── donations/ # (Coming soon)
├── dashboard/ # (Coming soon)
│
└── README.md


---

## Setup Instructions

### 1️⃣ Clone the repository
~ bash
git clone https://github.com/< your-username >/donatia.git
cd donatia
### 2️⃣ Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a superuser
python manage.py createsuperuser

6️⃣ Run the development server
python manage.py runserver

### API Endpoints Summary
Endpoint	    Method	Description	Access
/auth/register/	POST	Register donor or organization user	Public
/auth/login/	POST	Login and receive JWT token	Public
/auth/me/	GET	View current user details	Authenticated
/organizations/	GET / POST	List or create organizations	Authenticated (org role)
/organizations/{id}/	GET / PUT / DELETE	View or edit organization details	Authenticated / Admin
/dashboard/	GET	View analytics (future)	Admin / Org

## 🧑‍💻 Author

# Shaul R.
# ALX Backend Developer | UI/UX Designer

🌐 Portfolio

💼 LinkedIn

📧 ratemoshaul@gmail.com