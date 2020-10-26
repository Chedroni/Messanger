import socket

from SERVER.ServerSock import ServerSock


class ServerReceiveHandler:
    def __init__(self, serv_sock: ServerSock):
        self.serv_sock = serv_sock

        self.DATA_LIST = dict[socket.socket, bytes]

    async def handle(self, client_socket: socket.socket):
        while True:
            data = await self.serv_sock.receive_data(client_socket)

    def main(self):
        pass
