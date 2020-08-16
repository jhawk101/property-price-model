from flask import render_template, redirect, flash, session, url_for
from flask import current_app as app
from property_price_model.forms import PropertyInputForm
from property_price_model.postcodes import get_clean_postcode
from property_price_model.models import Sale


@app.route("/", methods=["GET", "POST"])
def index():
    form = PropertyInputForm()
    if form.validate_on_submit():
        flash("Property data input")
        session["pcode"] = get_clean_postcode(form.data.get("pcode"))
        session["sqft"] = form.data.get("sqft")
        session["beds"] = form.data.get("beds")
        return redirect(url_for("postcode_info"))
    return render_template("index.html", title="Property Input", form=form)


@app.route("/postcode_info")
def postcode_info():
    session["incode"], session["outcode"] = session["pcode"].split(" ")
    sales = Sale.query.filter_by(incode=session["incode"])
    return render_template("postcode_info.html", sales=sales)
