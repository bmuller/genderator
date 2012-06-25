import codecs, os
        
MALE = 0
FEMALE = 1
ANDROGYNOUS = 2

class Detector:
    def __init__(self, fname=None):
        fname = fname or os.path.join(os.path.dirname(__file__), 'data', "nam_dict.txt")
        self.parse(fname)


    def parse(self, fname):
        self.names = {}
        f = codecs.open(fname, encoding='iso8859-1')
        line = f.readline()
        while line:
            self.eatNameLine(line)
            line = f.readline()
        f.close()


    def eatNameLine(self, line):
        if line.startswith("#") or line.startswith("="):
            return

        parts = filter(lambda p: p.strip() != "", line.split(" "))
        
        if "F" in parts[0]:
            self.set(parts[1], FEMALE)
        elif "M" in parts[0]:
            self.set(parts[1], MALE)     
        else:
            self.set(parts[1], ANDROGYNOUS)


    def set(self, name, gender):
        # go w/ first option, don't reset
        if self.names.has_key(name):
            return

        if "+" in name:
            for replacement in [ '', '-', ' ' ]:
                self.set(name.replace('+', replacement), gender)
        else:
            self.names[name] = gender


    def getGender(self, name):
        return self.names.get(name, ANDROGYNOUS)
