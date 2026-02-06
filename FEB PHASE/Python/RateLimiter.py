class RateLimiter:
    def __init__(self,limit:int):
        if not isinstance(limit,int) or limit<=0:
            raise  ValueError('Limit can numeric and positive only')
        self.limit = limit
        self.requests = {}
    def allow_request(self,user_id):
        if not isinstance(user_id,int):
            return False
        count = self.requests.get(user_id,0)

        if count>= self.limit:
            return False
        
        self.requests[user_id] = count +1
        return True
rl = RateLimiter(2)
rl.allow_request(1)  # True
rl.allow_request(1)  # True
rl.allow_request(1)  # False
rl.allow_request(2)  # True
