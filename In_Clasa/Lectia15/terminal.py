
class Terminal:
    def __init__(self):
        self.last_ticket = 1
        self.clients = []
        self.current_client = {}
        self.operators = [{
            "name": "Ion",
            "speciality": "C"
        }]
    #cream ticket nou
    def create(self, type: str):
        # C - Consultanta, S - Suport
        client = {
            "type": type,
            "number": self.last_ticket,
            "code": f"{type}{self.last_ticket}"
        }
        print(f"Client nou: {client['code']}")
        self.clients.append(client)

        self.last_ticket += 1
        return client
    def add_operator(self, name, speciality):
        print(self.operators)
        operator = {
            "name": name,
            "speciality": speciality
        }
        self.operators.append(operator)
        print(f"Am adaugat operatorul {name}")
        print(self.operators)
    def extract(self, operator_name): # extragem 
        if len(self.clients) == 0:
            return False
        
        spec = [item["speciality"] for item in self.operators if item["name"] == operator_name][0]
        print(spec)
        for i, ticket in enumerate(self.clients):
            if ticket['type'] == spec:
                self.current_client = self.clients.pop(i)
                break # pentru a vizualiza clientul curent
        print(f"Clientul curent: {self.current_client['code']}, Ramasi: {len(self.clients)}")
        return self.current_client
    
atm = Terminal()

atm.extract("Ion")
atm.add_operator("Ana", "S")

atm.create("C")
atm.create("S")
atm.create("C")
atm.create("C")
atm.create("S")


atm.extract("Ion")
atm.create("C")

atm.extract("Ana")