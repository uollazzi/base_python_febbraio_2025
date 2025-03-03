import sqlite3

# connesction string (stringa di connessione)
# è una stringa che contiente le informazione per collegarsi da un determinato db
# tipicamente contiene: indirizzo del db, username, password

# nel caso di sqllite serve solo l'indirizzo fisico del db

# Operazione CRUD
# Create
# Read
# Update
# Delete


def get_products():
    with sqlite3.connect("store.db") as conn:
        products = conn.execute(
            """
            SELECT p.id, p.name, p.price, p.stock, p.category_id , c.name
            FROM products p
            INNER JOIN categories c ON p.category_id = c.id
            """
        ).fetchall()  # seleziona tutte le righe e le colonne della tabella products

        return products


def add_product(name, price, stock):
    with sqlite3.connect("store.db") as conn:
        return conn.execute(
            "INSERT INTO products (name, price, stock) VALUES (?, ?, ?)",
            (name, price, stock),
        )


def delete_product(id):
    with sqlite3.connect("store.db") as conn:
        return conn.execute("DELETE FROM products WHERE id = ?", (id,))


def rename_product(id, new_name):
    with sqlite3.connect("store.db") as conn:
        return conn.execute("UPDATE products SET name = ? WHERE id = ?", (new_name, id))


def update_product_price(id, percent):
    with sqlite3.connect("store.db") as conn:
        return conn.execute(
            "UPDATE products SET price = price * (1 - ?) WHERE id = ?", (percent, id)
        )


def aumento_listino(percent):
    with sqlite3.connect("store.db") as conn:
        return conn.execute("UPDATE products SET price = price * (1 + ?)", (percent,))


def sell_product(id, qta):
    with sqlite3.connect("store.db") as conn:
        return conn.execute(
            "UPDATE products SET stock = stock - ? WHERE id = ?", (qta, id)
        )


# add_product("Bicchieri", 23.49, 10)
# add_product("Friggitrice", 69.49, 60)

# delete_product(4)

# rename_product(5, "Bottiglie")
sell_product(1, 5)

result = get_products()
for prodotto in result:
    print(f"{prodotto[5]} - {prodotto[1]} - prezzo {prodotto[2]}")
