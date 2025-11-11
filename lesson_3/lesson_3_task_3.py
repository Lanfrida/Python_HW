from address import Address
from mailing import Mailing 

to_address = Address("127247", "Москва", "Бескудниковский бульвар", "29", "1")
from_address = Address("367891", "Санкт-Петербург", "Приморский", "5", "15")

mailing = Mailing(
    to_address = to_address,  
    from_address = from_address, 
    cost = 250,
    track = "Track123456789"
)

print(mailing)