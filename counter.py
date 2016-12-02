import collections;
l = [1, 4, 5, 6, 9, 9, 9];
print l;

#a counter is a dict subclass
count = collections.Counter(l);
#Counter({1: 10, 2: 10, 3: 10, 4: 10})

#This will print all the methods associated with an object
print dir(count);

#Unique functions (besides those available from all dictionaries)
#elements prints an element out the number of counts it has
print count.elements();
print list(count.elements());

#most common (self explanatory)
#subtract (object mapping)

totala = len(list(count.elements()));
totalb = 0;
for x in count.values():
    totalb += x;
print totala;
print totalb;

print count;
for k,v in count.iteritems():
    print k, v, float(v)/totalb;

# sum(c.values())                 # total of all counts
# c.clear()                       # reset all counts
# list(c)                         # list unique elements
# set(c)                          # convert to a set
# dict(c)                         # convert to a regular dictionary
# c.items()                       # convert to a list of (elem, cnt) pairs
# Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
# c.most_common()[:-n-1:-1]       # n least common elements
# c += Counter()                  # remove zero and negative counts


import matplotlib.pyplot as plt
x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]
plt.boxplot(x)
plt.show()


# You can save the plot by using the savefig() function in pyplot
# instead of show(). You call it on the plt object and pass in the
#  filename you wish to use. For example, to save the file as "boxplot.png",
#  you'd type plt.savefig("boxplot.png"). This will save the current plt object
#  with the filename you specified.


plt.hist(x, histtype='bar')
plt.show()



##QQ plots and examples of distributions
import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph
