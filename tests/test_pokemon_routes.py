from playwright.sync_api import Page, expect

"""
GET /pokemons
"""
def test_get_pokemons(db_connection, web_client):
    db_connection.seed("seeds/pokemon_store.sql")

    response = web_client.get("/api/pokemons")

    assert response.status_code == 200

    assert response.data.decode("utf-8") == "\n".join([
        "Pokemon(1, Bulbasaur, earth)",
        "Pokemon(2, Pikachu, electric)",
        "Pokemon(3, Mewtwo, psycho)",
        "Pokemon(4, Charizard, fire)",
        "Pokemon(5, Squirtle, water)"
    ])


"""
We can list out all the pokemons
"""
def test_get_pokemons(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")

    page.goto(f"http://{test_web_address}/pokemons")

    list_items = page.locator("li")

    expect(list_items).to_have_text([
        "Bulbasaur is a type of earth pokemon",
        "Pikachu is a type of electric pokemon",
        "Mewtwo is a type of psycho pokemon",
        "Charizard is a type of fire pokemon",
        "Squirtle is a type of water pokemon",
    ])

"""
We can visit a particular pokemons page
"""
def test_get_one_pokemon(db_connection, page, test_web_address):
    db_connection.seed("seeds/pokemon_store.sql")

    page.goto(f"http://{test_web_address}/pokemons")

    page.click("text=Pikachu")

    name_element = page.locator(".t-name")
    type_element = page.locator(".t-type")

    expect(name_element).to_have_text("Pikachu")
    expect(type_element).to_have_text("electric")
