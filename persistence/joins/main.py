import database as database


def menu():
    # display menu options and return integer
    print("""
    Please select one of the following options:
    [1] Display stock levels
    [2] Display suppliers
    [3] Display supplier locations
    [4] Display missing suppliers
  
    Your selection:
    """)
    response = int(input())
    return response


def run():
    response = menu()
    if response == 1:
        database.display_products_with_stock_levels()
    elif response == 2:
        database.display_product_supplier()
    elif response == 3:
        database.display_product_supplier_locations()
    elif response ==4:
        database.display_products_missing_suppliers()
    else:
        print("Invalid selection")


if __name__ == "__main__":
    run()
