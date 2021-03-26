import database as database


def menu():
    # display menu options and return integer
    print("""
    Please select one of the following options:
    [1] Display stock levels
    [2] Display suppliers
  
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
    else:
        print("Invalid selection")


if __name__ == "__main__":
    run()
