import pytest
from main import BooksCollector

@pytest.fixture(scope='function')
def book(self):
    return BooksCollector()