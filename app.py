from flask import Flask, render_template, request
import re
import math

app = Flask(__name__)

def calculate_entropy(password):
    if not password:
        return 0
    pool = set(password)
    entropy_per_char = math.log2(len(pool))
    total_entropy = entropy_per_char * len(password)
    return total_entropy

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        password = request.form['password']
       
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
