# lib/models/product.py
from models.__init__ import CURSOR, CONN

class Product:

    all = {}

    def __init__(self, name, description, price, stock, id=None):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock

    def __repr__(self):
        return f"<Product {self.id}: {self.name}, {self.description}, {self.price}, {self.stock}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name):
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, description):
        if isinstance(description, str) and len(description):
            self._description = description
        else:
            raise ValueError("Description must be a non-empty string")

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, (int, float)) and price > 0:
            self._price = price
        else:
            raise ValueError("Price must be a positive number")

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        if isinstance(stock, int) and stock >= 0:
            self._stock = stock
        else:
            raise ValueError("Stock must be a non-negative integer")

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS products (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT,
            price REAL,
            stock INTEGER
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS products;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO products (name, description, price, stock)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.name, self.description, self.price, self.stock))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, name, description, price, stock):
        product = cls(name, description, price, stock)
        product.save()
        return product

    def update(self):
        sql = """
            UPDATE products
            SET name = ?, description = ?, price = ?, stock = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.description, self.price, self.stock, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM products
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        product = cls.all.get(row[0])
        if product:
            product.name = row[1]
            product.description = row[2]
            product.price = row[3]
            product.stock = row[4]
        else:
            product = cls(row[1], row[2], row[3], row[4])
            product.id = row[0]
            cls.all[product.id] = product
        return product

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM products
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM products
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = """
            SELECT *
            FROM products
            WHERE name = ?
        """
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None
