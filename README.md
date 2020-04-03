# COSC 223 : Caching Theory

Compile and run the ListReader.java code (run `javac ListReader.java` then java ListReader) before running the code in `CachePolicies.py`. This will generate the sequence of requests needed from request generator and save them in a text file to be used later on. After that open `CachePolicies.py` using a text editor of your choice. This will call on the main function which runs all the simulations. The following are the inputs, outputs of the implemented functions;

1. fifoCache:Input:Cache Size, Sequence of requests. Output:Hit rate. Calculates hit rate under this policy
2. lruCache:Input:Cache Size, Sequence of requests. Output:Hit rate. Calculates hit rate under this policy
3. lfuCache:Input:Cache Size, Sequence of requests. Output:Hit rate.Calculates hit rate under this policy
4. main:Triggers the simulation process. Obtains the different requests and uses them to obtain hit rates under the different policies. Inputs: None. Outputs: None.
5. plotdistribution: Inputs: Takes in different cache sizes from 10-200, hitrates and the distributions from which they are obtained. Output: Plots the hitrates against the cache sizes for all the cache replacement policies
6. getunif: Generate and return 100,000 requests uniformly distributed on (1,1000). Inputs:None, Outputs: List of requests
7. get_zipF_probs: Generate and return list of zipF probabilities for items on (1,1000). Inputs:none, Outputs:Probabilities.
8. get_Zipf_RVs: Uses zipf probabilities to generate and return random zipf requests. Inputs:None, Outputs:100,000 requests
9. reqgen_RVs: This function obtains the requests obtained from the request generator. outputs list of generated requests. Has no input.
10. inList:Input:Instance of class,value. Output:Boolean. Helper for fifocache function.
11. mostRecent:Input:Instance of class,node object.Output:None. Helper for lrucache function
12. get:Input:Instance of class,value.Output:null. Helper function for lrucache function
13. lowestFreq:Input:Instance of class. Output:null. Helper for lfucache function
11.randomcache:Input:Cache Size, Sequence of requests. Output:Hit rate. Calculates hit rate under this policy


## Installation

Install java, python. Run the files thusly:


```bash
javac ListReader.java
python CachePolicies.py
```