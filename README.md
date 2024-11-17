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

---

### How to run

Before running the application, ensure all required dependencies are installed using the ```requirements.txt``` file. Run the following command:
```pip install -r requirements.txt```


**Initialize the Database:**
Run the application once to initialize the SQLite database. The app will automatically create the database.db file in the project directory if it doesn't already exist.

**Start the Flask Development Server:**
Use the following command to start the application:
```python app.py```

**Access the Application:**
Open your browser and navigate to the following URL:
```http://127.0.0.1:5000```

---
## Application Structure

### Main Files:

1. **`app.py`**:  
   The core Flask application that handles routes and logic:
   - `/` (GET/POST): The homepage for shortening and managing URLs.
   - `/<short_identifier>`: Redirects to the original URL if the shortened URL is active and not expired.
   - `/delete/<int:link_id>`: Deletes a shortened URL from the database.

2. **`index.html`**:  
   The main HTML file containing the UI for the URL shortener.

3. **`styles.css`**:  
   CSS file for styling the UI.

---
