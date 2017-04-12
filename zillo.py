import quandl
import pandas as pd
import ssl
import pickle
import matplotlib.pyplot as plt 
from matplotlib import style


#using styles from matplot
style.use("fivethirtyeight")


#apikey for quandl site
api_key = "A-ZstTgSgsTsS3-XdHV-"

ssl._create_default_https_context = ssl._create_unverified_context


#reading abbv from wiki and returning first column
def state_list():
	us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
	return us_states[0][0][1:]


#grabbing state data using quandl
def grab_state__data():
	states = state_list()
	main_df = pd.DataFrame()

	for abbv in states:
		query = "FMAC/HPI_"+str(abbv)
		df = quandl.get(query, authtoken = api_key)
		df.columns = [str(abbv)]

		if main_df.empty:
			main_df = df
		else:
			main_df = main_df.join(df)
	print(main_df.head())

	pickle_out = open("us_states.pickle", "wb")
	pickle.dump(main_df, pickle_out)
	pickle_out.close()

#grab_state__data()

pickle_in = open("us_states.pickle", "rb")
hpi_data = pickle.load(pickle_in)
hpi_data.plot()
plt.legend().remove()
plt.show()


