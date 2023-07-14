from abc import ABC, abstractmethod


class VehicleCreator(ABC):

    @abstractmethod
    def factory_method(self):
        raise NotImplementedError

    def operation(self):
        vehicle = self.factory_method()
        return vehicle.drive()


class TruckCreator(VehicleCreator):

    def factory_method(self):
        return Truck()


class BusCreator(VehicleCreator):

    def factory_method(self):
        return Bus()


class Vehicle(ABC):

    @abstractmethod
    def drive(self):
        raise NotImplementedError


class Truck(Vehicle):

    def drive(self):
        return 'Drive truck'


class Bus(Vehicle):

    def drive(self):
        return 'Drive bus'


if __name__ == '__main__':
    print(BusCreator().operation())
