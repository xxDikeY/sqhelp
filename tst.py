from main import *
import sqlite3

database = SqHelp()
database.path = "test.db"

database.table_add("People")
database.column_add_int("id")
database.column_add_str("name")

database.create_table()

print("done")