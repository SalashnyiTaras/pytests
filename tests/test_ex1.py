import pytest


@pytest.fixture(scope="module")
def fixture_1():
    print('run-fixture-1')
    return 1


@pytest.fixture(scope="module")
def fixture_yield():
    print('starting Test phase')
    yield 6
    print('END TEST PHASE')


def test_example(fixture_1):
    print('run-fixture in test 1 ')
    assert fixture_1 == 1


def test_example2(fixture_yield):
    print('run-fixture in test 1 ')
    assert fixture_yield == 6


def test_example82(fixture_yield):
    print('run-fixture in test 1 ')
    assert fixture_yield == 6

# @pytest.mark.slow
# def test_example():
#     assert 1 == 1
#
#
# def test_example3():
#     assert 1 == 1
#
#
# def test_example5():
#     assert 1 == 1
#
#
# def test_example55():
#     assert 1 == 1


# @pytest.mark.slow
# def test_example2():
#     print('some text')
#     assert 1 == 1