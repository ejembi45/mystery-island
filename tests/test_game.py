"""Unit tests for Mystery Island game logic."""

import unittest
from game import (
    new_game,
    move_player,
    take_item,
    light_beacon,
    is_game_over,
    available_actions,
)


class TestNewGame(unittest.TestCase):
    def test_t1_new_game_starts_correctly(self):
        """new_game starts at Beach with 5 energy and empty inventory."""
        p = new_game("Test")
        self.assertEqual(p["location"], "Beach")
        self.assertEqual(p["energy"], 5)
        self.assertEqual(p["inventory"], [])
        self.assertFalse(p["game_over"])
        self.assertFalse(p["won"])


class TestMovePlayer(unittest.TestCase):
    def test_t2_invalid_direction_unchanged(self):
        """move_player with an invalid direction leaves player state unchanged."""
        p = new_game("Test")
        result = move_player(p, "go cave")
        self.assertEqual(result["location"], "Beach")
        self.assertEqual(result["energy"], 5)
        self.assertEqual(result, p)

    def test_t3_legal_move_changes_location_and_energy(self):
        """A legal move changes location and decreases energy by exactly 1."""
        p = new_game("Test")
        result = move_player(p, "go jungle")
        self.assertEqual(result["location"], "Jungle")
        self.assertEqual(result["energy"], 4)

    def test_t4_wrong_direction_rejected_no_cost(self):
        """Wrong-direction move is rejected without energy cost."""
        p = new_game("Test")
        p = move_player(p, "go jungle")
        result = move_player(p, "go lighthouse")
        self.assertEqual(result["location"], "Jungle")
        self.assertEqual(result["energy"], 4)


class TestTakeItem(unittest.TestCase):
    def test_t5_rope_collected_once(self):
        """Rope can be collected once, second attempt rejected."""
        p = new_game("Test")
        p = move_player(p, "go jungle")
        p = take_item(p, "rope")
        self.assertEqual(len(p["inventory"]), 1)
        self.assertIn("rope", p["inventory"])
        # Second attempt
        result = take_item(p, "rope")
        self.assertEqual(len(result["inventory"]), 1)


class TestBridgeAndBeacon(unittest.TestCase):
    def test_t6_bridge_requires_rope(self):
        """Bridge cannot be crossed without rope."""
        p = new_game("Test")
        p = move_player(p, "go jungle")
        p = move_player(p, "go cave")
        old = p.copy()
        result = move_player(p, "go old bridge")
        self.assertEqual(result["location"], "Cave")
        self.assertEqual(result["energy"], 3)

    def test_t7_light_beacon_without_lantern_fails(self):
        """Lighthouse cannot be lit without lantern."""
        p = new_game("Test")
        p = move_player(p, "go jungle")
        p = take_item(p, "rope")
        p = move_player(p, "go cave")
        p = move_player(p, "go old bridge")
        p = move_player(p, "go lighthouse")
        # No lantern
        result = light_beacon(p)
        self.assertFalse(result["won"])
        self.assertFalse(result["game_over"])

    def test_t8_win_with_correct_items(self):
        """Correct inventory and location can win."""
        p = new_game("Test")
        p = move_player(p, "go jungle")
        p = take_item(p, "rope")
        p = move_player(p, "go cave")
        p = take_item(p, "lantern")
        p = move_player(p, "go old bridge")
        p = move_player(p, "go lighthouse")
        result = light_beacon(p)
        self.assertTrue(result["won"])
        self.assertTrue(result["game_over"])


class TestGameOver(unittest.TestCase):
    def test_t9_energy_exhaustion_causes_loss(self):
        """Energy exhaustion causes loss."""
        p = new_game("Test")
        for _ in range(3):
            p = move_player(p, "go jungle")
            p = move_player(p, "go beach")
            p = is_game_over(p)
        self.assertTrue(p["game_over"])
        self.assertFalse(p["won"])
        self.assertEqual(p["energy"], 0)

    def test_t10_replay_resets_state(self):
        """Replay resets energy, location and inventory."""
        p1 = new_game("Test")
        p1 = move_player(p1, "go jungle")
        p1 = take_item(p1, "rope")
        p1["won"] = True
        p2 = new_game("Test")
        self.assertEqual(p2["energy"], 5)
        self.assertEqual(p2["location"], "Beach")
        self.assertEqual(p2["inventory"], [])
        self.assertFalse(p2["won"])


if __name__ == "__main__":
    unittest.main()
