from flask import Flask, render_template, session, request, redirect
from flask_app import app
from flask_app.models.cookie_order import Cookies

@app.route("/")

@app.route("/cookies")
def index():
    cookies = Cookies.get_all()
    return render_template("index.html", cookies=cookies)

@app.route("/cookies", methods=["POST"])
def create_cookie():
    cookie_order = request.form
    if not Cookies.is_valid(cookie_order):
        return redirect('/cookies/add')
    Cookies.save_cookie(cookie_order)
    return redirect("/")

@app.route("/cookies/add")
def new_order():
    return render_template("new_order.html")

@app.route('/cookies/edit/<int:cookie_id>')
def edit(cookie_id):
    cookie_order = Cookies.get_by_id(cookie_id)
    return render_template("change_order.html", cookie_order= cookie_order)

@app.route("/cookies/edit/<int:cookie_id>", methods=["POST"])
def change_order(cookie_id):
    cookie_order = request.form
    if not Cookies.is_valid(cookie_order):
        return redirect(f"/cookies/edit/{cookie_id}")
    Cookies.update(cookie_order)
    return redirect('/')

@app.route('/cookies/delete/<int:id>')
def delete(id):
    data={
        "id": id
    }
    Cookies.destroy(data)
    return redirect('/')

