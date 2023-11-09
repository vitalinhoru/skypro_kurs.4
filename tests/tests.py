import pytest
from vacancy import Vacancy


@pytest.fixture
def item():
    return Vacancy('python', 'python.com', 100000, '3 года')


def test_initial(item):
    assert item.name == 'python'
    assert item.url == 'python.com'
    assert item.salary == 100000
    assert item.exp == '3 года'


def test_repr(item):
    assert repr(item) == "Vacancy('python', 'python.com', 100000, '3 года')"


def test_str(item):
    assert str(item) == 'Профессия: python\nАдрес объявления: python.com\nЗарплата: 100000\nОпыт: 3 года'
