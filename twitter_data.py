from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time

ckey = "D6t4Bk0ljUfWYozH5aiME7xF4"
csecret = "6nSs8bE1qA78aa6CUlOj196YMdtXZUfeG2pppbJYdkAMV2aNqs"
atoken = "2256809348-fSHxjx0o6dnbbm7aMaFCwndlMwR6rSS7txCCrwP"
asecret = "AYUJ5WCFbfW9gYcXvBEzd6r6jKpFYVnnoS0V0rFDrFz5b"


class listener(StreamListener):

	def on_data(self,data):

		try:
			print(data)
			tweet_data = open('tweets_data.csv', 'a')
			tweet_data.write(data)
			tweet_data.write('\n')
			tweet_data.colse()
			return True

		except BaseException as e:
			print("failed", str(e))
			time.sleep(5)

	def on_error(self,data):
		print(status)

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)
twitterStream = Stream(auth, listener())
twitterStream.filter(track=["crive"])

