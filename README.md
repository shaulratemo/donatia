### 🌍 Donatia — Donations Management Platform

Donatia is a Django REST API designed to connect donors with verified charitable organizations.
It enables donors to browse causes, make secure donations, and track their giving history.
Organizations can register, create causes, and monitor their donations, while administrators oversee all system activity, approvals, and reports.

### 🚀 Features
## 🔐 User Authentication

Custom user model (Donor, Organization, Admin roles)

JWT-based login and logout using SimpleJWT

Role-based permissions for secure access control

## 🏢 Organization Management

Organization users can register their profiles

Pending approval workflow — Admins review and approve

Public listing of approved organizations

## 🎯 Cause Management

Approved organizations can create and manage donation causes

Public can browse all active causes

Admins and organization owners can edit or deactivate causes

## 💰 Donation Management

Donors can contribute to specific causes

Each donation is linked to both a donor and a cause

Track donations and totals per organization/cause

## 📊 Dashboard & Reports

Admin Dashboard: Displays global system stats (total donations, top organizations, top causes)

Organization Dashboard: Shows each organization’s donation performance, total funds, and top causes

## 🧱 Role-Based Access

Donors → Can browse causes and make donations

Organizations → Can manage their causes and view dashboards

Admins → Approve organizations, moderate content, and view reports

### 🛠️ Tech Stack
Layer	Technology
Backend	Django 5, Django REST Framework
Auth	SimpleJWT (Access & Refresh Tokens)
Database	SQLite (development) / PostgreSQL (production-ready)
API Testing	Postman
Version Control	Git & GitHub

### 📂 Project Structure
DonatiaApp/
│
├── donatia/                # Project config (settings, urls, wsgi)
│
├── users/                  # Custom User model, serializers, and JWT auth views
├── organizations/          # Organization model, endpoints, and admin approval
├── causes/                 # Cause creation, listing, and permissions
├── donations/              # Donation model and endpoints
├── dashboard/              # Reports for Admins & Organizations
│
└── README.md

### ⚙️ Setup Instructions
1️⃣ Clone the Repository
git clone https://github.com/<your-username>/donatia.git
cd donatia

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run Migrations
python manage.py makemigrations
python manage.py migrate

5️⃣ Create a Superuser
python manage.py createsuperuser

6️⃣ Start the Server
python manage.py runserver


Server runs at:
➡️ http://127.0.0.1:8000/

### 🧭 API Endpoints Summary
Endpoint	Method	Description	Access
/auth/register/	POST	Register donor or organization	Public
/auth/login/	POST	Login and receive JWT tokens	Public
/auth/logout/	POST	Logout and blacklist token	Authenticated
/auth/me/	GET	Get current user details	Authenticated
/organizations/	GET / POST	List or register organizations	Authenticated (org role)
/organizations/{id}/	GET / PUT / PATCH / DELETE	View or edit organization details	Org owner / Admin
/causes/	GET / POST	View or create causes	Public / Org owner
/causes/{id}/	GET / PUT / DELETE	View, update, or delete a cause	Org owner / Admin
/donations/	GET / POST	List or make donations	Donor
/donations/{id}/	GET	View donation details	Donor / Admin
/dashboard/admin/	GET	View global donation stats	Admin
/dashboard/organization/	GET	View organization stats	Organization

### 🧪 Testing

Use Postman for testing API endpoints:

Register and log in as a user to get an access token.

Add the token to headers:

Authorization: Bearer <access_token>


Test endpoints based on user roles (Donor, Organization, Admin).

### 🧑‍💻 Author

Shaul R.
Backend Developer | UI/UX Designer | Software Engineering Student

📧 ratemoshaul@gmail.com
🌐 [Portfolio Coming Soon]
💼 [LinkedIn Coming Soon]

### 🏁 Future Enhancements

M-Pesa STK push integration for real donation payments

Email notifications for donors and organizations

Public donation leaderboard per cause

Admin analytics dashboard UI