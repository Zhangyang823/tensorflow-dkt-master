import numpy as np
import pandas as pd
x =[[1,2,2],[4,5,6]]
index=['a','b']
clo = ['c','d','e']
df = pd.DataFrame(x,index=index,columns=clo)
print(df.loc['b':,['c','d']])
