class ApiService:
    total_requests = 0
    def __init__(self,service_name,requests_handled=0):
        self.service_name = service_name
        self.requests_handled = requests_handled
    def handle_requests(self):
        ApiService.total_requests += 1
        self.requests_handled += 1
        return f'Handled by {self.service_name}'
    def stats(self):
        return {
            'service' :f'{self.service_name}',
            'handled': self.requests_handled,
            'global_requests': ApiService.total_requests
        }
s1 = ApiService("Auth")
s2 = ApiService("Payments")

s1.handle_requests()
s1.handle_requests()
s2.handle_requests()

print(s1.stats())
print(s2.stats())