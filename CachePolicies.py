import numpy as np
from scipy.stats import zipf
from scipy.stats import rv_discrete
from scipy import stats
import matplotlib.pyplot as plt
from numpy import random

"""
Code simulating various cache replacement policies including:
1. Random - each item is equally likely to be removed from the cache
2. First-In First-Out (FIFO) - the item that has been in the cache the longest is replaced
3. Least Recently Used (LRU) -  the item that has been accessed least recently is replaced
4. Least Frequently Used (LFU) - the item that has been accessed the fewest times is replaced
"""

def RandoSequences(length, range):
    ls= []
    n = length
    while n>0:
        ls.append(random.randint(1,range))
        n-=1
    return ls

def randomCache(cacheLength, seq):
    theCache = []
    hits = 0
    misses = 0
    index = 0
    while len(theCache)<cacheLength and index<len(seq):
        if seq[index] in theCache:
            pass
        else:
            misses+=1
            theCache.append(seq[index])
        index+=1

    if index>=len(seq):
        return hits
    for i in range(index, len(seq)):
        if seq[i] in theCache:
            hits+=1
        else:
            misses+=1
            randy = random.randint(0,cacheLength-1)
            theCache[randy] = seq[i]
    return hits/len(seq)

def fifoCache(cacheLength, seq):
    theCacheHead= LinkedList(0,None,0)
    hits = 0
    misses = 0
    index = 0
    CacheCounter = 0
    while CacheCounter<cacheLength and index<len(seq):
        if theCacheHead.inList(seq[index]):
            pass
        else:
            misses+=1
            if theCacheHead.first == None and theCacheHead.last==None:
                theCacheHead.first = LinkedList(seq[index], None, 0)
                theCacheHead.last = theCacheHead.first
                CacheCounter+=1
            else:
                x = LinkedList(seq[index],None,0)
                x.next = theCacheHead.first
                x.next.prev = x
                theCacheHead.first = x
                CacheCounter+=1
        index+=1
    if index>=len(seq):
        return hits


    for i in range(index, len(seq)):
        if theCacheHead.inList(seq[i]):
            hits+=1
        else:
            misses+=1
            x = LinkedList(seq[i],None,0)
            x.next = theCacheHead.first
            x.next.prev = x
            theCacheHead.first = x
            theCacheHead.last = theCacheHead.last.prev
            theCacheHead.last.next = None

    return hits/len(seq)

def lruCache(cacheLength,seq):
    theCacheHead= LinkedList(0,None,0)
    hits = 0
    misses = 0
    index = 0
    CacheCounter = 0
    while CacheCounter<cacheLength and index<len(seq):
        if theCacheHead.inList(seq[index]):
            #hits+=1
            theNode = theCacheHead.get(seq[index])
            theCacheHead.mostRecent(theNode)
        else:
            misses+=1
            if theCacheHead.first == None and theCacheHead.last==None:
                theCacheHead.first = LinkedList(seq[index], None, 0)
                theCacheHead.last = theCacheHead.first
                CacheCounter+=1
            else:
                x = LinkedList(seq[index],None,0)
                x.next = theCacheHead.first
                x.next.prev = x
                theCacheHead.first = x
                CacheCounter+=1
        index+=1
    if index>=len(seq):
        return hits


    for i in range(index, len(seq)):
        if theCacheHead.inList(seq[i]):
            hits+=1
            theNode = theCacheHead.get(seq[i])
            theCacheHead.mostRecent(theNode)

        else:
            misses+=1
            x = LinkedList(seq[i],None,0)
            x.next = theCacheHead.first
            x.next.prev = x
            theCacheHead.first = x
            theCacheHead.last = theCacheHead.last.prev
            theCacheHead.last.next = None

    return hits/len(seq)

def lfuCache(cacheLength, seq):
    theCacheHead= LinkedList(0,None,0)
    hits = 0
    misses = 0
    index = 0
    CacheCounter = 0
    while CacheCounter<cacheLength and index<len(seq):
        if theCacheHead.inList(seq[index]):
            #hits+=1
            x = theCacheHead.get(seq[index])
            x.freq = x.freq+1
        else:
            misses+=1
            if theCacheHead.first == None and theCacheHead.last==None:
                theCacheHead.first = LinkedList(seq[index], None, 1)
                theCacheHead.last = theCacheHead.first
                CacheCounter+=1
            else:
                x = LinkedList(seq[index],None,1)
                x.next = theCacheHead.first
                x.next.prev = x
                theCacheHead.first = x
                CacheCounter+=1
        index+=1
    if index>=len(seq):
        return hits
    for i in range(index, len(seq)):
        if theCacheHead.inList(seq[i]):
            hits+=1
            x = theCacheHead.get(seq[i])
            x.freq = x.freq+1
        else:
            misses+=1
            x = LinkedList(seq[i],None,1)
            y = theCacheHead.lowestFreq()
            if y.val == theCacheHead.first.val:
                x.next = y.next
                x.next.prev = x
                theCacheHead.first = x
            elif y.val == theCacheHead.last.val:
                theCacheHead.last.prev.next = x
                x.prev = theCacheHead.last.prev
                theCacheHead.last = x
            else:
                y.prev.next = x
                y.next.prev = x
                x.next = y.next
                x.prev = y.prev
    return hits/len(seq)



def main():
    '''
    Triggers the simulation process. Obtains the different requests and uses them to obtain hit rates under the different policies
    '''
    uniformrequests = getunif()
    zipfrequests = get_Zipf_RVs() 
    reqgenrequests = reqgen_RVs()
    cachesizes = [number for number in range(10,201,20)]

    #Hit rates for the different cache replacement policies under zipf and unif distributions
    random_unif, random_zipf, fifo_unif, fifo_zipf, lru_unif, lru_zipf, lfu_unif, lfu_zipf = [],[],[],[],[],[],[],[]
    random_rg, fifo_rg, lru_rg, lfu_rg =  [],[],[],[]
    for i in range(10,201,20):
    	random_unif.append(randomCache(i,uniformrequests))
    	random_zipf.append(randomCache(i,zipfrequests))
    	random_rg.append(randomCache(i,reqgenrequests))
    	fifo_unif.append(fifoCache(i,uniformrequests))
    	fifo_zipf.append(fifoCache(i,zipfrequests))
    	fifo_rg.append(fifoCache(i,reqgenrequests))
    	lru_unif.append(lruCache(i,uniformrequests))
    	lru_zipf.append(lruCache(i,zipfrequests))
    	lru_rg.append(lruCache(i,reqgenrequests))
    	lfu_unif.append(lfuCache(i,uniformrequests))
    	lfu_zipf.append(lfuCache(i,zipfrequests))
    	lfu_rg.append(lfuCache(i,reqgenrequests))
   
    hitrates_unif = [random_unif,fifo_unif,lru_unif,lfu_unif]
    hitrates_zipf = [random_zipf,fifo_zipf,lru_zipf,lfu_zipf]
    hitrates_rg= [random_rg,fifo_rg,lru_rg,lfu_rg]

    plotdistribution(cachesizes,hitrates_unif,"Uniform") 
    plotdistribution(cachesizes,hitrates_zipf, "Zipf")
    plotdistribution(cachesizes,hitrates_rg, "Request generator")
    return

def plotdistribution(cachesize,hitrates,distribution):
    '''
    Input(s): Takes in different cache sizes from 10-200, hitrates and the distribution from which they are obtained.
    Output:Plots the hitrates against the cache sizes for all the cache replacement policies
    '''
    policies = ["Random","FIFO","LRU","LFU"]
    for i in range(4):
        plt.plot(cachesize, hitrates[i], label = policies[i])
        plt.xlabel("Cache sizes")
        plt.ylabel("Hit rate")
        plt.title(distribution)
        plt.legend()
    plt.savefig(distribution)
    plt.show()
    return

def getunif():
    '''
    Generates 100,000 requests uniformly distributed on (1,1000)
    '''
    nums = np.arange(1,1001)
    probs = [1/1000 for number in range(1000)] 
    unif = stats.rv_discrete(name='unif', values=(nums, probs))
    RVs = unif.rvs(size=100000)

    return RVs

def get_zipF_probs():
    '''
    Generates a list of zipF probabilities for items on (1,1000)
    '''
    probs = []
    numsum = 0
    RV = 0
    denomsum = 0
    
    for x in range(1,1001):
        denomsum += 1/x
    
    for i in range(1,1001):
        numsum = 1/i
        p = numsum/denomsum
        probs.append(p)
        
    return probs

def get_Zipf_RVs():
    '''
    Uses zipf probabilities to generate random zipf requests
    '''
    nums = np.arange(1,1001)
    probs = get_zipF_probs()
    zipF = stats.rv_discrete(name='zipF', values=(nums, probs))
    RVs = zipF.rvs(size=100000)

    return RVs

def reqgen_RVs():
    '''
    This function obtains the requests obtained from the request generator.
    Output: List of generated requests
    '''
    f = open("requests.txt", "r")
    reqgen = [line.rstrip() for line in open("requests.txt")]
    return reqgen

class LinkedList:
    def __init__(self,val,prev,freq):
        self.val = val
        self.next = None
        self.prev = prev
        self.isHead = False
        self.size = 0
        self.first = None
        self.last = None
        self.freq = freq

    def inList(self,val):
        #checks if val is in list(To only be called by head)
        i = self.first
        while i!=None:
            if i.val == val:
                return True
            i = i.next
        return False

    def mostRecent(self, node):
        if node.val == self.first.val:
            return
        if node.val == self.last.val:
            self.first.prev = node
            node.next = self.first
            self.first = node
            self.last = node.prev
            self.last.next = None
            node.prev = None
            return
        node.prev.next = node.next
        node.next.prev = node.prev
        self.first.prev = node
        node.next = self.first
        node.prev = None
        self.first = node

    def get(self,val):
        i = self.first
        while i!=None:
            if i.val == val:
                return i
            i = i.next
        return None

    def lowestFreq(self):
        i = self.first
        lowest = float("inf")
        x = None
        while i!=None:
            if i.freq<lowest:
                lowest = i.freq
                x = i
            i = i.next
        return x


main()