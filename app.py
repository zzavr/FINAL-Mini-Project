from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

# PostgreSQL connection
conn = psycopg2.connect(
    host="<RDS_Endpoint>",
    database="<Your_First_Name>",
    user="<RDS_User>",
    password="<RDS_Password>"
)

@app.route("/", methods=["GET", "POST"])
def index():
    courses = []
    if request.method == "POST":
        level = request.form["level"]
        with conn.cursor() as cur:
            cur.execute("SELECT course_name, day, time FROM timetable WHERE level = %s", (level,))
            courses = cur.fetchall()
    return render_template("index.html", courses=courses)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
