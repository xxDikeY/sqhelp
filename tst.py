from main import *
import sqlite3

# database = sqHelp("test.db", tables_dict={"People" : {"id" : "int", "name" : "str"}}, build=True)

# print("done")


tables_dict={"People" : {    "id" : "int",    "name" : "str"},"Jobs" :{"id" : "int","people" : "text"}}

#sq = sqHelp("tst.db", tables_dict=tables_dict, build=True)
sq = sqHelp("tst.db", created=True)

