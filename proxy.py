import datetime
from functools import wraps


def logger_proxy(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Server.LOGS.append({time: f})

    return wrapper


class Server:
    _instance = None
    LOGS = []

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    @logger_proxy
    def receive_request(self):
        print('Server received request:')
        return 'received request'

    @logger_proxy
    def send_response(self):
        print('Server sent response to request: ')
        return 'sent response'


if __name__ == '__main__':
    server = Server()
    server.receive_request()
    server.send_response()
    print(server.LOGS)

