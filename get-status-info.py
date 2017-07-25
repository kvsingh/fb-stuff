online = True
import facebook, datetime
from textblob import TextBlob
import csv
writer = csv.writer(open('data-statuses.csv', 'wb'))
writer.writerow(['polarity', 'subjectivity', 'num_reactions', 'length', 'num_words', 'month', 'dow', 'tod', 'year'])

graph = facebook.GraphAPI(
    access_token='youraccesstoken',
    version='2.8')
posts = graph.get_all_connections(id='me', connection_name='posts')

i=0
for post in posts:
    try:
        post_id = post['id']
        status = post['message']

        if online:
            time_string = post['created_time'][:-5]
            time = datetime.datetime.strptime(time_string, '%Y-%m-%dT%H:%M:%S')
        else:
            time = post['time']

        #get features
        blob = TextBlob(status)
        polarity, subjectivity = blob.sentiment
        length = len(status)
        num_words = len(status.split(" "))   #split by other means? ',' etc
        post_reactions = graph.get_all_connections(id=post_id, connection_name="reactions")
        num_reactions = sum(1 for _ in post_reactions)

        month = time.month
        dow = time.weekday()
        tod = time.hour
        year = time.year

        print polarity, subjectivity, num_reactions, length, num_words, month, dow, tod
        writer.writerow([polarity, subjectivity, num_reactions, length, num_words, month, dow, tod, year])

        i+=1
        print i
    except:
        continue

