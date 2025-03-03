import pandas as pd

pokemon_data = pd.read_csv("pokemon.csv")

#Moving the name of the Pokémon to the first column 
pokemon_data = pokemon_data[['name'] + [col for col in pokemon_data.columns if col != 'name']]



