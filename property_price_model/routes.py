from flask import render_template, redirect, flash, session
from property_price_model import app
from property_price_model.forms import PropertyInputForm


@app.route("/", methods=["GET", "POST"])
def index():
    form = PropertyInputForm()
    if form.validate_on_submit():
        flash("Property data input")
        session["pcode"] = form.pcode.label
        session["sqft"] = form.sqft.label
        session["beds"] = form.beds.label
        return redirect("/postcode_info")
    return render_template("index.html", title="Property Input", form=form)


@app.route("/postcode_info")
def postcode_info():
    return render_template("postcode_info.html")
