class Client:
    def __init__(self, id, fio, date, amount, interest):
        self.id = id
        self.fio = fio
        self.date = date
        self.amount = amount
        self.interest = interest

    def __str__(self):
        return "id " + str(self.id) + ", fio: " + self.fio + ", date: " + self.date + ", amount: " + str(self.amount) + ", inerest: " + str(self.interest)
