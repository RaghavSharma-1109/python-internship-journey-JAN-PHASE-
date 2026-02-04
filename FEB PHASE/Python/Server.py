class Server:
    total_requests = 0
    def __init__(self,server_name):
        self.server_name = server_name
    
    def handle_request(self):
        Server.total_requests +=1
        return f'Request is handled by server: {self.server_name}'
server1 = Server("Server-A")
server2 = Server("Server-B")

print(server1.handle_request())
print(server2.handle_request())
print(server1.handle_request())

print("Total requests:", Server.total_requests)
