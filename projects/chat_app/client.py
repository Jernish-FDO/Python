import socket
import threading

# The User Interface for our chat, buddy!
class ChatClient:
    def __init__(self, nickname, host='127.0.0.1', port=55555):
        self.nickname = nickname
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((host, port))

    def receive(self):
        while True:
            try:
                message = self.client.recv(1024).decode('ascii')
                if message == 'NICK':
                    self.client.send(self.nickname.encode('ascii'))
                else:
                    print(message)
            except:
                print("❌ An error occurred!")
                self.client.close()
                break

    def write(self):
        while True:
            msg = input('')
            message = f'{self.nickname}: {msg}'
            self.client.send(message.encode('ascii'))

    def start(self):
        receive_thread = threading.Thread(target=self.receive)
        receive_thread.start()

        write_thread = threading.Thread(target=self.write)
        write_thread.start()

if __name__ == "__main__":
    nick = input("Choose your nickname, buddy: ")
    client = ChatClient(nick)
    client.start()
