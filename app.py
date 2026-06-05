from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS

import pymysql

app = Flask(__name__)

CORS(app)

DB_HOST = "10.0.21.197" # Replace with your MySQL server's IP address
DB_USER = "edulearnuser"
DB_PASSWORD = "Password123!"
DB_NAME = "edulearn"


@app.route("/")
def home():
    return "EduLearn API is running"


@app.route("/health")
def health():
    return "healthy"


@app.route("/testdb")
def testdb():

    try:

        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO registrations
        (
            fullname,
            email,
            phone,
            course,
            experience,
            comments
        )
        VALUES
        (
            'Test User',
            'test@test.com',
            '123456789',
            'AWS',
            'Beginner',
            'Connectivity Test'
        )
        """)

        conn.commit()

        cursor.close()
        conn.close()

        return "Database connection successful. Record inserted."

    except Exception as e:

        return f"Database Error: {str(e)}"


@app.route('/api/register', methods=['POST'])
def register():

    try:

        data = request.json

        conn = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )

        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO registrations
        (
            fullname,
            email,
            phone,
            course,
            experience,
            comments
        )
        VALUES
        (%s,%s,%s,%s,%s,%s)
        """,
        (
            data['fullname'],
            data['email'],
            data['phone'],
            data['course'],
            data['experience'],
            data['comments']
        ))

        conn.commit()

        cursor.close()
        conn.close()

        return jsonify({
            "message": "Registration submitted successfully"
        })

    except Exception as e:

        return jsonify({
            "message": str(e)
        }), 500


if __name__ == '__main__':

    app.run(
        host='0.0.0.0',
        port=5000
    )