from flask import Flask, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from dotenv import load_dotenv
from os import environ
import MySQLdb.cursors

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:8081"}})

# MySQL Configuration (update with your own credentials)
app.config["MYSQL_HOST"] = environ.get("MYSQL_HOST", "localhost")
app.config["MYSQL_USER"] = environ.get("MYSQL_USER")
app.config["MYSQL_PASSWORD"] = environ.get("MYSQL_PASSWORD")
app.config["MYSQL_DB"] = environ.get("MYSQL_DB")
app.config["MYSQL_CURSORCLASS"] = ("DictCursor") #optional returning as dict

# Initialize MySQL connection
mysql = MySQL(app)

@app.route("/createAccount", methods=["GET"])
def validate_user():
    return jsonify({"thing" : ["Thing1", "Thing2", "Thing3"]})

# @app.route("/users", methods=["GET"])
# def get_users():
#     ...
#     # cursor = mysql.connection.cursor()
#     # cursor.execute("SELECT * FROM users")  # Replace 'users' with your table name
#     # rows = cursor.fetchall()
#     # cursor.close()
#     # return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)
