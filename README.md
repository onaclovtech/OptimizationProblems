# OptimizationProblems


##Count Ones

    def countOnes(data):
        val = 0
        for i in range(len(data)):
            if (data[i] == '1'):
                val += 1
		#print data[i]
        return str(val)


![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/countones_n_5.png "Count Ones Algorithm N=5")

![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/countones_n_10.png "Count Ones Algorithm N=10")

![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/countones_n_15.png "Count Ones Algorithm N=15")

##Four Peaks

    def fourpeaks(data):
        i = 0
	      t = int(len(data) / 5)
        while (i < len(data) and data[i] == '1'):
            i += 1
        
        head = i
        i = len(data) - 1
        while (i >= 0 and data[i] == '0'):
            i -= 1
       
        tail = len(data) - 1 - i
        r = 0
        if (head > t and tail > t):
            r = len(data)
        
        return max(tail, head) + r
        
![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/fourpeaks_n_5.png "Four Peaks Algorithm N=5")

![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/fourpeaks_n_10.png "Four Peaks Algorithm N=10")

![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/fourpeaks_n_15.png "Four Peaks Algorithm N=15")

##Flip Flop

    def flipflop(data):
        val = 0;
        for i in range(len(data) - 1):
            if (data[i] != data[i + 1]):
                val += 1
        return str(val)
        
![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/flipflop_n_5.png "Flip Flop Algorithm N=5")

![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/flipflop_n_10.png "Flip Flop Algorithm N=10")

![alt text](https://github.com/onaclovtech/OptimizationProblems/blob/master/figures/flipflop_n_15.png "Flip Flop Algorithm N=15")
