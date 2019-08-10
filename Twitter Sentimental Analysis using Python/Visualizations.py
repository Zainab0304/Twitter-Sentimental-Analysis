# Visualizations for Twitter Sentimental Analysis in Power BI using Python Scripts

# 1. Polarity vs Time
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

style.use("ggplot")

fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    pullData = dataset['Tweet']
    lines = dataset['Polarity']

    xar = []
    yar = []

    x = 0
    y = 0

    for l in lines:
        x += 1
        if l>0:
            y += 1
        elif l<0:
            y -= 1
        else:
            y=y

        xar.append(x)
        yar.append(y)
    ax1.clear()
    plt.plot(xar,yar)
    plt.xlabel("Time")
    plt.ylabel("Polarity of Sentiment")
    plt.title("Polarity Analysis")
    plt.show()
ani = animation.FuncAnimation(fig, animate, interval=1000)

plt.show()

# 2. Comparative Study of Retweets and Likes vs Time
import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt 
tl = pd.Series(data=dataset['Likes'].values,index=dataset['Time'])
tl.plot(figsize=(16,4),label="likes",legend=True,color='r')
tll = pd.Series(data=dataset['Retweets'].values,index=dataset['Time'])
tll.plot(figsize=(16,4),label="retweets",legend=True, color='b')
plt.title("Comparative Analysis of Likes and Retweets")
plt.show()

# 3. Pie chart of Negative, Positive and neutral Tweets
import matplotlib.pyplot as plt 
import pandas as pd 
colors = ["red", "green", "blue"]
plt.pie(dataset['Time'], labels=dataset['Sentiment'], colors=colors, autopct='%1.1f%%')
plt.title("Sentimental Analysis of Tweets")
plt.show()

# 4. Retweets vs time and Likes vs Time
import matplotlib.pyplot as plt
df=dataset
ylabels = ["Likes","Retweets"]

fig = plt.figure(figsize=(13,3))
fig.subplots_adjust(hspace=0.01,wspace=0.01)

n_row = len(ylabels)
n_col = 1
for count, ylabel in enumerate(ylabels):
    ax = fig.add_subplot(n_row,n_col,count+1)
    ax.plot(df["Time"],df[ylabel])
    ax.set_ylabel(ylabel)
plt.xlabel("Time")
plt.title("Analysis of Likes and Retweets with Time")
plt.show()

# 5. Wordcloud of all the tweets with most Trending words highlighted
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
stopwords = set(STOPWORDS)
#data=dataset['Tweet']
def show_wordcloud(data, title = None):
    wordcloud = WordCloud(
        background_color='white',
        stopwords=stopwords,
        max_words=200,
        max_font_size=40, 
        scale=3,
        random_state=1 # chosen at random by flipping a coin; it was heads
    ).generate(str(data))

    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')
    if title: 
        fig.suptitle(title, fontsize=20)
        fig.subplots_adjust(top=2.3)

    plt.imshow(wordcloud)
    plt.title("Word Cloud of Most Trending Words in Tweets")
    plt.show()

show_wordcloud(dataset['Tweet'])

# 6. Bar graph of Sentiment analysis vs Time
import pandas
import matplotlib.pyplot as plt 
import seaborn as sns

plt.bar(dataset['Sentiment'],dataset['Time'])
plt.ylabel("Time")
plt.title("Sentimental Analysis of Tweets with Time")
plt.show()

# 7. Negative Polarity vs Time
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set(style="darkgrid")
fmri = sns.load_dataset("fmri")
sns.lineplot(x=dataset['Negative_Polarity'], y=dataset['Time'],data=fmri, color='r')
plt.xlabel("Negative")
plt.ylabel("Period of Time")
plt.title("Representation Negative Polarity of Tweets")
plt.show()

# 8. Positive Polarity vs Time
import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 
sns.set(style="darkgrid")
fmri = sns.load_dataset("fmri")
sns.lineplot(x=dataset['Positive_Polarity'], y=dataset['Time'],data=fmri, color='b')
plt.xlabel("Positive")
plt.ylabel("Period of Time")
plt.title("Representation Positive Polarity of Tweets")
plt.show()