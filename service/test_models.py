from factories import Factory, Faker
from factories import ProductFactory

def test_read_product():
    product = ProductFactory()
    assert product["name"] == "Some Name"  
    
def test_update_product():
    product = ProductFactory()
    product["name"] = "Updated Name"
    assert product["name"] == "Updated Name"
    
def test_delete_product():
    product = ProductFactory()
    del product
    assert product is None  
    
def test_search_by_name():
    product = ProductFactory(name="Test Product")
    assert product["name"] == "Test Product"    