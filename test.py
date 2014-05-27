from Channel import Channel

c = Channel("HerraMustikka")
for f in c.get_followers():
    print(f['user']['name'])
    #if f['user']['name'] == 'varesa':
    #    print("Found!")