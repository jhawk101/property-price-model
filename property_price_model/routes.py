from property_price_model import app

@app.route("/")
@app.route("/index")
def index():
    return "Hello Crev"