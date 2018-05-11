import pandas as pd
import numpy as np
import progressbar
from time import sleep

bar = progressbar.ProgressBar(maxval=2**27, \
    widgets=[progressbar.Bar('=', '[', ']'), ' ', progressbar.Percentage()])
csv = pd.read_csv("learnedindexstructures/bucket/out.csv")
df = pd.DataFrame(csv)
df.columns = ['a']
y=0
e=0.0
initVal = 0
i=0
emax = 0
per = 1
maxval = 2**27
bar.start()
while (i<(maxval)):
    bar.update(i+1)
    beta = np.random.beta(1,(2 * 10**9)-i) # This is a float from 0 to 1
    nextVal = (1-initVal)*beta+initVal
    initVal = nextVal
    e = y - ((2* 10**9) * nextVal)
    emax = max(emax, e)
    y=y+1
    i=i+1
bar.finish()
print(emax)
