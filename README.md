# college-email-portal

![Project Screenshot](static/images/screenshot(180).png) <!-- Add a screenshot later -->

A full-stack web application that enables students and parents to send official emails to college staff members with templates and attachments.

## Features

- 📧 Send emails to college staff (Principal, Office, HODs)
- 📝 Predefined email templates with auto-fill
- 📎 File attachment support (PDF/Images)
- 📱 Fully responsive design (mobile & desktop)
- 🔐 Admin panel for managing templates and recipients
- 📊 Email logging for record keeping

## Tech Stack

**Frontend:**  
- Bootstrap 5
- Custom CSS animations
- Responsive design

**Backend:**  
- Django 5
- PostgreSQL (SQLite for development)
- SMTP email integration

## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/ADN004/college-email-portal.git
   cd college-email-portal

## Setup
1. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows

2. Install dependencies:
   ```bash
   pip install -r requirements.txt

3. Configure environment:
   Update the .env
   Update with your SMTP credentials:
   ```ini
   EMAIL_HOST_USER=your@email.com
   EMAIL_HOST_PASSWORD=your-password

5. Run migrations:
   ```bash
   python manage.py migrate

6. Create admin user:
    ```bash
    python manage.py createsuperuser

7. Run development server:
    ```bash
    python manage.py runserver

## Usage
- Access the portal at http://localhost:8000
- Students/parents can:
   1. Select recipients from dropdown
   2. Choose email templates
   3. Send emails with attachments
   4. Admins can manage templates at http://localhost:8000/admin
