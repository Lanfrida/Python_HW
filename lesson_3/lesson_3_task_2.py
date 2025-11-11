from smartphone import Smartphone

catalog = [

    Smartphone("Apple", "Iphone 13", "+79155556735"),
    Smartphone("Xiaomi", "Redmi Note 10", "+79163538132"),
    Smartphone("Samsung", "S24", "+79268741327"),
    Smartphone("Nokia", "5110", "+79165843192"),
    Smartphone("Motorola", "A1200", "+79253715469")
]
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.number}")