import requests
from flask import render_template, request, redirect, url_for

##url = 'https://www.youtube.com/results?search_query=word+cookies+skip+levels'
##r = requests.get(url)
##print(r.cookies)
##
##
##data = [0]
##with open("test.txt", "w") as file:
##    file.write(str(data))
##
####with open("test.txt", "r") as file:
####    data2 = eval(file.readline())
##
### Let's see if data and types are same.
##print(data, type(data), type(data[0]))
####print(data2, type(data2), type(data2[0]))
##
##

def home():
    user_id = request.cookies.get('YourSessionCookie')
    if user_id:
        user = database.get(user_id)
        if user:
            # Success!
            return render_template('welcome.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))


def login():
    if request.method == "POST":
        # You should really validate that these fields
        # are provided, rather than displaying an ugly
        # error message, but for the sake of a simple
        # example we'll just assume they are provided

        user_name = request.form["name"]
        password = request.form["password"]
        user = db.find_by_name_and_password(user_name, password)

        # Note we don't *return* the response immediately
        response = redirect(url_for("do_that"))
        response.set_cookie('YourSessionCookie', user.id)
        return response


def do_that():
    user_id = request.cookies.get('YourSessionCookie')
    if user_id:
        user = database.get(user_id)
        if user:
            # Success!
            return render_template('do_that.html', user=user)
        else:
            return redirect(url_for('login'))
    else:
        return redirect(url_for('login'))
