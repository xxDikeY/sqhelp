import sqlite3


class SqHelp:
    path = ""
    table_current = ""
    tables_list = []
    columns_dict = {}

    #   Table methods
    #       Set

    def table_add(self, name: str):
        self.table_current = name
        self.tables_list.append(name)
        self.columns_dict[name] = {}

        return True

    def table_current_set(self, name: str):
        for def_name in self.tables_list:
            if name == def_name:
                self.table_current = name

                return True

        return False

    #       Get

    def table_get(self):
        return self.tables_list

    def table_current_get(self):
        return self.table_current

    #   Columns methods
    #       Set

    def column_add(self, name: str, type: str):
        if self.table_current == "":
            return False

        self.columns_dict[self.table_current][name] = type

        return True

    def column_add_int(self, name: str):
        if self.table_current == "":
            return False

        self.columns_dict[self.table_current][name] = "INTEGER"

        return True

    def column_add_str(self, name: str):
        if self.table_current == "":
            return False

        self.columns_dict[self.table_current][name] = "TEXT"

        return True

    def column_add_double(self, name: str):
        if self.table_current == "":
            return False

        self.columns_dict[self.table_current][name] = "REAL"

        return True

    def column_add_binary(self, name: str):
        if self.table_current == "":
            return False

        self.columns_dict[self.table_current][name] = "BLOB"

        return True

    #   Class methods

    def create_table(self):
        con = sqlite3.connect(self.path)
        cur = con.cursor()

        req = f"CREATE TABLE {self.table_current}("

        for key in self.columns_dict[self.table_current]:
            req += f"{key} {self.columns_dict[self.table_current][key]},"

        req = req[0: len(req) - 1]
        req += ");"

        cur.execute(req)
        con.commit()

        return True

