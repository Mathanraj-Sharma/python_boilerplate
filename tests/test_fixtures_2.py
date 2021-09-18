import pytest

def test_account_empty_from_diff_module(empty_account):
    print("\ntesting empty_account from diff module, since this fixture is session scoped not created again")
    assert empty_account.peek_balance() == 0


def test_account_20_from_diff_module_1(account_20):
    print("\ntesting account_20 from diff module, first call, since this fixture is module scoped created again for module 2")
    assert account_20.peek_balance() == 20


def test_account_20_from_diff_module_2(account_20):
    print("\ntesting account_20 from diff module, second call, within module 2 fixture not created again")
    assert account_20.peek_balance() == 20


def test_account_50_from_diff_module_1(account_50):
    print("\ntesting account_50 from diff module, first call")
    assert account_50.peek_balance() == 50


def test_account_50_from_diff_module_2(account_50):
    print("\ntesting account_50 from diff module, second call")
    assert account_50.peek_balance() == 50
