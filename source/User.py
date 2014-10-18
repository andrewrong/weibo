# coding:utf-8

import redis
from generateId import Generate
import string

class User(object):
    # 用户信息存储字段
    __userInfo = 'weibo.user.'
    # 存放所有email字段
    __email = 'weibo.user.email'
    # 存放所有name字段
    __name = 'weibo.user.name'
    # 存放所有从email到id的字段
    __emailtoid = 'weibo.user.idtoemail'
    # 存放所有从name到id的字段
    __nametoid = 'weibo.user.idtoeamil'
    # 用户生成userId的生成器
    __generate = null

    def __init__(self,client):
	self.client = client
	if __generate == null:
	    __generate = Generate(client,'weibo.user.userId')
	    __generate.init(0)

    # 注册模块
    def register(self,name,email,passwd):
	if self.client.sismember(__email,email):
	    return [4004,{'error':'此邮箱已经被人注册'}]
	if self.client.sismember(__name,name):
	    return [4004,{'error':'此用户名已经被人注册'}]

	userId = self.__gennrateId()
	userIdKey = __userInfo + userId

	# 保存用户信息
	self.client.hset(userId,'userId',userId)
	self.client.hset(userId,'name',name)
	self.client.hset(userId,'email',email)
	self.client.hset(userId,'password',passwd)

	# 将name 和 email存放到相应的集合中
	self.client.sadd(__name,name)
	self.client.sadd(__email,email)

	# 将email和name 与Id进行关联
	self.client.hset(__emailtoid,email,userId)
	self.client.hset(__nametoid,name,userId)

	return userId

    # 登录模块
    def login(name,password):
	key = __nametoid
	if find(name,'@') != -1:
	    key = __emailtoid

	userId = self.client.hget(key,name)

	if userId == null:
	    return [4004,{"msg":"不存在该用户"}]
	userId = __userInfo + userId
	passwd = self.client.hget(userId,'password')
	
	if password == passwd:
	    return [1001,{'msg':'登录成功'}]
	else:
	    return [4004,{'msg':'密码or 用户名错误'}]
	
    def __gennrateId():
	return __gennrate.gen()
