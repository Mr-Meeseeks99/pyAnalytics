#Topic:Correlation, Covariance,
#-----------------------------
#libraries

#The difference between variance, covariance, and correlation is:

#Variance is a measure of variability from the mean
#Covariance is a measure of relationship between the variability of 2 variables - covariance is scale dependent because it is not standardized
#Correlation is a of relationship between the variability of of 2 variables - correlation is standardized making it not scale dependent


import pandas as pd
import numpy as np


# Setting a seed so the example is reproducible
np.random.seed(4272018)
df = pd.DataFrame(np.random.randint(low= 0, high= 20, size= (5, 2)),  columns= ['Commercials Watched', 'Product Purchases'])
df
df.agg(["mean", "std"])
df.cov()
df.corr()


#skewness & Kurtosis
#%matplotlib inline
import numpy as np
import pandas as pd
from scipy.stats import kurtosis
from scipy.stats import skew

import matplotlib.pyplot as plt

plt.style.use('ggplot')

data = np.random.normal(0, 1, 10000000)
np.var(data)

plt.hist(data, bins=60)

print("mean : ", np.mean(data))
print("var  : ", np.var(data))
print("skew : ",skew(data))
print("kurt : ",kurtosis(data))
#https://www.spcforexcel.com/knowledge/basic-statistics/are-skewness-and-kurtosis-useful-statistics
#https://www.researchgate.net/post/What_is_the_acceptable_range_of_skewness_and_kurtosis_for_normal_distribution_of_data distribution



import numpy as np
from scipy.stats import kurtosis, skew

x_random = np.random.normal(0, 2, 10000)

x = np.linspace( -5, 5, 10000 )
y = 1./(np.sqrt(2.*np.pi)) * np.exp( -.5*(x)**2  )  # normal distribution

np.skew(y)

import matplotlib.pyplot as plt

f, (ax1, ax2) = plt.subplots(1, 2)
ax1.hist(x_random, bins='auto')
ax1.set_title('probability density (random)')
ax2.hist(y, bins='auto')
ax2.set_title('(your dataset)')
plt.tight_layout()

from pydataset import data
mtcars = data('mtcars')
mtcars.head()
dataDF = mtcars
dataDF.dtypes
dataDF.head()
dataDF.columns

sk = skew(dataDF)
sk
Col = np.array(dataDF.columns)
Col
pd.concat([pd.Series(Col), pd.Series(sk)], axis=1, sort=False)
kt = kurtosis(dataDF)
kt
pd.concat([pd.Series(Col), pd.Series(kt)], axis=1, sort=False)
cov = dataDF.cov()
cov
cor = dataDF.corr()
cor
plt.hist(dataDF.mpg, bins=60)
plt.xlabel("mpg", size = 14)
plt.hist(dataDF.cyl, bins=60)
plt.xlabel("cyl", size = 14)
plt.hist(dataDF.disp, bins=60)
plt.xlabel("disp", size = 14)
plt.hist(dataDF.hp, bins=60)
plt.xlabel("hp", size = 14)
plt.hist(dataDF.drat, bins=60)
plt.xlabel("drat", size = 14)
plt.hist(dataDF.wt, bins=60)
plt.xlabel("wt", size = 14)
plt.hist(dataDF.qsec, bins=60)
plt.xlabel("qsec", size = 14)
plt.hist(dataDF.vs, bins=60)
plt.xlabel("vs", size = 14)
plt.hist(dataDF.am, bins=60)
plt.xlabel("am", size = 14)
plt.hist(dataDF.gear, bins=60)
plt.xlabel("gear", size = 14)
plt.hist(dataDF.carb, bins=60)
plt.xlabel("carb", size = 14)

dataDF.skew()
dataDF.kurtosis()

