
# These functions came from github.com/pushkar/ABAGAIL
import math
import matplotlib.pyplot as plt

def countOnes(data):
        val = 0
        for i in range(len(data)):
            if (data[i] == '1'):
                val += 1
		#print data[i]
        return str(val)

def flipflop(data):
        val = 0;
        for i in range(len(data) - 1):
            if (data[i] != data[i + 1]):
                val += 1
        return str(val)
    

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
    

count = []
flip = []
four = []

for i in range(int(math.pow(2,15))):
	count.append(countOnes('{0:015b}'.format(i)))
	flip.append(flipflop('{0:015b}'.format(i)))
        four.append(fourpeaks('{0:015b}'.format(i)))

plt.figure('Count Ones N=15')
plt.title('Count Ones N=15')
plt.plot(count)
plt.savefig('figures/countones_n_15.png')
plt.figure('Flip Flop N=15')
plt.title('Flip Flop N=15')
plt.plot(flip)
plt.savefig('figures/flipflop_n_15.png')
plt.figure('Four Peaks N=15')
plt.title('Four Peaks N=15')
plt.plot(four)
plt.savefig('figures/fourpeaks_n_15.png')

count = []
flip = []
four = []
for i in range(int(math.pow(2,10))):
	count.append(countOnes('{0:010b}'.format(i)))
	flip.append(flipflop('{0:010b}'.format(i)))
	four.append(fourpeaks('{0:010b}'.format(i)))

plt.figure('Count Ones N=10')
plt.title('Count Ones N=10')
plt.plot(count)
plt.savefig('figures/countones_n_10.png')
plt.figure('Flip Flop N=10')
plt.title('Flip Flop N=10')
plt.plot(flip)
plt.savefig('figures/flipflop_n_10.png')
plt.figure('Four Peaks N=10')
plt.title('Four Peaks N=10')
plt.plot(four)
plt.savefig('figures/fourpeaks_n_10.png')

count = []
flip = []
four = []
for i in range(int(math.pow(2,5))):
	count.append(countOnes('{0:05b}'.format(i)))
	flip.append(flipflop('{0:05b}'.format(i)))
	four.append(fourpeaks('{0:05b}'.format(i)))

plt.figure('Count Ones N=5')
plt.title('Count Ones N=5')
plt.plot(count)
plt.savefig('figures/countones_n_5.png')
plt.figure('Flip Flop N=5')
plt.title('Flip Flop N=5')
plt.plot(flip)
plt.savefig('figures/flipflop_n_5.png')
plt.figure('Four Peaks N=5')
plt.title('Four Peaks N=5')
plt.plot(four)
plt.savefig('figures/fourpeaks_n_5.png')
#plt.show()
