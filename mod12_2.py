import unittest


class Runner:
    def __init__(self, name, speed=5):
        self.name = name
        self.distance = 0
        self.speed = speed

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant.name
                    place += 1
                    self.participants.remove(participant)

        return finishers

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.a = Runner('Усэйн',10)
        self.b = Runner('Андрей', 9)
        self.c = Runner('Ник',3)

    @classmethod
    def tearDownClass(cls):
        print(*cls.all_results, sep='\n')

    def test_tournament_1(self):
        tournament_1 = Tournament(90, self.a, self.c)
        TournamentTest.all_results.append(tournament_1.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])]=='Ник')

    def test_tournament_2(self):
        tournament_2 = Tournament(90, self.b, self.c)
        TournamentTest.all_results.append(tournament_2.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])]=='Ник')

    def test_tournament_3(self):
        tournament_3 = Tournament(90, self.a,self.b, self.c)
        TournamentTest.all_results.append(tournament_3.start())
        self.assertTrue(TournamentTest.all_results[-1][max(TournamentTest.all_results[-1])]=='Ник')

    def test_tournament_doping(self):
        tournament_4 = Tournament(25, self.b,self.a, self.c)
        TournamentTest.all_results.append(tournament_4.start())
        self.assertTrue(TournamentTest.all_results[-1][min(TournamentTest.all_results[-1])]== 'Усэйн',
            f'{TournamentTest.all_results[-1][min(TournamentTest.all_results[-1])]} '
            f'уличен в применении допинга! Результат забега аннулирован!')
        









if __name__ == '__main__':
    unittest.main()

