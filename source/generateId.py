# coding:utf-8
class Generate:
    def __init__(self,client,key):
	self.client = client
	self.key = key

    def init(self,n):
	self.client.set(self.key,n);

    def gen(self):
	newId = self.client.incr(self.key,1)
	return int(newId)

