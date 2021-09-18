import pytest


from python_boilerplate.python_boilerplate import Account


@pytest.fixture(scope='session')
def empty_account():
    print("\nempty_account fixture created with session scope")
    return Account(0)


@pytest.fixture(scope='module')
def account_20():
    print("\naccount_20 fixture created with module scope")
    return Account(20)


@pytest.fixture
def account_50():
    print("\naccount_50 fixture created with function scope")
    return Account(50)