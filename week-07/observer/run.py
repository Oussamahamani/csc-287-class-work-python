"""
Observer Pattern.

Adapted From:
https://refactoring.guru/design-patterns/observer/python/example#example-0--main-py
"""
from publisher import ConcretePublisher
from subscriber import ConcreteSubscriberA
from subscriber import ConcreteSubscriberB
from subscriber import ConcreteSubscriberC

# The client code.

publisher = ConcretePublisher()

subscriber_a = ConcreteSubscriberA()
publisher.attach(subscriber_a)

subscriber_b = ConcreteSubscriberB()
publisher.attach(subscriber_b)

subscriber_c = ConcreteSubscriberC()
publisher.attach(subscriber_c)

publisher.run_business_logic()
publisher.run_business_logic()
