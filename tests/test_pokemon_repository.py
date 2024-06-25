from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon

"""
When we call PokemonRepository#all
We get a list of Pokemon objects reflecting the seed data.
"""
def test_get_all_records(db_connection): 
    db_connection.seed("seeds/pokemon_store.sql") 
    repository = PokemonRepository(db_connection) 

    pokemons = repository.all()

    assert pokemons == [
        Pokemon(1,'Bulbasaur', 'earth'),
        Pokemon(2,'Pikachu', 'electric'),
        Pokemon(3,'Mewtwo', 'psycho'),
        Pokemon(4,'Charizard', 'fire'),
        Pokemon(5,'Squirtle', 'water'),
    ]

"""
When we call PokemonRepository#find(id)
We get one Pokemon with an id.
"""
def test_get_one_record(db_connection): 
    db_connection.seed("seeds/pokemon_store.sql") 
    repository = PokemonRepository(db_connection) 

    pokemon = repository.find(1)

    assert pokemon.id == 1
    assert pokemon.name == 'Bulbasaur'
    assert pokemon.type == 'earth'

