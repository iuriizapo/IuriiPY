class WordsFinder:
    def __init__(self, *args):
        self.file_names = list(args)

    def get_all_words(self):
        d = {}
        for name in self.file_names:
            with open(name, encoding='utf-8') as file:
                s = file.read().lower()
                for c in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                    s = s.replace(c, ' ')
                l = s.split()
                d[name] = l
        return d

    def find(self, word):
        d1 = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                d1[name] = words.index(word.lower())
        return d1

    def count(self, word):
        d2 = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                d2[name] = words.count(word.lower())
        return d2




finder2 = WordsFinder('test_file.txt')
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
print(finder2.get_all_words())


