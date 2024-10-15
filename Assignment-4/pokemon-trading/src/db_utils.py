"""
SQL-Connector and all things DB go in here
"""
import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE


class DbConnectionError(Exception):
    pass


def _connect_to_db():
    cnx = mysql.connector.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        auth_plugin='mysql_native_password',
        database=DATABASE
    )
    return cnx


# Function to get all Pokémon cards from the database
def get_all_cards_db():
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        query = """SELECT * FROM cards"""
        cur.execute(query)
        result = cur.fetchall()  # List of records where each record is a tuple

        cur.close()
        return result

    except Exception as e:
        raise DbConnectionError(f"Failed to read data from DB: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Function to add a new Pokémon card to the database
def add_new_card_db(new_card_dict):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        print("ADD THIS CARD TO DB:", new_card_dict)

        query = f"""
         INSERT INTO cards (name, type, condition)
         VALUES ('{new_card_dict['name']}', '{new_card_dict['type']}', '{new_card_dict['condition']}')
         """

        # Execute the query
        cur.execute(query)

        # Commit the transaction to make the changes in the database
        db_connection.commit()

        print("Card added successfully!")

        # Optionally, retrieve all cards after adding
        cur.execute("""SELECT * FROM cards""")
        result = cur.fetchall()
        cur.close()

        return result

    except Exception as e:
        raise DbConnectionError(f"Failed to add card to DB: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


# Function to delete a Pokémon card by ID
def delete_card_by_id(card_id):
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print("Connected to DB: %s" % DATABASE)

        del_query = """DELETE FROM cards WHERE id = {}""".format(card_id)
        cur.execute(del_query)

        db_connection.commit()  # IMPORTANT!!! Commit the transaction to apply the deletion

        print(f"Record with card_id {card_id} deleted successfully.")

        # Optionally, retrieve all remaining cards after deletion
        cur.execute("SELECT * FROM cards")
        remaining_records = cur.fetchall()  # Get all remaining records
        cur.close()

        return remaining_records

    except Exception as e:
        raise DbConnectionError(f"Failed to delete card from DB: {e}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed")


if __name__ == "__main__":
    # Testing database connection
    # print("TESTING DB CONNECTION")
    # cards = get_all_cards_db()
    # print(cards)
    delete_card_by_id(1)  # Change ID as needed for testing
