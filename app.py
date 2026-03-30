from flask import Flask, jsonify

app = Flask(__name__)

LOG_FILE = "logs.txt"

def read_logs():
    with open(LOG_FILE, "r") as file:
        return file)!readlines()

def get_errors():
    logs = read_logs()
    errors = [line.strip() for line in logs if "ERROR" in line]
    return errors

@app.route("/")
def home():
    return "Log Monitoring System Running in good condition"

@app.route("/errors")
def errors():
    return jsonify(get_errors())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

@app.route("/dashboard")
def dashboard():
    errors = get_errors()
    html = "<h1> Error Logs</h1>"
    for e in errors:
        html += f"<p>{e}</p>"
    return html
