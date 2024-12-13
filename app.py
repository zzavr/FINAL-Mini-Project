from flask import Flask, render_template, request 
import psycopg2  

app = Flask(__name__)

conn = psycopg2.connect(
    host="postgres.cnq042mcc64k.eu-north-1.rds.amazonaws.com", 
    database="postgres",  
    user="postgres",  
    password="postgres"  
)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles requests to the homepage.
    - If GET: Displays the form for inputting the level.
    - If POST: Processes the form input, queries the database, and fetches courses for the given level.
    """
    courses = []  #an empty list to store course results
    if request.method == "POST":  # Check if the request is a POST
        level = request.form["level"]  
        with conn.cursor() as cur:  # Open a database cursor
            cur.execute(
                "SELECT course_name, day, time FROM timetable WHERE level = %s",  
                (level,)  
            )
            courses = cur.fetchall()  # Fetch all matching rows from the query result
    return render_template("index.html", courses=courses)

if __name__ == "__main__":
    """
    Run the Flask development server:
    - host="0.0.0.0": Makes the server accessible from any IP address.
    - port=8000: The server will listen on port 8000.
    - debug=True: Enables debug mode for easier development and troubleshooting.
    """
    app.run(host="0.0.0.0", port=8000, debug=True)
