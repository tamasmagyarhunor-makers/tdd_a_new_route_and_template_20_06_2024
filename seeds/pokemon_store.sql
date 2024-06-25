DROP TABLE IF EXISTS pokemons;
DROP SEQUENCE IF EXISTS pokemons_id_seq;

CREATE SEQUENCE IF NOT EXISTS pokemons_id_seq;
CREATE TABLE pokemons (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    type VARCHAR(255)
);

INSERT INTO pokemons (name, type) VALUES ('Bulbasaur', 'earth');
INSERT INTO pokemons (name, type) VALUES ('Pikachu', 'electric');
INSERT INTO pokemons (name, type) VALUES ('Mewtwo', 'psycho');
INSERT INTO pokemons (name, type) VALUES ('Charizard', 'fire');
INSERT INTO pokemons (name, type) VALUES ('Squirtle', 'water');