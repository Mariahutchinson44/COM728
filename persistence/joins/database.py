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

def display_product_supplier():
    # display each product with its supplier
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id"

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()
    print("The suppliers for each product are as follows:")

    for record in records:
        print(f"""
        Product: {record[0]}, Supplier: {record[1]}
        """)


def display_product_supplier_locations():
    # display each product with its supplier and location
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name, city, country " \
          "FROM product " \
          "INNER JOIN supplier ON product.supplier_id = supplier.id, " \
          "location ON supplier.location_id = location.id"

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()
    print("The suppliers for each product are as follows:")

    for record in records:
        print(f"""
        Product: {record[0]}, Supplier: {record[1]}, Supplier Location: {record[2]}, {record[3]}
        """)

def display_products_missing_suppliers():
    # display each product with its supplier
    # use left outer join
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name " \
          "FROM product " \
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.id" \

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()
    print("The suppliers for each product are as follows:\n")

    for record in records:
        print(f"Product: {record[0]}, Supplier: {record[1]}")

def display_suppliers_missing_products():
    # display each product with its supplier
    # use right outer join
    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON product.supplier_id = supplier.id" \

    cursor.execute(sql)
    records = cursor.fetchall()
    db.close()
    print("The suppliers for each product are as follows:\n")

    for record in records:
        print(f"Supplier: {record[1]}, Product: {record[0]}")


def display_missing_data():
    # display products and supplier names that are missing data
    # use full outer join

    db = sqlite3.connect("catalogue.db")
    cursor = db.cursor()
    sql = "SELECT product.name, supplier.name " \
          "FROM product " \
          "LEFT OUTER JOIN supplier ON product.supplier_id = supplier.id " \
          "UNION " \
          "SELECT product.name, supplier.name " \
          "FROM supplier " \
          "LEFT OUTER JOIN product ON product.supplier_id = supplier.id "


    cursor.execute(sql)
    records = cursor.fetchall()

    db.close()

    for record in records:
        if record[1] == None:
            print(f"The following products are missing suppliers: {record[0]}\n")
        elif record[0] == None:
            print(f"The following suppliers are missing products: {record[1]}\n")


    #     if record[0] == None:
    #         print(f"The following locations are not associated with a supplier: {record[1]}, {record[2]}")


    # print(f"The following locations are not associated with a supplier: {record[2]}, {record[3]}")

