"""Start the Mystery Island game and handle CLI input."""

from game import new_game, available_actions


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
        elif choice not in actions:
            print("Invalid choice, try again")
        else:
            if choice == "quit":
                break


if __name__ == "__main__":
    main()
