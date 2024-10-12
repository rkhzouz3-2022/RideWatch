from flask import Flask, jsonify
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)


# # MySQL Configuration (update with your own credentials)
# app.config["MYSQL_HOST"] = "localhost"  # Use server IP if remote
# app.config["MYSQL_USER"] = "youruser"
# app.config["MYSQL_PASSWORD"] = "yourpassword"
# app.config["MYSQL_DB"] = "yourdatabase"  # Database name from MySQL Workbench
# app.config["MYSQL_CURSORCLASS"] = (
#     "DictCursor"  # Optional: returns results as dictionary
# )

# # Initialize MySQL connection
# mysql = MySQL(app)

@app.route("/")
def home():
    return {"thing" : ["Thing1", "Thing2", "Thing3"]}

@app.route("/users", methods=["GET"])
def get_users():
    ...
    # cursor = mysql.connection.cursor()
    # cursor.execute("SELECT * FROM users")  # Replace 'users' with your table name
    # rows = cursor.fetchall()
    # cursor.close()
    # return jsonify(rows)


if __name__ == "__main__":
    app.run(debug=True)
