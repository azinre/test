# features/steps/load_steps.py
from behave import given
from app import products, Product  # Assuming you have a Product model in your app

@given('the following products exist in the system')
def step_impl(context):
    """
    Given step to load predefined products into the system before running tests.
    """
    # Clear existing products
    products.clear()

    # Load data from the feature file's table
    for row in context.table:
        product_id = int(row['id'])
        name = row['name']
        category = row['category']
        available = row['available'] == 'True'  # Convert string to boolean
        product = Product(product_id, name, category, available)
        products.append(product)

    # Optionally, log the products loaded
    print(f"Loaded products: {products}")
