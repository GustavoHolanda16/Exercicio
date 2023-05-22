import requests

# obter dados dos Pokémons da API
response = requests.get("https://pokeapi.co/api/v2/pokemon?limit=151")
data = response.json()["results"]

# criar um dicionário para armazenar os dados dos Pokémons
pokedex = {}
for pokemon in data:
    response = requests.get(pokemon["url"])
    pokemon_data = response.json()
    pokedex[pokemon_data["id"]] = pokemon_data

# definir uma função para exibir informações de um Pokémon
def display_pokemon_info(pokemon_id):
    pokemon = pokedex.get(pokemon_id)
    if pokemon:
        print("Nome:", pokemon["name"])
        print("Tipos:", [t["type"]["name"] for t in pokemon["types"]])
        print("Habilidades:", [a["ability"]["name"] for a in pokemon["abilities"]])
        print("Movimentos:", [m["move"]["name"] for m in pokemon["moves"]])
        print("HP:", pokemon["stats"][0]["base_stat"])
        print("Ataque:", pokemon["stats"][1]["base_stat"])
        print("Defesa:", pokemon["stats"][2]["base_stat"])
        print("Velocidade:", pokemon["stats"][5]["base_stat"])
    else:
        print("Pokemon não encontrado.")

# definir uma função para exibir a lista de Pokémons
def display_pokemon_list():
    for pokemon_id in pokedex:
        pokemon = pokedex[pokemon_id]
        print(pokemon_id, "-", pokemon["name"])

# exemplo de uso
display_pokemon_list()
pokemon_id = input("Digite o número do Pokémon para exibir informações: ")
display_pokemon_info(int(pokemon_id))
