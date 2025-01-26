from test_utils import add_src_to_path
add_src_to_path()

import unittest
from unittest.mock import patch
from io import StringIO

from main import main

class TestMain(unittest.TestCase):
    @patch("sys.stdin", StringIO("Spider 2, Leopard 0\nLions 3, Spider 3\nLeopard 1, Lions 2"))
    @patch("sys.stdout", new_callable=StringIO)
    def test_main(self, mock_stdout):
        main()

        expected_output = (
            "1. Lions, 4 pts\n"
            "2. Spider, 4 pts\n"
            "3. Leopard, 0 pts\n"
        )
        self.assertEqual(mock_stdout.getvalue(), expected_output)

if __name__ == "__main__":
    unittest.main()
