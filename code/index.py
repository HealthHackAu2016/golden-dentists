from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/bill_lookup")
def bill_lookup():
    return render_template('bill_lookup.html')

@app.route("/area_lookup")
def area_lookup():
    return render_template('area_lookup.html')

@app.route('/dentist_lookup', methods=['GET', 'POST'])
def dentist_lookup():
    if request.method == 'POST':
        
        return render_template('dentist_lookup_results.html', 
                               fname=request.form['firstname'],
                               lname=request.form['lastname'])
    else:
        return render_template('dentist_lookup.html')


if __name__ == "__main__":
    app.run()

