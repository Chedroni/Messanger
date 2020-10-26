import asyncio
import socket

from ClIENT.DB.ClientDB import ClientDB
from LIB.SOCKET import SOCKET


class ClientSock(SOCKET):
    def __init__(self):
        super().__init__()

        self.data_base = ClientDB

    async def connect_to_server(self):
        _SERVER_IP = None
        _SERVER_PORT = None

        await self.main_loop.sock_connect(self.main_sock, [_SERVER_IP, _SERVER_PORT])

    async def receive_loop(self, client_socket: socket.socket = None):
        pass

    async def send_loop(self):
        pass

    async def main(self):
        pass

    def start(self):
        pass
