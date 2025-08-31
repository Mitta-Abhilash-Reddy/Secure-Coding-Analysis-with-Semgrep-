from flask import Flask, request
import subprocess
import sqlite3
import yaml

app = Flask(__name__)

@app.route('/ping')
def ping():
    host = request.args.get('host', '127.0.0.1')
    # BAD: shell=True enables command injection
    output = subprocess.check_output(f"ping -c 1 {host}", shell=True)    
    return output

@app.route('/search')
def search():
    q = request.args.get('q', '')
    conn = sqlite3.connect('users.db')
    cur = conn.cursor()
    # BAD: Unsafe f-string SQL -> injection
    cur.execute(f"SELECT * FROM users WHERE name = '{q}'")
    rows = cur.fetchall()
    return str(rows)

@app.route('/eval')
def eval_route():
    code = request.args.get('code', '1+1')
    # BAD: eval on untrusted input
    return str(eval(code))

def load_config(yaml_str):
    # BAD: yaml.load without SafeLoader is unsafe
    return yaml.load(yaml_str)

if __name__ == "__main__":
    app.run(debug=True)
