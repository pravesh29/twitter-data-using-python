from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import json
import re



#Variables that contains the user credentials to access Twitter API 
access_token = "846219345739108352-0LJBu7PSpB4mOU0JHvJR3G18WhWCs7A"
access_token_secret = "cdF052xBilGKFrFF5rmdx3H3N7Nbn9lspN4sLmx8JdZPJ"
consumer_key = "70jcdtJgu6RQK2rbfR6F2llrY"
consumer_secret = "FAXba9Z9si48tY7a84H022fUF16m4wWDqedq4Qv4mWVGQR9zG9"


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        print ("data", data)
        return True

    def on_error(self, status):
        print ("status")


if __name__ == '__main__':

    #This handles Twitter authentication and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)

    #This line filter Twitter Streams to capture data by the keywords
    stream.filter(track=['dollar'] )

    