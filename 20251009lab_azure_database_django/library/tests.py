from django.test import TestCase
from .models import Book


class BookModelTest(TestCase):
    def test_create_book(self):
        b = Book.objects.create(name='Dune', author='Frank Herbert', publication_year=1965)
        self.assertEqual(str(b), 'Dune by Frank Herbert (1965)')
