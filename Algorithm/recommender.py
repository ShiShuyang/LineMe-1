import MysqlAPI

'''
Ref:
http://ocelma.net/software/python-recsys/build/html/quickstart.html
'''

def frindOfFriend(user, pairs, userlist, limit = 30):
    d = dict.fromkeys(userlist)
    for i in d:
        d[i] = []
    for pair in pairs:
        d[pair[0]].append(pair[1])
        d[pair[1]].append(pair[0])
    friendCnt = dict.fromkeys(userlist, 0)
    for i in d[user]:
        d[i] = list(set(d[i]))
        for j in d[i]:
            friendCnt[j] += 1
    friendCnt = zip(friendCnt.keys(), friendCnt.values())
    friendCnt.sort(key = lambda x:x[1], reverse = True)
    return zip(*friendCnt)[0][1:limit+1]

def main(group, user):
    userList = MysqlAPI.getNameList(group)
    pairs = MysqlAPI.getPairs(group)
    return frindOfFriend(user, pairs, userlist)   

def test():
    user = 1
    userlist = range(10)
    pairs = [(0, 1), (3, 4), (1, 3), (1, 5), (6, 8), (5, 8), (8, 3)]
    print frindOfFriend(user, pairs, userlist)

if __name__ == '__main__':
    test()
