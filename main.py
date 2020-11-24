import sqlite3


class DatabaseContextManager(object):
    def __init__(self, path):
        self.path = path

    def __enter__(self):
        self.connection = sqlite3.connect(self.path)
        self.cursor = self.connection.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.connection.commit()
        self.connection.close()


def create_table_companies():
    query = """CREATE TABLE IF NOT EXISTS Companies(
                company_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                address TEXT)"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


def create_table_customers():
    query = """CREATE TABLE IF NOT EXISTS Customers(
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                surname TEXT,
                company_id INTEGER,
                FOREIGN KEY (company_id) REFERENCES Companies(company_id))"""
    with DatabaseContextManager("db") as db:
        db.execute(query)


# ------------------------Companies CRUD------------------------



def create_company(name: str, address: str):
    query = """INSERT INTO Companies(name, address) VALUES(?, ?)"""
    parameters = [name, address]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)



def update_company_name(old_name: str, new_name: str):
    query = """UPDATE Companies
                SET name = ?
                WHERE name = ?"""
    parameters = [new_name, old_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_company(name: str):
    query = """DELETE FROM Companies
                WHERE name = ?"""
    parameters = [name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_companies():
    query = """SELECT * FROM Companies"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


def get_company_by_name(name: str):
    query = """SELECT * FROM Companies 
                WHERE name = ?"""
    parameters = [name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)
        return db.fetchone()


# ------------------------Customers CRUD------------------------



def create_customer(name: str, surname: str, company_id: int):
    query = """INSERT INTO Customers(name, surname, company_id) VALUES(?, ?, ?)"""
    parameters = [name, surname, company_id]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def update_customer_name(old_name: str, new_name: str):
    query = """UPDATE Customers
                SET name = ?
                WHERE name = ?"""
    parameters = [new_name, old_name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def delete_customer(name: str):
    query = """DELETE FROM Customers
                WHERE name = ?"""
    parameters = [name]
    with DatabaseContextManager("db") as db:
        db.execute(query, parameters)


def get_customers():
    query = """SELECT * FROM Customers"""
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


# ------------------------JOIN------------------------

def join_customers_companies():
    query = """SELECT * 
                FROM Customers 
                JOIN Companies 
                    ON Customers.company_id = Companies.company_id """
    with DatabaseContextManager("db") as db:
        db.execute(query)
        for record in db.fetchall():
            print(record)
    print("------------------------------------------------------")


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    create_table_companies()
    create_table_customers()

    create_company('Feniksas', 'Petrausko 5')
    create_company('IBM', 'Miško 12')

    create_customer('Jonas', 'Jonaitis', 123)
    update_customer_name('Jonas', 'Petras' )

    get_companies()
    get_customers()

    join_customers_companies()
