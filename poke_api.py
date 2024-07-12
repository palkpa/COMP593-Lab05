import requests

def get_pokemon_info(pokemon_name):
    """
    Fetches information for a specified Pokémon from the PokéAPI.

    Args:
        pokemon_name (str): Name or PokéDex number of the Pokémon.

    Returns:
        dict: Dictionary containing the Pokémon information if successful, None otherwise.
    """
    print(f"Getting information for {pokemon_name}...")

    POKE_API_URL = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower().strip()}'
    response = requests.get(POKE_API_URL)

    if response.status_code == 200:
        print("Success")
        return response.json()
    else:
        print("Failure")
        return None
