import facebook

graph = facebook.GraphAPI(access_token='EAACEdEose0cBAB5jmkEZAB8CKzFlrLSfTJcot1JMhzkOgRgYgvgJrr22vzNxLqVYZAgV3QR149ZA9nXsl6ap8chrcZCQE0Od5qZBdUwvnMD6ZC9RDXKkVg0ZAUH5qwIoD6BfuyxSdez2x6kWEYrAIV9fhNUJLxvFFbQLHmMgOdATV23criYsnRr4DyNfZAwJs9IZD', version='2.8')

#friends = graph.get_all_connections(id='me', connection_name='posts')
posts = graph.get_all_connections(id='me', connection_name='posts')
post_ids = []

i=0
for post in posts:
    post_id = post['id']
    post_ids.append(post_id)
    i+=1
    if i>40:
        break

#post_objects = graph.get_objects(ids=post_ids[:40])

num_likes_by_person = {}

for id in post_ids:
    post_reactions = graph.get_all_connections(id=id, connection_name="reactions")
    #print sum(1 for _ in post_reactions)
    for person_object in post_reactions:
        person_id = person_object['name']
        num_likes_by_person[person_id] = num_likes_by_person.get(person_id, 0) + 1

#print num_likes_by_person

final = sorted(num_likes_by_person.items(), reverse=True, key=lambda a:a[1])
final = final[:10]

for person, count in final:
    print person, count
#for post in post_objects:
#    post_reactions = graph.get_all_connections(id=post['id'], connection_name="reactions")

#posts_actual = posts['data']
#print sum(1 for _ in posts_actual)
#post = graph.get_object(id='603417164_10155134270072165')
#print(post['message'])
