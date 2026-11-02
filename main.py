"""Start the Mystery Island game and handle CLI input."""

from game import new_game, available_actions, move_player, take_item



def main():
    print("Welcome to Mystery Island!")
    print("Explore the island, find the Rope and Lantern, and light the beacon at the Lighthouse to escape.")
    player_name = input("What is your name? ").strip()

    player = new_game(player_name)

    while True:
        actions = available_actions(player)
        print(f"\n[{player['location']}] Actions: {', '.join(actions)}")
        choice = input("> ").strip().lower()

        if choice == "quit":
            break
        elif choice.startswith("go "):
            old_location = player["location"]
            player = move_player(player, choice)
            if player["location"] != old_location:
                print(f"You move to {player['location']}. Energy: {player['energy']}")
            else:
                print("You can't go that way")
        elif choice.startswith("take "):
            item = choice.replace("take ", "").strip()
            old_inventory = player["inventory"].copy()
            player = take_item(player, item)
            if player["inventory"] != old_inventory:
                print(f"You picked up the {item}.")
            else:
                print(f"There is no {item} here or you already have it.")
        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    main()
