"""Hold all pure game logic for Mystery Island."""


def new_game(player_name):
    """Return a new player dict with starting state."""
    return {
        "name": player_name,
        "location": "Beach",
        "energy": 5,
        "inventory": [],
        "game_over": False,
        "won": False,
    }


def available_actions(player):
    """Return a list of valid action strings for the player's current state."""
    if player["game_over"] or player["won"]:
        return ["quit"]
    return ["quit"]
