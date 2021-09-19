class Lexicon(object):

    def __init__(self):
        self.direction = ['north', 'east', 'south', 'west']
        self.verbs = ['go', 'kill', 'eat']
        self.stops = ['the', 'in', 'of']
        self.nouns = ['bear', 'princess']
        self.numbers = ['3', '91234', '1234']
        self.lexicon = []

    def scan(self):
        while True:
            line = input('> ')
            string_split = line.split()
            for split in string_split:
                if split in self.direction:
                    pair = ('direction', split)
                elif split in self.verbs:
                    pair = ('verb', split)
                elif split in self.stops:
                    pair = ('stop', split)
                elif split in self.nouns:
                    pair = ('noun', split)
                elif split in self.numbers:
                    pair = ('number', int(split))
                else:
                    pair = ('error', split)
                if pair not in self.lexicon:
                    self.lexicon.append(pair)
            print(self.lexicon)


lexicon = Lexicon()
lexicon.scan()
