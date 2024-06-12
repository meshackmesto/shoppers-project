from models.__init__ import CURSOR, CONN

class Sales:

    all = {}

    def __init__(self, product_id, customer_id, quantity, date, id=None):
        self.id = id
        self.product_id = product_id
        self.customer_id = customer_id
        self.quantity = quantity
        self.date = date

    def __repr__(self):
        return f"<Sales {self.id}: Product {self.product_id}, Customer {self.customer_id}, Quantity {self.quantity}, Date {self.date}>"

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS sales (
            id INTEGER PRIMARY KEY,
            product_id INTEGER,
            customer_id INTEGER,
            quantity INTEGER,
            date TEXT,
            FOREIGN KEY (product_id) REFERENCES products(id),
            FOREIGN KEY (customer_id) REFERENCES customers(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS sales;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO sales (product_id, customer_id, quantity, date)
            VALUES (?, ?, ?, ?)
        """
        CURSOR.execute(sql, (self.product_id, self.customer_id, self.quantity, self.date))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, product_id, customer_id, quantity, date):
        sales = cls(product_id, customer_id, quantity, date)
        sales.save()
        return sales

    def update(self):
        sql = """
            UPDATE sales
            SET product_id = ?, customer_id = ?, quantity = ?, date = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.product_id, self.customer_id, self.quantity, self.date, self.id))
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM sales
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        sales = cls.all.get(row[0])
        if sales:
            sales.product_id = row[1]
            sales.customer_id = row[2]
            sales.quantity = row[3]
            sales.date = row[4]
        else:
            sales = cls(row[1], row[2], row[3], row[4])
            sales.id = row[0]
            cls.all[sales.id] = sales
        return sales

    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM sales
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT *
            FROM sales
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_product_id(cls, product_id):
        sql = """
            SELECT *
            FROM sales
            WHERE product_id = ?
        """
        rows = CURSOR.execute(sql, (product_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_customer_id(cls, customer_id):
        sql = """
            SELECT *
            FROM sales
            WHERE customer_id = ?
        """
        rows = CURSOR.execute(sql, (customer_id,)).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    def product(self):
        from models.products import Product
        return Product.find_by_id(self.product_id)

    def customer(self):
        from models.customer import Customer
        return Customer.find_by_id(self.customer_id)
