import asyncio
import socket

from LIB.SOCKET import SOCKET


class ClientSock(SOCKET):
    def __init__(self):
        super().__init__()

    async def receive_loop(self, client_socket: socket.socket = None):
        pass

    async def send_loop(self):
        pass

    async def main(self):
        pass

    def start(self):
        pass
