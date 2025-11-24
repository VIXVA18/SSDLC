import unittest
from unittest.mock import patch
from io import StringIO
import builtins

# Import your module (adjust name if needed)
import your_game_file_name as game


class TestGuessingGame(unittest.TestCase):

    # -----------------------------------------
    # slow_print()
    # -----------------------------------------
    @patch("sys.stdout", new_callable=StringIO)
    @patch("time.sleep")  # prevent delays
    def test_slow_print(self, mock_sleep, mock_stdout):
        game.slow_print("Hi")
        self.assertIn("Hi", mock_stdout.getvalue())
        mock_sleep.assert_called()  # should call sleep for each char

    # -----------------------------------------
    # get_difficulty()
    # -----------------------------------------
    @patch("builtins.input", side_effect=["x", "2"])
    @patch("sys.stdout", new_callable=StringIO)
    @patch("time.sleep")
    def test_get_difficulty(self, mock_sleep, mock_stdout, mock_input):
        limit = game.get_difficulty()
        self.assertEqual(limit, 50)  # difficulty 2 => 50

    # -----------------------------------------
    # play_game()
    # -----------------------------------------
    @patch("sys.stdout", new_callable=StringIO)
    @patch("time.sleep")
    @patch("random.randint", return_value=7)
    @patch("builtins.input", side_effect=["3", "9", "7"])
    def test_play_game(self, mock_input, mock_rand, mock_sleep, mock_stdout):
        game.play_game(10)
        output = mock_stdout.getvalue()

        self.assertIn("Too low!", output)
        self.assertIn("Too high!", output)
        self.assertIn("You got it!", output)
        self.assertIn("7", output)

    # -----------------------------------------
    # play_again()
    # -----------------------------------------
    @patch("builtins.input", return_value="y")
    def test_play_again_yes(self, mock_input):
        self.assertTrue(game.play_again())

    @patch("builtins.input", return_value="n")
    def test_play_again_no(self, mock_input):
        self.assertFalse(game.play_again())

    # -----------------------------------------
    # main() — only test that it exits correctly
    # -----------------------------------------
    @patch("builtins.input", side_effect=[
        "1",  # difficulty: easy
        "5",  # guess
        "5",  # guess again (correct)
        "n"   # no more games
    ])
    @patch("random.randint", return_value=5)
    @patch("time.sleep")
    @patch("sys.stdout", new_callable=StringIO)
    def test_main(self, mock_stdout, mock_sleep, mock_rand, mock_input):
        # We don't want the script to actually call main() repeatedly
        game.main()
        output = mock_stdout.getvalue()
        self.assertIn("Farewell", output)


if __name__ == "__main__":
    unittest.main()
