# class DataTable:
#     def __init__(self, name, categories):
#         self.name = name
#         self.categories = categories
#         self.data = {self.name: {cat: [] for cat in self.categories}}

#     def add_data(self, category, values):
#         if category in self.categories:
#             self.data[self.name][category].extend(values)
#         else:
#             print(f"Error: {category} is not a valid category.")

#     def print_table(self):
#         print(self.data)


# class TableCollection:
#     def __init__(self):
#         self.tables = {}

#     def add_table(self, table):
#         self.tables[table.name] = table

#     def get_table(self, table_name):
#         return self.tables.get(table_name)

#     def print_tables(self):
#         for table_name, table_instance in self.tables.items():
#             print(f"Table: {table_name}")
#             table_instance.print_table()


# tbl_categories = ['comunidad', 'primer nivel', 'segundo nivel', 'centros']

# my_tables = TableCollection()
# table_1 = DataTable("Region1", tbl_categories)
# table_1.add_data("comunidad", [10, 10])
# table_1.add_data("primer nivel", [10, 10])

# table_2 = DataTable("Region2", tbl_categories)
# table_2.add_data("comunidad", [20, 20])
# table_2.add_data("primer nivel", [20, 20])

# my_tables.add_table(table_1)
# my_tables.add_table(table_2)

# my_tables.get_table("Region2").data


