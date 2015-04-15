import sys

class L2:
    
    def __init__(self):
        self.gib = open('L2_Challenge.txt', 'r').read()

    def solution0(self):
        print 'L2:', ''.join([c for c in self.gib if c not in self.gib[:self.gib.index(c)] + self.gib[self.gib.index(c)+1:]])
    
    def solution1(self):
        import collections
        d = collections.OrderedDict()
        for c in self.gib :
            if c in d: d[c] = 1
            else: d[c] = 0
        print 'L2:', ''.join(c for c in d if d[c]==0)



class L3:
    '''
        use Q3_Readin file
        '''
    def answer1(self):
        import re
        c = open('L3_Readin').read()
        reg = re.findall(r'[^A-Z][A-Z]{3}([a-z])[A-Z]{3}[^A-Z]', c)
        if reg:
            print 'L3:', ''.join(r for r in reg)




if __name__ == '__main__':

    import time
    start_time = time.time()
    level2 = L2()
    level2.solution1()
    print ("--- %s seconds ---" % (time.time() - start_time))

