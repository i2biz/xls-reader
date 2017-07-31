# -*- coding: utf-8 -*-

import datetime
from decimal import Decimal
import pathlib
import typing
import unittest

from example_bindings import bindings


EXAMPLE_FILES = pathlib.Path(__file__).parent.absolute() / "example_files"



class SheetTestCase(unittest.TestCase):

  FILE_NAME: str = 'example1.xlsx'
  SHEET_NAME: str = None
  EXPECTED_OUTPUT: typing.List[dict] = None

  def setUp(self):
    if self.SHEET_NAME is None:
      raise unittest.SkipTest()
    self.file_path = EXAMPLE_FILES / self.FILE_NAME
    self.importer = bindings.ExampleDataImporter()

  def test_sheet(self):
    response = list(self.importer.read_file(str(self.file_path), self.SHEET_NAME))
    print(response)
    self.assertEqual(response, self.EXPECTED_OUTPUT)


class Sheet1Test(SheetTestCase):

  SHEET_NAME = "simple_sheet"
  EXPECTED_OUTPUT = [
    {
      'name': 'something', 'price': Decimal('1234'), 'location': bindings.Category.OFFICE,
      'description': 'Something', 'active': True, 'date_added': datetime.datetime(2014, 1, 12, 0, 0)
    },
    {
      'name': 'else', 'price': Decimal('43.312'), 'location': bindings.Category.WAREHOUSE,
      'description': 'else', 'active': False, 'date_added': datetime.datetime(2014, 1, 21, 0, 0)
    },
    {
      'name': 'entirely', 'price': Decimal('12.32'), 'location': bindings.Category.OFFICE,
      'description': 'and now', 'active': True, 'date_added': datetime.datetime(2000, 12, 12, 0, 0)
    }
  ]


class EmptyHeaderAndColumns(SheetTestCase):
    SHEET_NAME = "empty headers and columns"
    EXPECTED_OUTPUT = [
      {
        'name': 'something', 'price': Decimal('1234'), 'location': bindings.Category.OFFICE,
        'description': 'Something', 'active': True,
        'date_added': datetime.datetime(2014, 1, 12, 0, 0)
      },
      {
        'name': 'else', 'price': Decimal('43.312'), 'location': bindings.Category.WAREHOUSE,
        'description': 'else', 'active': False, 'date_added': datetime.datetime(2014, 1, 21, 0, 0)
      },
      {
        'name': 'entirely', 'price': Decimal('12.32'), 'location': bindings.Category.OFFICE,
        'description': 'and now', 'active': True,
        'date_added': datetime.datetime(2000, 12, 12, 0, 0)
      }
    ]


class MissingNotRequiredColumn(SheetTestCase):
  SHEET_NAME = "missing not required column"
  EXPECTED_OUTPUT = [
    {
      'name': 'something', 'price': Decimal('1234'), 'location': bindings.Category.OFFICE,
      'description': None, 'active': True,
      'date_added': datetime.datetime(2014, 1, 12, 0, 0)
    },
    {
      'name': 'else', 'price': Decimal('43.312'), 'location': bindings.Category.WAREHOUSE,
      'description': None, 'active': False, 'date_added': datetime.datetime(2014, 1, 21, 0, 0)
    },
    {
      'name': 'entirely', 'price': Decimal('12.32'), 'location': bindings.Category.OFFICE,
      'description': None, 'active': True,
      'date_added': datetime.datetime(2000, 12, 12, 0, 0)
    }
  ]


if __name__ == "__main__":
  unittest.main()

