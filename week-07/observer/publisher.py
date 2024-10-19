"""
Observer Pattern.

Adapted From:
https://refactoring.guru/design-patterns/observer/python/example#example-0--main-py
"""
from abc import ABC, abstractmethod
from random import randrange


class Publisher(ABC):
    """Declares a set of methods for managing subscribers."""

    @abstractmethod
    def attach(self, subscriber):
        """Attach a subscriber to the publisher."""

    @abstractmethod
    def detach(self, subscriber):
        """Detach a subscriber from the publisher."""

    @abstractmethod
    def notify(self):
        """Notify all subscribers about an event."""


class ConcretePublisher(Publisher):
    """Concrete Publisher."""

    def __init__(self):
        """Init the Publisher."""
        self._state = None
        self._subscriber = []

    def get_state(self):
        """Get the Publisher State."""
        return self._state

    def attach(self, subscriber):
        """Attach a new subscriber."""
        print("Publisher: Attached a subscriber.")
        self._subscriber.append(subscriber)

    def detach(self, subscriber):
        """Detach the specified subscriber."""
        self._subscriber.remove(subscriber)

    def notify(self):
        """Notify all subscribers."""
        print("Publisher: Notifying subscribers...")
        for subscriber in self._subscriber:
            subscriber.update(self)

    def run_business_logic(self):
        """Run Business Logic."""
        print("Publisher: I'm doing something important.")
        random_num = str(randrange(0, 3))
        steps = {
            "0":"Step 0",
            "1":"Step 1",
            "2":"Fail",
        }
        self._state = steps[random_num]

        print(f"Publisher: My state has just changed to: {self._state}")
        self.notify()
