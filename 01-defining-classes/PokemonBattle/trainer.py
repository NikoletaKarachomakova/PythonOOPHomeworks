from PokemonBattle.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemon = [] #list, which contains pokemons which are objects

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        else:
            self.pokemon.append(pokemon)
            return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        pokemon_names = [p.name for p in self.pokemon]
        if pokemon_name not in pokemon_names:
            return f"Pokemon is not caught"

        del self.pokemon[pokemon_names.index(pokemon_name)]
        return f"You have released {pokemon_name}"

    def trainer_data(self):
        result = f'Pokemon Trainer {self.name}\n' \
                 f"Pokemon count {len(self.pokemon)}"
        for p in self.pokemon:
            result += f"\n- {p.pokemon_details()}"
        return result + "\n"

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
