import sqlite3


class sqHelp:
    path = ""
    current_table = ""
    tables_list = []
    tables_dict = {}

    # not finished, need execptions
    def __init__(self, path: str, created: bool = False, tables_dict: dict = {}, build: bool = False):
        self.path = path

        if created:
            con = sqlite3.connect(self.path)
            cur = con.cursor()

            req = cur.execute("SELECT * FROM sqhelp")

            for line in req.fetchall():
                if not line[1] in self.tables_dict:
                    self.tables_list.append(line[1])
                self.tables_dict[line[1]] = {line[2] : line[3]}

            self.current_table = self.tables_list[0]


        if len(tables_dict) == 0:
            # exeption
            pass
        
        # done
        else:
            self.tables_dict = tables_dict
            

            for key in tables_dict:
                self.tables_list.append(key)

            self.current_table = self.tables_list[0]

            
            if build:
                con = sqlite3.connect(self.path)
                cur = con.cursor()

                cur.execute("DROP TABLE IF EXISTS sqhelp")
                cur.execute("CREATE TABLE sqhelp(id INTEGER PRIMARY KEY AUTOINCREMENT, table_name TEXT, column_name TEXT, column_type TEXT)")

                for table_name in self.tables_dict:
                    req = f"CREATE TABLE {table_name}("

                    for column_name in self.tables_dict[table_name]:
                        cur.execute(f"INSERT INTO sqhelp (table_name, column_name, column_type) VALUES ('{table_name}', '{column_name}', '{self.tables_dict[table_name][column_name]}')")
                        con.commit()

                        req += f"{column_name} {self.format_types(self.tables_dict[table_name][column_name])}, "

                    req = req[0: len(req) - 1]
                    req += ");"
                    
                    cur.execute(req)


                   
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

    #   Columns method
    #       Set

    # need execptions
    def add_column(self, name: str, type: str):
        if self.current_table == "":
            return False

        if type.lower() in ["int", "integer"]:
            self.tables_dict[self.current_table][name] = "INTEGER"

        elif type.lower() in ["str", "string", "text"]:
            self.tables_dict[self.current_table][name] = "TEXT"

        elif type.lower() in ["float", "double", "real"]:
            self.tables_dict[self.current_table][name] = "REAL"

        elif type.lower() in ["bin", "bit", "blob"]:
            self.tables_dict[self.current_table][name] = "BLOB"

        return True

    #   Class methodsa

    # not finished, need execptions
    def create_table(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()

        req = f"CREATE TABLE {self.current_table}("

        for key in self.tables_dict[self.current_table]:
            req += f"{key} {self.tables_dict[self.current_table][key]},"

        req = req[0: len(req) - 1]
        req += ");"

        cur.execute(req)

        return True
    
    #   Static methods
    #       Other

    def format_types(self, types : str):
        
        if types.lower() in ["int", "integer"]:
            return "INTEGER"
        
        elif types.lower() in ["str", "string", "text"]:
            return "TEXT"

        elif types.lower() in ["float", "double", "real"]:
            return "REAL"

        elif types.lower() in ["bin", "bit", "blob"]:
            return "BLOB"