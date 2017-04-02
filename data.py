#pandas yahoo and xom basic _____________________

"""import pandas as pd
import datetime
#import pandas.io.data as web
from pandas_datareader import data, wb
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')



df = data.DataReader("XOM", "yahoo", "2015-2-1", "2016-2-1")

print(df.head())

df['Adj Close'].plot()

plt.show()"""

#________________________


import pandas as pd
import matplotlib.pyplot as plt 
from matplotlib import style

style.use('ggplot')

web_stats = {'Day' : [1,2,3,4,5,6],
			 'Visitors' : [43,53,34,45,57,78],
			 'Bounce_rate' : [65,72,54,67,57,45]}

df = pd.DataFrame(web_stats)

print (df.set_index('Day'))


