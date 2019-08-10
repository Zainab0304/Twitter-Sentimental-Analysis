import tweepy			#puthon library for accessing Twitter API
import pandas as pd		#Python library for Data Analysis and Dataframes
import ssl			#Secure Socket layer
import datetime			#formatting date time
from textblob import TextBlob

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context
ti=list()
td=list()
tw=list()
sen=list()
tu=list()
tl=list()
tr=list()
tll=list()
tp=list()
pos=list()
neg=list()
neu=list()
pt=list()
nt=list()
net=list()
pu=list()
nu=list()
neui=list()
posd=dict()
negd=dict()
neud=dict()
data = dict()

consumer_key = "Enter Consumer key here"
consumer_secret = "Enter Consumer secret key here"
access_token = "Enter access token key here"
access_token_secret = "Enter access token secret key here"

q="370"

limit=300
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True)

for tweet in tweepy.Cursor(api.search,q,lang="en",since="2019-08-05").items(limit):
    if 'RT @' not in tweet.text:
        t=datetime.datetime.time(tweet.created_at)	#Extracting Time of tweet
        t0=datetime.datetime.date(tweet.created_at)	#Extracting Date of tweet
        t1=tweet.text					#Extracting Tweet Text
        t2=tweet.user.screen_name			#Extracting User Screen name
        t3=tweet.retweet_count				#Extracting Retweet Count
        t4=tweet.favorite_count				#Extracting Number of Likes for Twwets
        t5=tweet.user.location 				#Extracting Location of Tweet
        analysis = TextBlob(tweet.text)
        pol=analysis.sentiment.polarity			#Calculate Polarity Score
        if analysis.sentiment.polarity < 0:
            sent = "negative"
            neg.append(pol)
	    nt.append(t)
            nu.append(t2)
        elif analysis.sentiment.polarity == 0:
            sent = "neutral"
            neu.append(pol)
	    net.append(t)
            neui.append(t2)
        else:
            sent = "positive"
            pos.append(pol)
	    pt.append(t)
            pu.append(t2)
        ti.append(t)
        td.append(t0)
        tw.append(t1.encode('utf-8'))
        sen.append(sent)
        tr.append(t3)
        tu.append(t2)
        tl.append(t4)
        tll.append(t5.encode('utf-8'))
        tp.append(pol)

data = {'Tweet':tw,'Time':ti,'Date':td,'Retweets':tr,'Likes':tl,'Sentiment':sen,'User':tu,'Location':tll,'Polarity':tp}		#Store data in dictionary
twitter=pd.DataFrame(data)		#Using pandas to create Datafra
posd = {'Positive_Polarity':pos,'Time':pt,'User ID':pu}
Positive=pd.DataFrame(posd)
negd = {'Negative_Polarity':neg,'Time':nt,'User ID':nu}
Negative=pd.DataFrame(negd)
neud = {'Neutral_Polarity':neu,'Time':net,'User ID':neui}
Neutral=pd.DataFrame(neud)
