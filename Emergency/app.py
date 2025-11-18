from flask import Flask, render_template, request, jsonify
import os
from datetime import datetime

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    if not (name and email and message):
        return jsonify(success=False, error='Missing fields'), 400

    os.makedirs('messages', exist_ok=True)
    fname = os.path.join('messages', 'contacts.txt')
    with open(fname, 'a', encoding='utf-8') as f:
        f.write(f"---\n{datetime.utcnow().isoformat()} UTC\n{name} <{email}>\n{message}\n")

    return jsonify(success=True)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
