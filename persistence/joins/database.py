import sqlite3

def display_products_with_stock_levels():
    # display each product with stock levels
    # use natural join
    # connect to database
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT name, description, quantity " \
          "FROM product " \
          "NATURAL JOIN stock"

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()
    # number of products in the catalogue.
    print(f"There are {len(records)} products in the catalogue")
    print("The stock level for each product is as follows:")

    for record in records:
        print(f"""
        Product: {record[0]}
        Description: {record[1]}
        Stock level: {record[2]}
        """)
