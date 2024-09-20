import datetime
from functools import wraps
from abc import ABC, abstractmethod


def logger_proxy(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        f = func(*args, **kwargs)
        time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        Server.LOGS.append({time: f})

    return wrapper


class Singleton(type):
    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance


class AbstractServer(metaclass=Singleton):
    @abstractmethod
    def receive_request(self):
        pass

    def send_response(self):
        pass


class Server(AbstractServer):
    _instance = None
    LOGS = []

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

