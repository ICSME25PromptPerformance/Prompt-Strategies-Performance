class SQLGenerator:
    def __init__(self, table_name):
        self.table_name = table_name

    def select(self, fields=None, condition=None):
        fields_part = ', '.join(fields) if fields else '*'
        condition_part = f" WHERE {condition}" if condition else ''
        return f"SELECT {fields_part} FROM {self.table_name}{condition_part};"

    def insert(self, data):
        columns = ', '.join(data.keys())
        values = ', '.join(f"'{v}'" for v in data.values())
        return f"INSERT INTO {self.table_name} ({columns}) VALUES ({values});"

    def update(self, data, condition):
        set_part = ', '.join(f"{k} = '{v}'" for k, v in data.items())
        return f"UPDATE {self.table_name} SET {set_part} WHERE {condition};"

    def delete(self, condition):
        return f"DELETE FROM {self.table_name} WHERE {condition};"

    def select_female_under_age(self, age):
        return f"SELECT * FROM {self.table_name} WHERE age < {age} AND gender = 'female';"

    def select_by_age_range(self, min_age, max_age):
        return f"SELECT * FROM {self.table_name} WHERE age BETWEEN {min_age} AND {max_age};"