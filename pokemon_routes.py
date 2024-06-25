from lib.database_connection import get_flask_database_connection
from lib.pokemon_repository import PokemonRepository
from lib.pokemon import Pokemon
from flask import request, render_template, redirect, url_for

def apply_pokemon_routes(app):
    @app.route('/api/pokemons', methods=['GET'])
    def get_pokemons():
        connection = get_flask_database_connection(app)
        pokemon_repository = PokemonRepository(connection)
        return pokemon_repository.all()

    @app.route('/pokemons', methods=['GET'])
    def pokemon_index():
        connection = get_flask_database_connection(app)
        pokemon_repository = PokemonRepository(connection)
        pokemons = pokemon_repository.all()
        return render_template('pokemons/index.html', pokemons=pokemons)

    @app.route('/pokemons/<int:id>', methods=['GET'])
    def get_pokemon_by_id(id):
        connection = get_flask_database_connection(app)
        pokemon_repository = PokemonRepository(connection)
        pokemon = pokemon_repository.find(id)
        return render_template('pokemons/show.html', pokemon=pokemon)

    @app.route('/pokemons/new', methods=['GET'])
    def pokemon_new_form():
        return render_template('pokemons/new.html')