from datetime import datetime


class Customer:
    def __init__(self, name, discount_rate) -> None:
        self._name = name
        self._start_date = datetime.today()
        self._discount_rate = discount_rate

    @property
    def discount_rate(self):
        return self._discount_rate

    def _set_discount_rate(self, discount_rate):
        self._discount_rate = discount_rate

    def become_preferred(self):
        self._set_discount_rate(self.discount_rate + 0.03)
        # Other good things...

    def apply_discount(self, amount):
        return amount - amount * self.discount_rate

    def asString(self):
        return f'{self._start_date}: {self.discount_rate}'

