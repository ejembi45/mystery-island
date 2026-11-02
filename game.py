"""Hold all pure game logic for Mystery Island."""

LOCATIONS = {
    "Beach": ["Jungle"],
    "Jungle": ["Beach", "Cave"],
    "Cave": ["Jungle", "Old Bridge"],
    "Old Bridge": ["Cave", "Lighthouse"],
    "Lighthouse": ["Old Bridge"],
}

ITEM_LOCATIONS = {
    "rope": "Jungle",
    "lantern": "Cave",
}


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


def move_player(player, direction):
    """Return a new player dict with updated location and energy if move is legal."""
    if player["game_over"] or player["won"]:
        return player

    target = direction.replace("go ", "").strip()
    current = player["location"]

    # Normalize target to match location names (capitalize first letter)
    normalized_target = target.capitalize()

    if normalized_target in LOCATIONS.get(current, []):
        new_player = player.copy()
        new_player["location"] = normalized_target
        new_player["energy"] = player["energy"] - 1
        return new_player

    return player


def take_item(player, item_name):
    """Return a new player dict with item added if pickup is valid."""
    if player["game_over"] or player["won"]:
        return player

    if item_name not in ITEM_LOCATIONS:
        return player

    item_loc = ITEM_LOCATIONS[item_name]
    if player["location"] != item_loc:
        return player

    if item_name in player["inventory"]:
        return player

    new_player = player.copy()
    new_player["inventory"] = player["inventory"] + [item_name]
    return new_player


def available_actions(player):
    """Return a list of valid action strings for the player's current state."""
    if player["game_over"] or player["won"]:
        return ["quit"]

    actions = ["quit"]
    current = player["location"]
    for target in LOCATIONS.get(current, []):
        actions.append(f"go {target.lower()}")

    for item, loc in ITEM_LOCATIONS.items():
        if loc == current and item not in player["inventory"]:
            actions.append(f"take {item}")

    return actions
