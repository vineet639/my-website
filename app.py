from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# Connect to MySQL
def get_data():
    conn = mysql.connector.connect(
        host="localhost",
        user="your_mysql_user",
        password="your_mysql_password",
        database="your_database_name"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")  # Change 'users' to your table name
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/')
def index():
    data = get_data()
    return render_template('index.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)
