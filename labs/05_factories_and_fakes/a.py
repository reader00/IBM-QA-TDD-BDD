import factory


def get_name():
    name = factory.Faker('name')
    return name


get_name()
