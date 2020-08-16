import pandas as pd
from sqlalchemy import create_engine


def load_file(filepath, remove_columns=[], date_columns=[]):
    df = pd.read_csv(filepath)

    if remove_columns:
        df = df.drop(remove_columns, axis=1)

    if date_columns:
        for col in date_columns:
            df[col] = pd.to_datetime(df[col])

    df[["incode", "outcode"]] = df.postcode.str.split(" ", expand=True)

    engine = create_engine("sqlite:///app.db")
    df.to_sql(name="sale", con=engine, if_exists="append", index=False)

    print("File loaded into db")


def execute_query(query):
    engine = create_engine("sqlite:///app.db")
    conn = engine.raw_connection()
    cursor = conn.cursor()
    cursor.execute(query)
    conn.commit()


if __name__ == "__main__":
    load_file(
        "property_price_model/notebooks/data/2020_sales.csv",
        ["placeholder1", "placeholder2"],
        ["date"],
    )
