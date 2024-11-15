def test_read_product():
    product = ProductFactory()
    product["name"] = "Updated Name"
    assert product["name"] == "Updated Name"