import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


klout = pd.read_csv('klout.csv', header=None, names=['data'])


#plt.figure()

klout.plot.hist()
k_desc = klout.describe()
print(k_desc)

#plt.legend().set_visible(False)
plt.axvline(klout['data'].mean(), color='black', linestyle='dashed', linewidth=2, label='Pop mean: {0:.2f}'.format(klout['data'].mean()))


# what if we created samples of 35 observations...what is mean?
# same as pop

#what is SD?

sample_sd = k_desc.loc['std', 'data'] / np.sqrt(35)
print('sample sd is {}\n'.format(sample_sd))


#if sample mean was 40, how many SD would it be away
plt.axvline(40, color='red', linewidth=2, label='new_mean: 40')
new_mean_dist = (40-k_desc.loc['mean','data'])/sample_sd

print('(z score) new mean distance in SDs is: {0:.2f}\n'.format(new_mean_dist))

import scipy.stats as st
prob_from_zscore = st.norm.cdf(new_mean_dist)
print('prob from z score: {0:.2f}'.format(1-prob_from_zscore))


### what happens if we use a sample size of 400 instead


sample_sd_250 = k_desc.loc['std', 'data'] / np.sqrt(250)
print('sample sd  {}\n'.format(sample_sd_250))

new_mean_dist_250 = (40-k_desc.loc['mean','data'])/sample_sd_250
print('(z score) new mean distance in SDs is: {0:.2f}\n'.format(new_mean_dist_250))

import scipy.stats as st
prob_from_zscore = st.norm.cdf(new_mean_dist_250)
print('prob from z score: {0:.4f}'.format(1-prob_from_zscore))

'''

down vote
accepted
+50
What you're looking for is quite simply

In [12]: def normz(val):
   ....:     return scipy.stats.norm.ppf((1+val)/2)
'''


plt.legend()
plt.savefig('klout_his.png',bbox_inches='tight')
#plt.show()
