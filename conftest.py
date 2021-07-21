import pytest
from django.contrib.auth.models import User
from pytest_factoryboy import register

from tests.factories import UserFactory, CategoryFactory, ProductFactory


# after factory was registered you can access it using following syntax: name_factory
register(UserFactory)
register(CategoryFactory)
register(ProductFactory)


@pytest.fixture
def new_user(db, user_factory):
    user = user_factory.create(
        username='Tarik',
        first_name='Salik',
        email='sharik@gmail.com', )
    return user


@pytest.fixture
def new_super_user(db, user_factory):
    user = user_factory.create(
        username='Tester',
        first_name='Pytester',)
    return user


@pytest.fixture
def new_modeluser_fk(db, product_factory):
    user = product_factory.create()
    return user


# @pytest.fixture
# def user_factory(db):
#     """ example of a factory in pytest"""
#     def create_user(username, password, first_name, is_staff=False, is_superuser=False, is_active=True):
#         user = User.objects.create_user(
#             username=username,
#             password=password,
#             first_name=first_name,
#             is_staff=is_staff,
#             is_superuser=is_superuser,
#             is_active=is_active,
#         )
#         return user
#     return create_user
#
#
# @pytest.fixture
# def new_user(db, user_factory):
#     return user_factory('Tarik', 'password', 'tarik-salik')
#
#
# @pytest.fixture
# def new_staff_user(db, user_factory):
#     return user_factory('Tarik', 'password', 'tarik-salik', is_staff=True)
#
#
# @pytest.fixture
# def new_super_user(db, user_factory):
#     return user_factory('password', 'Tarik', 'tarik-salik', is_staff=True, is_superuser=True)