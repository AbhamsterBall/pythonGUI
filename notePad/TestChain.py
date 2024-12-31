# 定义一个处理请求的接口
class Handler:
    def __init__(self, successor=None):
        self._successor = successor

    def handle_request(self, request):
        pass

# 具体处理者1
class ConcreteHandler1(Handler):
    def handle_request(self, request):
        if request == "request1":
            print("ConcreteHandler1: Handling request1.")
        else:
            if self._successor:
                self._successor.handle_request(request)

# 具体处理者2
class ConcreteHandler2(Handler):
    def handle_request(self, request):
        if request == "request2":
            print("ConcreteHandler2: Handling request2.")
        else:
            if self._successor:
                self._successor.handle_request(request)

# 客户端使用责任链
def client():
    handler1 = ConcreteHandler1()
    handler2 = ConcreteHandler2(handler1)  # 设置handler1为handler2的后继处理者

    handler2.handle_request("request1")  # 由handler1处理
    handler2.handle_request("request2")  # 由handler2处理
    handler2.handle_request("request3")  # 无处理者处理

client()
