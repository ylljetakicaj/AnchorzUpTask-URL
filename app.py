from flask import Flask, render_template, request, redirect, url_for, request
import sqlite3
from shortuuid import ShortUUID
import time

app = Flask(__name__)
db_file = "database.db"

# Initialize the database
def init_db():
    with sqlite3.connect(db_file) as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_url TEXT NOT NULL,
                expiration INTEGER NOT NULL
            )
        """)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        # Retrieve form data
        original_url = request.form.get("original_url")
        expiration_option = request.form.get("expiration")

        if not original_url or not expiration_option:
            return redirect(url_for("index"))  # Ensure fields are filled

        # Convert expiration option into seconds
        expiration_map = {
            "1 minute": 60,
            "5 minutes": 5 * 60,
            "30 minutes": 30 * 60,
            "1 hour": 60 * 60,
            "5 hours": 5 * 60 * 60
        }
        expiration_seconds = expiration_map.get(expiration_option)
        expiration_time = int(time.time()) + expiration_seconds

        # Generate a short URL
        short_identifier = ShortUUID().random(length=6)
        short_url = request.host_url.rstrip('/') + '/' + short_identifier

        # Store in database
        with sqlite3.connect(db_file) as conn:
            conn.execute("INSERT INTO links (original_url, short_url, expiration) VALUES (?, ?, ?)",
                         (original_url, short_url, expiration_time))

        return redirect(url_for("index"))

    # Retrieve active links from the database
    with sqlite3.connect(db_file) as conn:
        cur = conn.execute("SELECT id, short_url, original_url FROM links WHERE expiration > ?",
                           (int(time.time()),))
        links = [{"id": row[0], "short_url": row[1], "original_url": row[2]} for row in cur.fetchall()]

    return render_template("index.html", links=links)

@app.route("/<short_identifier>")
def redirect_to_url(short_identifier):
    with sqlite3.connect(db_file) as conn:
        cur = conn.execute("SELECT original_url FROM links WHERE short_url LIKE ? AND expiration > ?", 
                           (f"%/{short_identifier}", int(time.time())))
        result = cur.fetchone()
        if result:
            return redirect(result[0])  # Redirect to the original URL
    return "URL not found or expired", 404

@app.route("/delete/<int:link_id>", methods=["POST"])
def delete_link(link_id):
    with sqlite3.connect(db_file) as conn:
        conn.execute("DELETE FROM links WHERE id = ?", (link_id,))
    return redirect(url_for("index"))

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
