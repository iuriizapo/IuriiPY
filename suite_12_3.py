import unittest
import mod12_1, mod12_2


mod_12_TS = unittest.TestSuite()
mod_12_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(mod12_1.RunnerTest))
mod_12_TS.addTest(unittest.TestLoader().loadTestsFromTestCase(mod12_2.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(mod_12_TS)