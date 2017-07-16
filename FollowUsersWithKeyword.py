import tweepy
from tweepy import OAuthHandler


token = "token"
secret = "secret"

CONSUMER_KEY = "key"
CONSUMER_SECRET = "secret"

auth = OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(token, secret)
api = tweepy.API(auth)


users = []

##Search maximum amount of users that match the keyword
for i in range(0,51):

    print(i)
    
    ##Specify the keyword at "your keyword"
    data = api.search_users("your keyword", 20,i)

    for i in range(len(data)):

        user = data[i]._json
        users.append(user["screen_name"])

followed = [];
for u in range(0,len(users),100):

    print(u)

    if u + 100 > len(users):
        
        relationships = api.lookup_friendships(screen_names=users[u:len(users)])
    else:
        
        relationships = api.lookup_friendships(screen_names=users[u:u+100])

    for relationship in relationships:
        
        ##If we are not yet following, follow the user
        if not relationship.is_following:

            print(relationship.screen_name)
            
            try:
                api.create_friendship(relationship.screen_name)
            except Exception:
                pass

print(users[0])
