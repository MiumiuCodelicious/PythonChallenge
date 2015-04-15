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



class L4:
    '''
        send 400 requests
        '''
    def __init__(self):
        self.seed = 12345
        self.url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
        self.url2 = 'http://www.pythonchallenge.com/pc/def/'
    
    def answer(self):
        import urllib, re
        for t in range(400):
            response =  urllib.urlopen(self.url+str(self.seed)).read()
            #        print t, response
            if re.match(r'Yes', response):  self.seed = self.seed/2
            elif re.search(r'\.html', response):  print 'Q4:', response ;break
            else:
                reg_reply = re.search(r'the next nothing is ([0-9]+)', response)
                self.seed = int( response[reg_reply.start()+20 :reg_reply.end()] )






if __name__ == '__main__':

    import time
    start_time = time.time()
    level2 = L2()
    level2.solution1()
    print ("--- %s seconds ---" % (time.time() - start_time))

