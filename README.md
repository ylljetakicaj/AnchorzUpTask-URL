# URL Shortener Project

This is a simple URL shortener web application built using **Flask**. It allows users to shorten long URLs, specify expiration times for the shortened URLs, and manage them through an intuitive interface. The project features a database to store the original and shortened URLs along with their expiration times.

---

### Features

- **Shorten URLs**: Input a long URL and get a shortened version.
- **Expiration Dates**: Choose from preset expiration times (e.g., 1 minute, 5 minutes).
- **URL Management**: View, delete, and manage all active shortened URLs.
- **Automatic Expiration**: Expired URLs are automatically excluded from the active list.

---

### Prerequisites

To run this project, ensure you have the following installed on your system:

- Python 3.8 or later
- Pip (Python package manager)

### How to run

Before running the application, ensure all required dependencies are installed using the 'requirements.txt file'. Run the following command:
```pip install -r requirements.txt```
'flask
flask-sqlalchemy
flask-restful
shortuuid'

**Initialize the Database:**
Run the application once to initialize the SQLite database. The app will automatically create the database.db file in the project directory if it doesn't already exist.

**Start the Flask Development Server:**
Use the following command to start the application:
```python app.py```

**Access the Application:**
Open your browser and navigate to the following URL:
```http://127.0.0.1:5000```


  
---
