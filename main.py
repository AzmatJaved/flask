from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home.html")

@app.route("/contact")
def contact_us():
    return render_template("contact.html")

@app.route("/getpost", methods = ["GET", "POST"])
def get_post():
    print(request.method) 
    print(request.form)
    if (request.method == "POST"):
        #handle the form
        with open("file.txt", 'a') as f: 
            f.write(f"the name is {request.form['name']} & email is {request.form['email']} \n")
        return render_template("get_post_request.html")

app.run(debug=True)