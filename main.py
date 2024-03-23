import sqlite3


class sqHelp:
    path = ""
    current_table = ""
    tables_list = []
    tables_dict = {}

    # not finished, need execptions
    def __init__(self, path: str, created: bool = False, tables_dict: dict = {}, build: bool = False):
        self.path = path

        # fill
        if created:
            
            #return
            pass

        if len(tables_dict) == 0:
            #return False
            pass
        
        else:
            self.tables_dict = tables_dict

            for key in tables_dict:
                self.tables_list.append(key)

            if build:
                self.create_table()

            #return True
            
    

    #   Table methods
    #       Set

    def add_table(self, name: str):
        self.current_table = name
        self.tables_list.append(name)
        self.tables_dict[name] = {}

        return True

    # need execptions
    def set_current_table(self, name: str):
        for def_name in self.tables_list:
            if name == def_name:
                self.current_table = name

                return True

        return False

    #   Columns methods
    #       Set

    # need execptions
    def add_column(self, name: str, type: str):
        if self.current_table == "":
            return False

        if type.lower() == "int" or type.lower() == "integer":
            self.tables_dict[self.current_table][name] = "INTEGER"

        elif type.lower() == "str" or type.lower() == "string" or type.lower() == "text":
            self.tables_dict[self.current_table][name] = "TEXT"

        elif type.lower() == "float" or type.lower() == "double" or type.lower() == "real":
            self.tables_dict[self.current_table][name] = "REAL"

        elif type.lower() == "bin" or type.lower() == "bit" or type.lower() == "blob":
            self.tables_dict[self.current_table][name] = "BLOB"

        return True

    #   Class methodsa

    # not finished, need execptions
    def create_table(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()

        cur.execute("""CREATE TABLE IF NOT EXISTS sqhelp(id INTEGER PRIMARY KEY AUTOINCREMENT, table_name TEXT, column_name TEXT, column_type TEXT)""")

        # problem here
        for table_name in self.tables_dict:
            for column_name in table_name:
                cur.execute(f"INSERT INTO sqhelp (table_name, column_name) VALUES ('{table_name}', '{column_name}', '{table_name[column_name]}')")
                con.commit()

        req = f"CREATE TABLE {self.current_table}("

        for key in self.tables_dict[self.current_table]:
            req += f"{key} {self.tables_dict[self.current_table][key]},"

        req = req[0: len(req) - 1]
        req += ");"

        cur.execute(req)

        return True

# tables_dict={

#     "People" : 
#     {
#         "id" : "int",
#         "name" : "str"
#     },

#     "Jobs" :
#     {
#         "id" : "int",
#         "people" : "text"
#     }
# }
