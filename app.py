from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
from settings import DATABASE_CONFIG

app = Flask(__name__)

# Database connection function
def get_db_connection():
    return mysql.connector.connect(**DATABASE_CONFIG)

# Home route
@app.route('/')
def index():
    connection = get_db_connection()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    employees = cursor.fetchall()
    cursor.close()
    connection.close()
    return render_template('index.html', employees=employees)

# Route to add a new employee
@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form.get('name')
    position = request.form.get('position')
    department = request.form.get('department')

    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO employees (name, position, department) VALUES (%s, %s, %s)",
                   (name, position, department))
    connection.commit()
    cursor.close()
    connection.close()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

