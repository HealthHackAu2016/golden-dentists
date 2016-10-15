from flask import Flask, render_template, request
app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/procedure_lookup", methods=['GET', 'POST'])
def procedure_lookup():
    if request.method == 'POST':
        
        return render_template('procedure_lookup_results.html', 
                               procedure_code=request.form['procedure_code'],
                               procedure_name=request.form['procedure_name'])
    else:
        return render_template('procedure_lookup.html')

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

