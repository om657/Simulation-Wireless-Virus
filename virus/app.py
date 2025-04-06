# app.py
from flask import Flask, render_template, jsonify
from virus_sim import infected_devices, start_simulation

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/infected')
def get_infected():
    return jsonify(infected_devices)

if __name__ == "__main__":
    start_simulation()  # Start infection thread
    app.run(debug=True)
