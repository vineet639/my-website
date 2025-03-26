from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ViNiT@Gmail1",  # Move this to an environment variable in production!
        database="my_database"
    )

# Home Route - Fetch and Display Data
@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', data=data)

# Submit Route (Handles Form Submission)
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']

        if not name or not email:
            return "Error: Name and Email are required", 400

        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
        conn.commit()
        cursor.close()
        conn.close()

        return redirect('/')  # Redirect back to home page after submission

if __name__ == "__main__":
    app.run(debug=True)
