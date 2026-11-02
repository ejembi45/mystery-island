"""Start the Mystery Island game and handle CLI input."""

from game import new_game, available_actions, move_player, take_item, light_beacon, is_game_over



def main():
    print("Welcome to Mystery Island!")
    print("Explore the island, find the Rope and Lantern, and light the beacon at the Lighthouse to escape.")
    player_name = input("What is your name? ").strip()

    while True:
        player = new_game(player_name)

        while True:
            player = is_game_over(player)
            if player["game_over"]:
                if player["won"]:
                    print("\n*** YOU WIN! You lit the beacon and escaped Mystery Island! ***")
                else:
                    print("\n*** GAME OVER! You ran out of energy and could not escape! ***")
                break

            actions = available_actions(player)
            print(f"\n[{player['location']}] Actions: {', '.join(actions)}")
            choice = input("> ").strip().lower()

            if choice == "quit":
                break
            elif choice.startswith("go "):
                old_location = player["location"]
                player = move_player(player, choice)
                player = is_game_over(player)
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
            elif choice == "light beacon":
                old_state = (player["won"], player["game_over"])
                player = light_beacon(player)
                if (player["won"], player["game_over"]) != old_state:
                    pass
                else:
                    print("You need a lantern to light the beacon.")
            else:
                print("Invalid choice, try again")

        replay = input("\nPlay again? (yes/no) ").strip().lower()
        if replay in ("no", "n"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
