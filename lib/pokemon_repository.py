from lib.pokemon import Pokemon

class PokemonRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from pokemons')
        pokemons = []
        for row in rows:
            item = Pokemon(row["id"], row["name"], row["type"])
            pokemons.append(item)
        return pokemons

    def find(self, id):
        rows = self._connection.execute('SELECT * FROM pokemons WHERE id=%s', [id])

        pokemon = Pokemon(rows[0]['id'], rows[0]['name'], rows[0]['type'])
        return pokemon