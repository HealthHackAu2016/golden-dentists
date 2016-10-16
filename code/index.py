from flask import Flask, render_template, request, send_file
from flaskext.mysql import MySQL
import matplotlib.pyplot as plt
import numpy as np
 
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
    dentist = request.args.get('dentist', None)
    
    if request.method == 'POST':
        
        procedure_code = request.form['procedure_code']
        procedure_name=request.form['procedure_name']
        
        try:
            dentist=request.form['dentist']
        except Exception:
            pass
        
        if not procedure_code and not procedure_name:
            return render_template('procedure_lookup_results.html',
                       procedure_code=None,
                       procedure_name=None)
        
        if not procedure_code:
            if procedure_name:
                cursor = mysql.connect().cursor()
                cursor.execute("SELECT code from items where description='" + procedure_name + "'")
                procedure_code = cursor.fetchone()
                
                if not procedure_code:
                    return render_template('procedure_lookup_results.html',
                       procedure_code=None,
                       procedure_name=-1)
                else:
                    procedure_code = procedure_code[0]
        
        if procedure_code:
            # Lookup name in db regardless of whether provided.
            cursor = mysql.connect().cursor()
            cursor.execute("SELECT description from items where code='" + procedure_code + "'")
            procedure_name = cursor.fetchone()
            
            if not procedure_name:
                procedure_code=-1
                procedure_name=None
                return render_template('procedure_lookup_results.html',
                       procedure_code=procedure_code,
                       procedure_name=procedure_name)
            else:
                procedure_name = procedure_name[0]
                
                cursor = mysql.connect().cursor()
                cursor.execute("SELECT ROUND(AVG(price)), MIN(price), MAX(price) from invoices where code='" + procedure_code + "'")
                average_price, min_price, max_price = cursor.fetchone()
                
                if dentist:
                    cursor.execute("SELECT ROUND(AVG(price)), MIN(price), MAX(price) from invoices where code='" + procedure_code + "' AND dentist='" + dentist + "'")
                    dentist_average_price, dentist_min_price, dentist_max_price = cursor.fetchone()
                else:
                    dentist_average_price = None
                    dentist_min_price = None
                    dentist_max_price = None
        
        return render_template('procedure_lookup_results.html',
                               procedure_code=procedure_code,
                               procedure_name=procedure_name,
                               average_price=average_price,
                               min_price=min_price,
                               max_price=max_price,
                               dentist=dentist,
                               dentist_average_price=dentist_average_price, 
                               dentist_min_price=dentist_min_price, 
                               dentist_max_price=dentist_max_price)
    else:
        return render_template('procedure_lookup.html',
                               dentist=dentist)


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
    

@app.route('/fig/<procedure_code>')
def figure(procedure_code):
    return ('', 204)
    
    '''
    cursor = mysql.connect().cursor()
    cursor.execute("SELECT price FROM invoices where code='" + procedure_code + "'")
    prices = cursor.fetchall()
    
    prices2 = []
    
    for price in prices:
        prices2.append(price[0])
    
    fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))

    
    # rectangular box plot
    bplot1 = axes[0].boxplot(prices2,
                             vert=True,   # vertical box aligmnent
                             patch_artist=True)   # fill with color

    # notch shape box plot
    bplot2 = axes[1].boxplot(prices2,
                             notch=True,  # notch shape
                             vert=True,   # vertical box aligmnent
                             patch_artist=True)   # fill with color
    
    # fill with colors
    colors = ['pink', 'lightblue', 'lightgreen']
    for bplot in (bplot1, bplot2):
        for patch, color in zip(bplot['boxes'], colors):
            patch.set_facecolor(color)
    
    # adding horizontal grid lines
    for ax in axes:
        ax.yaxis.grid(True)
        ax.set_xticks([y+1 for y in range(len(prices2))], )
        ax.set_xlabel('xlabel')
        ax.set_ylabel('ylabel')
    
    # add x-tick labels
    plt.setp(axes, xticks=[y+1 for y in range(len(prices2))],
             xticklabels=['x1', 'x2', 'x3', 'x4'])
    
    
    return send_file(plt, mimetype='image/png')
    '''

if __name__ == "__main__":
    app.run(host= '0.0.0.0', port=8080)








