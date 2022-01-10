class Phone:
    pass

phone1 = Phone()
phone2 = Phone()

phone1.model = '13'
phone1.color = 'Gray'
phone1.size = 'Max'
phone1.owner = ""

phone2.model = 'XR'
phone2.color = 'Black'
phone2.size = 'Normal'
phone2.owner = ""

ask = input("What model is your phone? ")

if ask == "13":
    phone1.owner = "Josee"
    phone2.owner = "Spencer"
else:
    phone1.owner = "Spencer"
    phone2.owner = "Josee"

print(phone1.owner)
