# coding=utf-8


from xls_reader import *


def test_exception_string():
  class ExampleColumn(Column):
    TEST = ColumnDescription(
      regex="Name",  # Name is the column header
      reader=StringReader(attr_name="name")
    )

  exc = ColumnReadException(message="A message")
  exc.row = 1
  exc.column = "A1"
  exc.column_enum = ExampleColumn.TEST

  assert str(exc) == "('A message', 1, 'A1', Column.TEST)"
