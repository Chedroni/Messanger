import asyncio
import socket

from LIB.SOCKET import SOCKET
from SERVER.DB.ServerDB import ServerDB
from SERVER.HANDLERS.ServerReceiveHandler import ServerReceiveHandler
from SERVER.HANDLERS.ServerSendHandler import ServerSendHandler


class ServerSock(SOCKET):
    def __init__(self, port):
        super().__init__()
        self.HOST = socket.gethostbyname(socket.gethostname())
        self.PORT = port
        self.ACTIVE_CLIENTS = []

        self.data_base = ServerDB

        self.receive_handler = ServerReceiveHandler(self)
        self.send_handler = ServerSendHandler(self)

        self.main_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    async def accept_client(self) -> socket.socket:
        client_socket, client_address = await self.main_loop.sock_accept(self.main_sock)

        self.main_loop.create_task(self.receive_loop(client_socket))

        return client_socket

    async def receive_loop(self, client_socket: socket.socket = None):
        pass

    async def send_loop(self):
        pass

    async def accept_clients(self):
        try:
            while True:
                client_socket = await self.main_sock.accept_client()

                self.ACTIVE_CLIENTS.append(client_socket)
        except socket.error:
            pass

    async def main(self):
        pass

    def pre_start(self):
        pass

    def start(self):
        self.main_sock.bind([self.HOST, self.PORT])
