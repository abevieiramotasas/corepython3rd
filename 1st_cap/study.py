import re

# organizar as infos
class Pattern:
    def __init__(self, pattern, *samples):
        self.pattern_string = pattern
        self.pattern = re.compile(pattern)
        self.samples = samples
        
        
    def findall(self, s):
        print('"%s"   "%s"    %s' % (self.pattern_string, s, self.pattern.findall(s)))
        
    def run_samples(self):
        for sample in self.samples:
            self.findall(sample)
            
    def __str__(self):
        return self.pattern_string
        
patterns = []

def run_all_samples():
    for sample in patterns:
        sample.run_samples()

patterns.append(Pattern(r'curso de regex', 'curso de regex', 'curso de net'))

patterns.append(Pattern(r'a|b', 'a', 'b', 'cv', 'ab'))

patterns.append(Pattern(r'.', 'a', 'b', '', 'aa'))

patterns.append(Pattern(r'^aab*', 'aabbb', 'aa', 'abbba'))

# pattern match left to right
patterns.append(Pattern(r'ab|a|b', 'ab'))
patterns.append(Pattern(r'a|b|ab', 'ab'))

patterns.append(Pattern(r'aab*$', 'aabbbb', 'aabbbc', 'caaabb'))

patterns.append(Pattern(r'^aab*$', 'aabbbb', 'aabbbc', 'caabbb'))

patterns.append(Pattern(r'a{1,3}', 'aaa', 'aaaa'))
patterns.append(Pattern(r'a{1,3}?', 'aaa', 'aaaa'))

patterns.append(Pattern(r'[a-bA-B0-9]*', 'abelardo123', 'SwampCrazyBR'))

patterns.append(Pattern('r[^0-9]*', 'abelardo', 'abelardo123', 'ab1^$%%'))

patterns.append(Pattern(r'\bab\b', 'meu apelido eh ab', 'nao abe'))

patterns.append(Pattern(r'((?:ab)*)', 'abababab'))

patterns.append(Pattern(r'.*?(abe*)c*\1', 'uahauhsabeeecccccabeee', 'uahsuhaabeecccccabe'))

patterns.append(Pattern(r'(?P<grupo>abe*)c*(?P=grupo)', 'abeeecccabeee', 'abeeeccabe'))

patterns.append(Pattern(r'ab*(?#mas que regex linda)ab*', 'abbbabb', 'ababbb'))

# LOOK
#   AHEAD
# regex(look) casa a regex se depois dela vier look
#   BEHIND
# regex(look) casa a regex se antes dela vier look

# match consome e n adiciona ao match
patterns.append(Pattern(r'^(.*)(?=.com)', 'abbbekgb@gmail.com'))

# se nao match nao consome
patterns.append(Pattern(r'(\w*)(?!@hotmail.com)', 'abbbekgb@gmail.com', 'abbbekgb@hotmail.com'))

# match consome e n adiciona ao match, voltando
patterns.append(Pattern(r'(?<=abc)defg*', 'defggabcdefggg'))

patterns.append(Pattern(r'(?<!abc)defg*', 'defggabcdefggg'))

# nao sei usar!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
patterns.append(Pattern(r'(<)?\w+(?(1)>)', '<abe>', 'abe', '<abe'))

patterns.append(Pattern(r'\bab', 'abelardo', 'o abelardo eh legal', 'oab'))

patterns.append(Pattern(r'\Bab', 'abelardo', 'o abelardo eh legal', 'oab'))

patterns.append(Pattern(r'(\w+)-(\d+)', 'ab-10', 'aaa-20'))
# exemplo com (?:...)

# re.match(r'ab(?:ab)cc', 'ababcc').groups() 
# ()
# re.match(r'ab(ab)cc', 'ababcc').groups()
# ('ab')

# exercicios

# 1 regex pra linguagem das strings espelhadas : abab abeabe hehehehe
# r'^(.{1,}?)\1$'



patterns[-1].run_samples()
