import pytest

@pytest.fixture
def clear_books_database() -> None:
    print('Clearing Books Database')


@pytest.fixture
def fill_books_database() -> None:
    print('Filling Books Database')


@pytest.mark.usefixtures('fill_books_database')
def test_read_all_books_in_library():
    print('Reading all books in library')


@pytest.mark.usefixtures(
    'clear_books_database',
    'fill_books_database'
)
class TestLibrary:
    def test_read_book_from_library(self):
        ...

    def test_delete_book_from_library(self):
        ...
