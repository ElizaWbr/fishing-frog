import sqlite3

class DBProxy:
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.connection = sqlite3.connect(db_name)
        self.connection.execute('''
                                   CREATE TABLE IF NOT EXISTS fishes(
                                   fish_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                   name TEXT NOT NULL,
                                   fished INTEGER NOT NULL)
                                '''
                                )

    def save(self, name: str):
        added = self.retrieve_fish(name)
        if added:
            added_id, fished = added[0]
            self.update(added_id, fished)
        else:
            self.add(name)

    def add(self, name: str):
        self.connection.execute(f'INSERT INTO fishes (name, fished) VALUES ("{name}", 1)')
        self.connection.commit()

    def update(self, fish_id, fished):
        fished = fished + 1
        self.connection.execute(f'UPDATE fishes SET fished = "{fished}" WHERE fish_id = "{fish_id}"')
        self.connection.commit()

    def retrieve_fish(self, name: str):
        return self.connection.execute(f'SELECT fish_id, fished FROM fishes WHERE name = "{name}"').fetchall()

    def retrieve_all_fishes(self) -> list:
        return self.connection.execute('SELECT * FROM fishes ORDER BY fished DESC').fetchall()

    def close(self):
        return self.connection.close()
