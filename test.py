import unittest
from whiteboard import solution

class WhiteboardTest(unittest.TestCase):
    def test_1(self):
        self.assertIn(solution("Hello there:) I'm a smiley face:) but sometimes I get sad :(. I'm usually really happy! :D"), [[3, 1], (3, 1)])

    def test_2(self):
        self.assertIn(solution("I'm a sad face :(, this is my brother smiley face :) my cousins are crying face :'( and oddly-always-too-happy-face :D"), [[2, 2], (2, 2)])

    def test_3(self):
        self.assertIn(solution(":():)(:):'(:'(:'((:::)(:)(:():'(::D:D::'(D:DD:'(:D:DD:DD:D:D:D:D:'("), [[14,9], (14,9)])


if __name__ == '__main__':
    unittest.main()