from factory import Factory, Faker # type: ignore

class ProductFactory(Factory):
    class Meta:
        model = dict  # Example: replace with your actual Product model

    id = Faker("uuid4")
    name = Faker("word")
    category = Faker("word")
    availability = Faker("boolean")
    price = Faker("random_number", digits=5)
