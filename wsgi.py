from property_price_model import create_app, db
from property_price_model.models import Sale

app = create_app()


@app.shell_context_processor
def make_shell_context():
    return {"db": db, "Sale": Sale}


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
