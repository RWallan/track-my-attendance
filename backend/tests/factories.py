import factory

from backend.database import models


class UserFactory(factory.Factory):
    class Meta:  # pyright: ignore
        model = models.User

    name = factory.Faker('text')
    course = factory.Faker('text')
    period = factory.Faker('text')
    email = factory.LazyAttribute(lambda obj: f'{obj.name}@test.com')
    password = factory.LazyAttribute(lambda obj: f'{obj.name}@test.com')
