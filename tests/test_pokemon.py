from lib.pokemon import Pokemon

"""
Pokemon constructs with an id, name and type
"""
def test_pokemon_constructs():
    pokemon = Pokemon(1, "Bulbasaur", "earth")
    assert pokemon.id == 1
    assert pokemon.name == "Bulbasaur"
    assert pokemon.type == "earth"

"""
We can format pokemons to strings nicely
"""
def test_pokemons_format_nicely():
    pokemon = Pokemon(1, "Bulbasaur", "earth")
    assert str(pokemon) == "Pokemon(1, Bulbasaur, earth)"

"""
We can compare two identical pokemons
And have them be equal
"""
def test_pokemons_are_equal():
    pokemon1 = Pokemon(1, "Bulbasaur", "earth")
    pokemon2 = Pokemon(1, "Bulbasaur", "earth")
    assert pokemon1 == pokemon2

