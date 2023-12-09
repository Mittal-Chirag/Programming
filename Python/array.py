import numpy as np
import pandas as pd
# a=np.array([1,2,3,4,5,np.NaN])
# b=pd.Series(a)
# print(b)
# print(b.max())
# print(b.min())
# print(b.info)
a=pd.Series([i for i in range(101,106,1)],index=[chr(i) for i in range(65,70,1)],name="Chirag_Mittal")
print(a.info)