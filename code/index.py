from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bill_lookup")
def bill_lookup():
    return render_template('bill_lookup.html')

@app.route("/area_lookup")
def area_lookup():
    return render_template('area_lookup.html')

@app.route("/dentist_lookup")
def dentist_lookup():
    return render_template('dentist_lookup.html')

if __name__ == "__main__":
    app.run()

