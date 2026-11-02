# Mystery Island

A text adventure game. Explore the island, find essential items, and signal for rescue.

## Goal

Reach the **Lighthouse** and light the beacon. To do so, you must carry both the **Rope** and the **Lantern**.

## Locations

The island is a linear chain of five locations:

```
Beach → Jungle → Cave → Old Bridge → Lighthouse
```

You can move forward and backward between adjacent locations.

## Items

| Item   | Location |
|--------|----------|
| Rope   | Jungle   |
| Lantern| Cave     |

## Energy System

- You start with **5 energy**.
- Every legal move costs **1 energy**.
- Picking up items costs **0 energy**.
- The "light beacon" action costs **0 energy**.
- Invalid or rejected input costs **0 energy**.
- If your energy reaches **0 before the beacon is lit**, you lose.

## How to Win

1. Be at the **Lighthouse**.
2. Have both the **Rope** and **Lantern** in your inventory.
3. Choose the **light beacon** action.

## Energy Math & Difficulty

The optimal path is:

```
Beach → Jungle (1) → Cave (2) → Old Bridge (3) → Lighthouse (4)
Pick up Rope (0) → Pick up Lantern (0) → Light Beacon (0)
Total: 4 moves, 5 energy → 1 energy remaining
```

**You have room for exactly one mistake.** One extra move (a wrong turn, an unnecessary backtrack) consumes your last energy point and causes you to lose. Any more than one wasted move and the game ends.

## Commands

- `move <direction>` — Move to an adjacent location (costs 1 energy)
- `inventory` — Check what you are carrying
- `look` — Describe your current location
- `pick <item>` — Pick up an item at your current location (free)
- `light beacon` — Light the beacon at the Lighthouse (win condition)
- `help` — Show available commands
