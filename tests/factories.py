import factory
from django.contrib.auth.models import User
from factory import Faker

# fake = Faker()
from core.app1.models import Category, Product


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    # username = 'Tarik'
    # first_name = 'Salik'
    # email = 'sharik@gmail.com'
    # TODO: to fix problem with fake
    # username = fake.name()
    # is_staff = True


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = 'django'


class ProductFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Product

    title = 'any_title'
    category = factory.SubFactory(CategoryFactory)  # simulates foreign key relation
    description = 'any_description'
    slug = 'any_slug'
    regular_price = '9'
    discount_price = '5'
