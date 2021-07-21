import pytest
from django.contrib.auth.models import User


@pytest.mark.django_db
def test_create_user():
    # @pytest.mark.django_db is used to simulate connection with database
    User.objects.create_user('test', 'test@test.com', 'test')
    count = User.objects.all().count()
    print(count, 'number of users')
    assert User.objects.count() == 1


@pytest.mark.django_db
def test_count_users():
    # database content will be cleaned after each test will be utilized
    res = User.objects.all().count()
    print(res)
    assert res == 0
