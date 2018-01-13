import random
from bookinfo.settings import UAPOOL
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware

class Uamid(UserAgentMiddleware):
    def __int__(self, ua=''):
        self.ua = ua

    def process_request(self, request, spider):
        thisua = random.choice(UAPOOL)
        # print("当前使用的user-agent是:"+thisua)
        request.headers.setdefault('User-Agent', thisua)
