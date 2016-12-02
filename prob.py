import collections;
import pandas as pd
import matplotlib.pyplot as plt;
import numpy as np
import scipy.stats as stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

c = collections.Counter(x)

total = sum(c.values());

freq_dict = {}
for k, v in c.iteritems():
    print k, v
    freq_dict[k] = float(v) / total;

for key in freq_dict:
    print freq_dict[key]

plt.boxplot(x, notch=True, labels=['Distribution of data'], meanline=True)
plt.savefig("boxplot.png")
plt.clf()

plt.hist(x, bins=10, label="Histogram")
plt.show();
plt.clf()

df = pd.DataFrame(x);
print df[0]

plt.figure()
test_data = np.random.normal(size=1000)
graph1 = stats.probplot(test_data, dist="norm", plot=plt)
plt.show() #this will generate the first graph
plt.figure()
test_data2 = np.random.uniform(size=1000)
graph2 = stats.probplot(test_data2, dist="norm", plot=plt)
plt.show() #this will generate the second graph
