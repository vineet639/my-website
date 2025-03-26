from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def connect_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="ViNiT@Gmail1",
        database="my_database"
    )

# Home Route
@app.route('/')
def index():
    return render_template('index.html')

# Submit Route (Handles Form Submission)
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')

    if not name or not email:
        return "Error: Name and Email are required", 400

    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, email) VALUES (%s, %s)", (name, email))
    conn.commit()
    cursor.close()
    conn.close()

    return redirect('/')  # Redirect back to home page after submission

@app.route('/')
def index():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', data=data)


if __name__ == "__main__":
    app.run(debug=True)
