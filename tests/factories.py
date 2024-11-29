from factory import Factory, Faker 

class ProductFactory(Factory):
    class Meta:
        model = dict  

    id = Faker("uuid4")
    name = Faker("word")
    category = Faker("word")
    availability = Faker("boolean")
    price = Faker("random_number", digits=5)
