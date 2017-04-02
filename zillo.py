import quandl
import pandas as pd
import ssl

api_key = "A-ZstTgSgsTsS3-XdHV-"

#df = quandl.get("FMAC/HPI_AK", authtoken = api_key)
#print(df.head())
ssl._create_default_https_context = ssl._create_unverified_context

us_states = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#print(us_states[0][0])

main_df = pd.DataFrame()

for abbv in us_states[0][0][1:]:
	query = "FMAC/HPI_"+str(abbv)
	df = quandl.get(query, authtoken = api_key)
	df.columns = [str(abbv)]

	if main_df.empty:
		main_df = df
	else:
		main_df = main_df.join(df)

print(main_df.head())



