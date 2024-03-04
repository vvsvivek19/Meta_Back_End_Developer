class Employees:
    def __init__(self, first, last) -> None:
        self.first = first
        self.last = last

class Supervisors(Employees):
    def __init__(self, first, last, password) -> None:
        super().__init__(first, last)
        self.password = password

class Chefs(Employees):
    def leave_request(self, days):
        return "May I take a leave for " + str(days) + " days."
    
adrian = Supervisors("Adrian","A","apple")
emily = Chefs("Emily","E")
juno = Chefs("Juno","J")

print(emily.leave_request(3))
print(adrian.password)
print(emily.first)