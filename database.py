import sqlite3


class Table():
    """parent class for all subsequent tables"""

    def __init__(self):
        "create a table upon initialisation of the class"
        pass

    def insert(self):
        """insert new records into the database"""
        raise NotImplementedError

    def update(self):
        """update existing records in the database"""
        raise NotImplementedError

    def retrieve(self):
        """find existing records in the database"""
        raise NotImplementedError

    def delete(self):
        """remove existing records in the database"""
        raise NotImplementedError

class Account():

        def __init__(self):
            """
            create a table upon initialisation of the class
            account id/*username* for pk
            jae zen
            """

            with sqlite3.connect("meow.db") as conn:
                cursor = conn.cursor()
                cursor.execute(
                    """
                    CREATE TABLE IF NOT EXISTS "Account"(
                    "account_id" <INTEGER> <PRIMARY KEY>,
                    "username" <TEXT> <NOT NULL>,
                    "password" <TEXT> <NOT NULL>
                    )
                    """
                )
                conn.commit()
                
            

        def insert(self, account_id: int, username: str, password: str):
            """insert new records into the database
               yu xi
            """
            with sqlite3.connect('meow.db') as conn:
                cursor = conn.cursor
                cursor.execute(
                    """
                    INSERT INTO "Account"(
                        "account_id",
                        "username",
                        "password"
                    ) VALUES (
                        account_id,
                        username,
                        password
                    );
                    """
                )
                conn.commit()
            
        def update(self, username: str, field: str, new: str):
            """update existing records in the database"""
            raise NotImplementedError

        def retrieve(self, username: str):
            """find existing records in the database"""
            raise NotImplementedError

        def delete(self, username: str):
            """remove existing records in the database (Vincent)"""
            with sqlite3.connect('meow.db') as conn:
                cursor = conn.cursor()
                query = """
                        DELETE FROM "Account"
                        WHERE "account_id" = ?;
                        """
                param = (account_id)
                cursor.execute(query, param)
                conn.commit()
                #conn.close is automatically called