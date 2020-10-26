import asyncio
import socket

from LIB.DB import DB
from LIB.ENCRYPTOR import ENCRYPTOR


class SOCKET:
    def __init__(self):
        self.TASKS = []

        self.ENCRYPTOR = ENCRYPTOR()

        self.data_base = DB

        self.main_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        self.main_loop = asyncio.get_event_loop()

    async def send_data(self, data: bytes, client_socket: socket.socket):
        await self.main_loop.sock_sendall(client_socket, data)

    async def receive_data(self, client_socket: socket.socket) -> bytes:
        receive_data: bytes = await self.main_loop.sock_recv(client_socket, 1024)
        return receive_data

    async def receive_loop(self, client_socket: socket.socket = None):
        raise NotImplementedError

    async def send_loop(self):
        raise NotImplementedError

    async def main(self):
        raise NotImplementedError

    def start(self):
        raise NotImplementedError
