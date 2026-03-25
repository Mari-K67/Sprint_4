import pytest
from origin_class import BooksCollector

@pytest.fixture(scope='function')
def book(self):
    return BooksCollector()