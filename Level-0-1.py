'''
    Created on Feb 27, 2013
    
    @author: jewel
    
    This is pure fun.
    '''
import sys


class L0:
    
    def solution(self):
        sys.stdout.write('Level 0: %d\n' % 2**38)



class L1:

    def __init__(self):
        self.alph = list('abcdefghijklmnopqrstuvwxyz')

    def solution0(self, str):
        def shift(c):
            if c in self.alph:
                return self.alph [ ( self.alph.index( c ) + 2 ) % 26 ]
            else:
                return c
        print "Level 1:", "".join( map( shift, list(str) ) )
    
    
    def solution1(self, str):
        from string import maketrans
        trans = maketrans("abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab")
        print "Level 1:", str.translate(trans)
    
    def solution2(self, given):
        print 'Level 1: ', ''.join([chr((ord(l)+2-97)%26+97) if ord(l)<=ord('z') and ord(l)>=ord('a') else l for l in given])



if __name__ == '__main__':
    level0 = L0()
    level0.solution()
    
    gibberish = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
    level1 = L1()
    level1.solution0(gibberish)
    level1.solution0("map")
    level1.solution1("map")
