# Mystery Island

A text adventure game. Explore the island, find essential items, and signal for rescue.

## Prerequisites

- Python 3.x

## How to Run the Game

```bash
python3 main.py
```

## How to Run the Tests

```bash
python3 -m unittest discover -s tests -v
```

## Game Rules

### Location Map

```
Beach → Jungle → Cave → Old Bridge → Lighthouse
```

You can move forward and backward between adjacent locations.

### Items

| Item   | Location |
|--------|----------|
| Rope   | Jungle   |
| Lantern| Cave     |

### Energy System

- You start with **5 energy**.
- Every legal move costs **1 energy**.
- Picking up items costs **0 energy**.
- The "light beacon" action costs **0 energy**.
- Invalid or rejected input costs **0 energy**.
- If your energy reaches **0 before the beacon is lit**, you lose.

### Win Condition

1. Be at the **Lighthouse**.
2. Have both the **Rope** and **Lantern** in your inventory.
3. Choose the **light beacon** action.

### Lose Condition

- Energy reaches **0** before the beacon is lit.
- The bridge between Cave and Old Bridge cannot be crossed without the **Rope**.

### Energy Math

The optimal path is:

```
Beach → Jungle (1) → Cave (2) → Old Bridge (3) → Lighthouse (4)
Pick up Rope (0) → Pick up Lantern (0) → Light Beacon (0)
Total: 4 moves, 5 energy → 1 energy remaining
```

**You have room for exactly one mistake.** One extra move (a wrong turn, an unnecessary backtrack) consumes your last energy point and causes you to lose.

## Available Commands

- `go <location>` — Move to an adjacent location (e.g., `go jungle`)
- `take <item>` — Pick up an item at your current location (e.g., `take rope`)
- `light beacon` — Light the beacon at the Lighthouse (win condition)
- `quit` — Exit the game
- `help` — Show available commands

## Known Limitations

- No save/load functionality
- Fixed text commands only (no natural language parsing)
- No location descriptions beyond the current location name
- No inventory display command (inventory shown only on pickup)
- Single-player only, no multiplayer
