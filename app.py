import os
from flask import Flask, request, render_template, redirect, url_for,flash
import sqlite3

app= Flask(__name__)

import os.path

BASE_DIR = r"C:\Users\hp\Desktop"
db_path = os.path.join(BASE_DIR, "StudentDetails.db")

@app.route('/')
def form():
	return """
        <html>
            <body>
                <h1>Blood Donation</h1>

                <form action="/transform" method="post" enctype="multipart/form-data">
                    <input type="file" name="data_file" />
                    <input type="file" name="data_file2" />
                    <input type="submit" name="Submit" value="Submit" />
                </form>
                
            </body>
        </html>
    	"""
@app.route('/home', methods=['GET', 'POST'])
def home():
    error = None
    if request.method == 'POST':
        u_reg=request.form['reg']
        error = 'Invalid Credentials. Please try again.'
        #return redirect(url_for('home'))
        if(u_reg=='login'):
            return(render_template('login.html', error=error))
        else:
            return render_template('register.html', error=error)
    return render_template('home.html',error=error)

@app.route('/register', methods=['GET', 'POST'])
def register():
    #error = None
    if request.method == 'POST':
        u_fname=request.form['userfirstname']
        u_lname=request.form['userlastname']
        u_fathername=request.form['userfathername']
        u_mothername=request.form['usermothername']
        u_gender=request.form['usergender']
        u_dob=request.form['dob']
        u_phonenumber=request.form['phonenumber']
        u_bloodgroup=request.form['bloodgroup']
        u_email=request.form['email']
        u_password=request.form['password']
        u_address=request.form['address']
        u_city=request.form['city']
        u_state=request.form['state']
        u_country=request.form['country']
        u_pincode=request.form['pincode']
        u_rank=request.form['userrank']
        u_branch=request.form['userbranch']

        conn=sqlite3.connect(db_path)
        cur=conn.cursor()

        cur.execute("INSERT INTO Student(FirstName,LastName,FatherName,MotherName,Gender,DOB,PhoneNumber,BloodGroup,Email,Password,Address,City,State,Country,Pincode,Rank,Branch) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)",(u_fname,u_lname,u_fathername,u_mothername,u_gender,u_dob,u_phonenumber,u_bloodgroup,u_email,u_password,u_address,u_city,u_state,u_country,u_pincode,u_rank,u_branch))
        conn.commit()
        ID=cur.lastrowid
        print(ID)
        #flash("thanks for registering")
        return "Your UserId is "+str(ID)+" !\n Please write it somewhere."
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        u_name=request.form['userid']
        u_name=int(u_name)
        u_password=request.form['password']
        print("u_name=",u_name,"\n u_password=",u_password)
        
        conn=sqlite3.connect(db_path)
        cur=conn.cursor()
        cur.execute("SELECT StudentID,Password from Student where StudentID={}".format(u_name))
        data=cur.fetchall()
        for i in data:
            uid=i[0]
            upass=i[1]
            print(uid,upass)
        print(u_name == uid)
        print(u_password == upass)
        if((u_name == uid)and(u_password == upass)):
            print(u_name,"==",uid)
            print("select * from Student where StudentID={}".format(u_name))
            cur.execute("select * from Student where StudentID={}".format(u_name))
            data1=cur.fetchall()
            return render_template('detail.html',data1=data1)
    return render_template('login.html', error=error)



if __name__ == '__main__':
    app.run(debug=True)