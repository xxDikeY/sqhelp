class TableNotFound(Exception):
    def __init__(self, message):
        self.table_name = message

    def __str__(self):
        return self.message