class Phone:
    def __init__(self, model, color, size, owner):
        self.model = model
        self.color = color
        self.owner = owner
        self.size = size
    def owner_model(self):
        return '{} {}'.format(self.owner, self.model)

phone1 = Phone('13', 'Gray', 'Max', 'Josee')
phone2 = Phone('XR', 'Black', 'Normal', 'Spencer')

print(phone1.owner_model())
