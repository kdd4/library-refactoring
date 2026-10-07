from abc import ABC, abstractmethod


class Book:
    REGULAR: int = 0
    NEW_RELEASE: int = 1
    CHILDREN: int = 2

    def __init__(self, title: str, price_code: int):
        self._title = title
        self._price_code = price_code

    @property
    def title(self) -> str:
        return self._title

    @property
    def price_code(self) -> int:
        return self._price_code

    @property
    def fixed_cost(self):
        return {
            self.REGULAR: 2,
            self.CHILDREN: 1.5,
        }.get(self.price_code, 0)

    @property
    def free_days(self):
        return {
            self.REGULAR: 2,
            self.CHILDREN: 3,
        }.get(self.price_code, 0)

    @property
    def daily_cost(self):
        return {
            self.REGULAR: 1.5,
            self.NEW_RELEASE: 3,
            self.CHILDREN: 1.5,
        }.get(self.price_code, 0)

class Rental:
    def __init__(self, book: Book, days_rented: int):
        self._book = book
        self._days_rented = days_rented

    @property
    def book(self) -> Book:
        return self._book

    @property
    def days_rented(self) -> int:
        return self._days_rented

    @property
    def amount(self) -> float:
        amount = self.book.fixed_cost

        paid_days = self.days_rented - self.book.free_days

        if paid_days > 0:
            amount += paid_days * self.book.daily_cost

        return amount

class Client:
    def __init__(self, name: str):
        self._name = name
        self._rentals = []

    def add_rental(self, rental: Rental):
        self._rentals.append(rental)

    @property
    def name(self) -> str:
        return self._name

    def statement(self) -> str:
        total_amount = 0
        frequent_renter_points = 0
        result = f"Rental summary for {self.name}\n"
        
        for rental in self._rentals:
            # add frequent renter points
            frequent_renter_points += 1
            if rental.book.price_code == Book.NEW_RELEASE and rental.days_rented > 1:
                frequent_renter_points += 1

            # show each rental result
            result += f"- {rental.book.title}: {rental.amount}\n"
            total_amount += rental.amount
        
        # show total result
        result += f"Total: {total_amount}\n"
        result += f"Points: {frequent_renter_points}"
        return result