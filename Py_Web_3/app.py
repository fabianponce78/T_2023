'''
Created on Feb 8, 2023

@author: fponce
'''
from flask import Flask, render_template, request
#from flask import request
#from aiohttp.client import request
from datetime import datetime, date
import pyodbc 

app = Flask(__name__)

lst_Form = []

#===============================================================================
# # Creating simple Routes 
# @app.route('/test')
# def test():
#     return "Home Page"
# 
# @app.route('/test/about/')
# def about_test():
#     return "About Page"
#===============================================================================

# Routes to Render Something
@app.route('/')
def index():
    Var_title = "TiTuLo..."
    return render_template("index.html", title=Var_title)

@app.route('/about', strict_slashes=False)
def about():
    Var_name = ["xxx", "YYY", "ZZZ"]
    return render_template("about.html", names=Var_name)
    #return render_template("about.html")

#@app.route('/FormA', strict_slashes=False)
@app.route('/FormA', methods=['GET', 'POST'])
def FormA():
    title = "Form!"
    return render_template("FormA.html", title=title)


@app.route('/form', methods=['GET', 'POST'])
def form():
    Var_XXX = 'xxxxxxxxxxxxxxxxxxxxxxxx'
    dt_Now = date.today()
    print("Today's date:", dt_Now)
    First_Name = request.form.get("First_Name")
    Last_Name = request.form.get("Last_Name")
    email = request.form.get("email")
    title = "Thank You!"
    #return render_template("FormX.html", title=title, First_Name=First_Name, Last_Name=Last_Name, email=email)
    Var_name = ["xxx", "YYY", "ZZZ"]
    print('XXX? = ', Var_XXX)
    
    print('First_Name = ', First_Name)
    print('Last_Name = ', Last_Name)
    print('email = ', email)
    
    lst_Form.append(f"{dt_Now}|{First_Name}|{Last_Name}|{email}")
    
    Str_Result =   str(dt_Now) + '|' + First_Name + '|' + Last_Name  + '|' + email + '\n'
    
    #return render_template("form.html", title=title, names=Var_name, Var_XXX=Var_XXX , dt_Now=dt_Now, First_Name=First_Name, Last_Name=Last_Name, email=email)
    
    #var_Y = fn_Form_2_DataBase(lst_Form)
    #print('\t var_Y : ', var_Y)
    
    ############---------------------------------------------
    # current dateTime
    now = datetime.now()

    # convert to string
    #date_time_str = now.strftime("%Y-%m-%d %H:%M:%S")
    date_time_str = now.strftime("%Y-%m-%d_%H")
    date_time_str = now.strftime("%Y%m%d_%H")
    
    str_Log_FileName = "Log_" + str(date_time_str) + '.TXT'
    path_file = 'Log_Form/log.txt'
    path_file = 'Log_Form/' + str_Log_FileName

    try:
        with open(path_file, 'a') as f:
            #f.write('Create a new text file!')
            f.write(str(Str_Result))
            f.close()
    except FileNotFoundError:
        print("The 'docs' directory does not exist")
    
    ############---------------------------------------------
    ###############################################################################
    try:
        server = 'MDC-DCMW8C3' 
        database = 'DB_FP' 
        username = 'FP2' 
        password = 'N1rvana53120' 
                
        Query_SP_1 = 'insert into dbo.Flask_Form_A (STR_FORM) values (GETDATE())'
        Query_SP_1 = 'insert into dbo.Flask_Form_A (STR_FORM) values (\''+str(First_Name)+'\')'
        Query_SP_1 = 'insert into dbo.Flask_Form_A (STR_FORM) values (\''+str(Str_Result)+'\')'
        print('\t Query_SP_1 = ' , Query_SP_1)
        
        conn = pyodbc.connect('DRIVER={SQL Server};SERVER='+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+password+'')                
        cursor = conn.cursor()
        
        cursor.execute(Query_SP_1)
        conn.commit()
        conn.close()
    except AssertionError as error:
        print('... ', error)    
    ###############################################################################    
    
    
    return render_template("form.html", title=title, names=Var_name, Var_XXX=Var_XXX , dt_Now=dt_Now, lst_Form=lst_Form)
    
    

def fn_Form_2_DataBase(lst_Form):
    print('--fn_Form_2_DataBase--')
    print(lst_Form)
    
    var_Y = 1
    return var_Y


# Make sure this we are executing this file
if __name__ == '__main__':
    app.run(debug=True)