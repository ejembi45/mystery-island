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
    # Normalize target: lowercase each word then capitalize first letter
    normalized_target = " ".join(word.capitalize() for word in target.lower().split())

    # Special rule: Cave -> Old Bridge requires rope
    if current == "Cave" and normalized_target == "Old Bridge":
        if "rope" not in player["inventory"]:
            return player  # reject, energy unchanged

    if normalized_target in LOCATIONS.get(current, []):
        new_energy = player["energy"] - 1
        if new_energy < 0:
            new_energy = 0
        new_player = player.copy()
        new_player["location"] = normalized_target
        new_player["energy"] = new_energy
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


def light_beacon(player):
    """Return a new player dict with won=True if beacon can be lit."""
    if player["game_over"] or player["won"]:
        return player
    if can_light_beacon(player):
        new_player = player.copy()
        new_player["won"] = True
        new_player["game_over"] = True
        return new_player
    return player


def is_game_over(player):
    """Return True if game is over (won or lost)."""
    if player["won"]:
        return player
    if player["energy"] <= 0 and not player["won"]:
        new_player = player.copy()
        new_player["game_over"] = True
        return new_player
    return player


def can_cross_bridge(player):
    """Return True if player has rope to cross from Cave to Old Bridge."""
    return "rope" in player["inventory"]


def can_light_beacon(player):
    """Return True if player has lantern and is at Lighthouse."""
    return player["location"] == "Lighthouse" and "lantern" in player["inventory"]


def available_actions(player):
    """Return a list of valid action strings for the player's current state."""
    if player["game_over"] or player["won"]:
        return ["quit"]

    actions = ["quit"]
    current = player["location"]
    for target in LOCATIONS.get(current, []):
        # Only show bridge move if player has rope
        if current == "Cave" and target == "Old Bridge":
            if "rope" in player["inventory"]:
                actions.append(f"go {target.lower()}")
        else:
            actions.append(f"go {target.lower()}")

    for item, loc in ITEM_LOCATIONS.items():
        if loc == current and item not in player["inventory"]:
            actions.append(f"take {item}")

    # Light beacon at Lighthouse with lantern
    if current == "Lighthouse" and "lantern" in player["inventory"]:
        actions.append("light beacon")

    return actions
