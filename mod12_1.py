import unittest


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        a = Runner('X')
        for _ in range(10):
            a.walk()
        self.assertEqual(a.distance, 50)

    def test_run(self):
        b = Runner('Y')
        for _ in range(10):
            b.run()
        self.assertEqual(b.distance, 100)

    def test_challenge(self):
        c = Runner('Z')
        d = Runner('S')
        for _ in range(10):
            d.walk()
            c.run()
        self.assertNotEqual(c.distance, d.distance)

if __name__ == '__main__':
    unittest.main()

