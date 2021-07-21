import pytest


class TestUser:
    """writing tests using factoryboy"""

    def test_username(self, new_user):
        print('for efficient use of factory boy we can combine it with fixture.')
        print('One for instance can create a user and return him')
        assert new_user.username == 'Tarik'

    def test_first_name(self, new_user):
        print('for efficient use of factory boy we can combine it with fixture.')
        print('One for instance can create a user and return him')
        assert new_user.first_name == 'Salik'

    def test_user_email(self, new_user):
        print('for efficient use of factory boy we can combine it with fixture.')
        print('One for instance can create a user and return him')
        assert new_user.email == 'sharik@gmail.com'

    def test_superuser_username(self, new_super_user):
        print('sergey, a u drunk???')
        assert new_super_user.first_name == 'Pytester'

    def test_superuser(self, new_super_user):
        new_super_user.is_superuser = True
        assert new_super_user.is_superuser


class TestModelWithForeignKey:

    def test_new_product_description(self, product_factory):
        assert product_factory.description == 'any_description'

    # def test_new_product_category(self, product_factory):
    #     assert product_factory.category == 'django'

    def test_new_product_slug(self, product_factory):
        assert product_factory.slug == 'any_slug'

    def test_new_product_regular_price(self, product_factory):
        assert product_factory.regular_price == '9'

    def test_new_product_discount_price(self, product_factory):
        assert product_factory.discount_price == '5'

    def test_new_product_title(self, product_factory):
        assert product_factory.title == 'any_title'
