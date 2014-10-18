### 1. 微博的功能

    1.1 存储用户账号
    1.2 关注与被关注
    1.3 发微博
    1.4 微博时间线
    1.5 点赞、评论和转发

### 2. 存储用户账号实现详解
    
    1. 用户的基本信息:name、email、password;存放的数据结构为hash表，用一个唯一的Id存放用户的所有信息；
    2. 规则1：name、email不能重复;所以要维护name和email的集合(set)，用来保证当一个用户注册的时候可以进行判断;
    3. 规则2: 每一个用户都有一个独一无二的id,叫做userId;使用generateId来生成userId
    4. 动作:
	    4.1 注册: register(name,email,password)
	    4.2 登录: login(name or email,password)
	    4.3 生成userId: generateId()
