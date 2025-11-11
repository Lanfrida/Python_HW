from address import Address

class Mailing:
    def __init__(self, to_address, from_address, cost, track):
        self.to_address = to_address
        self.from_address = from_address
        self.cost = cost
        self.track = track

    def __str__(self):
        from_addr = self.from_address
        to_addr = self.to_address
        return f"Отправление {self.track} из {from_addr.index}, {from_addr.city}, {from_addr.street}, {from_addr.house} - {from_addr.apartment} в {to_addr.index}, {to_addr.city}, {to_addr.street}, {to_addr.house} - {to_addr.apartment}. Стоимость {self.cost} рублей."