# coding:utf-8

class RelationShip(object):
    __attention = 'weibo.user.attention'  
    __fans = 'weibo.user.fans'

    def __init__(self,client):
	self.client = client
    # L 关注 R
    def attention(self,userIdL,userIdR):
	attention = __attention + userIdL
	fans = __fans + userIdR

	self.client.sadd(attention,userIdR)
	self.client.sadd(fans,userIdL)

	return [1001,{'msg':'success'}]
    
    # A 是否关注 B
    def isFollow(self,userA,userB):
	attention = __attention + userA
	if sismember(attention,userB) == 1:
	    return [1001,{'msg':'已经关注了'}]
	else:
	    return [1001,{'msg':'还没有关注'}]
    
    # A 与 B是否相互关注
    def isFollowEachOther(self,userA,userB):
	attentionA = __attention + userA
	attentionB = __attention + userB
	if sismember(attentionA,userB) == 1 and sismember(attentionB,userA) == 1:
	    return [1001,{'msg':'相互关注'}]
	else:
	    return [1001,{'msg':'没有相互关注'}]

   # 获得用户的所有关注的人
   def getAllFollows(self,userA):
       attentionA = __attention + userA

