import asyncio
import socket

from LIB.SOCKET import SOCKET


class ServerSock(SOCKET):
    def __init__(self, port):
        super().__init__()
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.PORT = port
        self.ACTIVE_CLIENTS = []

        self.main_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    async def receive_loop(self, client_socket: socket.socket = None):
        pass

    async def send_loop(self):
        pass

    async def main(self):
        pass

    def start(self):
        pass
