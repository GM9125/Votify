# Votify
```
A secure and efficient web-based voting system built with Django framework. This system enables organizations to conduct elections online while maintaining security, transparency and ease of use.
```
## Features

### Voter Features
- Secure voter registration and authentication
- Cast votes for multiple positions
- View personal ballot history
- OTP verification
- One-time voting restriction

### Admin Features  
- Complete election management
- Voter records management
- Position and candidate setup
- Real-time vote tallying
- PDF report generation
- Ballot configuration
- Election settings control

## Tech Stack
- **Backend:** Python 3.8+, Django 3.2+
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 4
- **Database:** SQLite3
- **Authentication:** Django Auth
- **Charts:** Chart.js
- **PDF:** WeasyPrint


## Installation

1. Clone the repository
```bash
git clone https://github.com/GM9125/Votify.git
cd Votify
```

2. Create virtual environment
```bash
python -m venv venv
venv\Scripts\activate     # Windows
source venv/bin/activate  # Linux/Mac
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Setup database migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Create administrator user
```bash
python manage.py createsuperuser
```

6. Run development server
```bash
python manage.py runserver
```

Access the application at `http://127.0.0.1:8000/`


## Security Features

- CSRF Protection
- Session Management
- One-time voting restriction
- Role-based access control
- Password hashing
- Form validation

## Project Structure
```
Votify/
├── account/         # Authentication
├── administrator/   # Admin panel
├── e-voting/        # Core voting
├── media/           # Uploads
├── static/          # Assets
└── voting/          # HTML files
```

## Access Control

| Role  | Permissions |
|-------|-------------|
| Admin | Full system control|
| Voter | Vote casting, View ballot|


## Contributors

```
Made with ❤️ by
Ghulam Mustafa
```

## Contact

- Email: gmustafa.bese23seecs@seecs.edu.pk
- GitHub: https://github.com/GM9125
- Linkedin: https://www.linkedin.com/in/ghulam-mustafa2/
- Contact: +923195631613
