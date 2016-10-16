from flask import Flask, render_template, request
from flaskext.mysql import MySQL
 
mysql = MySQL()
app = Flask(__name__)
app.config['DEBUG'] = True

app.config['MYSQL_DATABASE_USER'] = 'gareth'
app.config['MYSQL_DATABASE_PASSWORD'] = 'test'
app.config['MYSQL_DATABASE_DB'] = 'dentists'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/procedure_lookup", methods=['GET', 'POST'])
def procedure_lookup():
    if request.method == 'POST':
        
        procedure_code = request.form['procedure_code']
        procedure_name=request.form['procedure_name']
        
        if procedure_code:
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT * from invoices where code='" + procedure_code + "'")
            inv = cursor.fetchall()
        elif procedure_name:
            pass
        
        return render_template('procedure_lookup_results.html')
    else:
        return render_template('procedure_lookup.html')


@app.route('/area_lookup', methods=['GET', 'POST'])
def area_lookup():
    if request.method == 'POST':
        
        postcode = request.form['postcode']
        
        if postcode:
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT * from dentists where postcode='" + postcode + "'")
            dentists = cursor.fetchall()
            
            if dentists:
                final_dentists = []
                
                for d in dentists:
                    cursor.execute("SELECT ROUND(AVG(price)) from invoices where dentist='" + d[0] + "'")
                    d = d + cursor.fetchone()
                    final_dentists.append(d)
            else:
                final_dentists = -1
        else:
            final_dentists = None
        
        return render_template('area_lookup_results.html', 
                               dentists=final_dentists)
    else:
        return render_template('area_lookup.html')


@app.route('/dentist_lookup', methods=['GET', 'POST'])
def dentist_lookup():
    if request.method == 'POST':
        
        dentist_name=request.form['dentist_name']
        
        if dentist_name:
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT * from dentists where name='" + dentist_name + "'")
            dentist = cursor.fetchone()
            
            if dentist:
                cursor.execute("SELECT ROUND(AVG(price)) from invoices where dentist='" + dentist[0] + "'")
                avg_cost = cursor.fetchone()
            else:
                dentist = -1
                avg_cost = [0]
        else:
            dentist = None
            avg_cost = [0]
                
        return render_template('dentist_lookup_results.html', 
                               dentist=dentist,
                               avg_cost=avg_cost[0])
    else:
        return render_template('dentist_lookup.html')
    



if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080)








