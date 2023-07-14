from abc import ABC, abstractmethod


class AbstractFactory(ABC):

    @abstractmethod
    def create_pistons(self):
        raise NotImplementedError

    @abstractmethod
    def create_crankshaft(self):
        raise NotImplementedError


class GasEngine(AbstractFactory):

    def create_pistons(self):
        return GasPistons()

    def create_crankshaft(self):
        return GasCrankshaft()


class DieselEngine(AbstractFactory):

    def create_pistons(self):
        return DieselPistons()

    def create_crankshaft(self):
        return DieselCrankshaft()


class AbstractPistons(ABC):

    @abstractmethod
    def do_some_staff_with_pistons(self):
        raise NotImplementedError


class GasPistons(AbstractPistons):

    def do_some_staff_with_pistons(self):
        return "Do some staff with gas pistons"


class DieselPistons(AbstractPistons):

    def do_some_staff_with_pistons(self):
        return "Do some staff with diesel pistons"


class AbstractCrankshaft(ABC):

    @abstractmethod
    def do_some_staff_with_crankshaft(self):
        raise NotImplementedError


class GasCrankshaft(AbstractCrankshaft):

    def do_some_staff_with_crankshaft(self):
        return "Do some staff with gas crankshaft"


class DieselCrankshaft(AbstractCrankshaft):

    def do_some_staff_with_crankshaft(self):
        return "Do some staff with diesel crankshaft"


if __name__ == '__main__':
    gas_engine = GasEngine()
    gas_pistons = gas_engine.create_pistons()
    print(gas_pistons.do_some_staff_with_pistons())
    gas_crankshaft = gas_engine.create_crankshaft()
    print(gas_crankshaft.do_some_staff_with_crankshaft())

    diesel_engine = DieselEngine()
    diesel_pistons = diesel_engine.create_pistons()
    print(diesel_pistons.do_some_staff_with_pistons())
    diesel_crankshaft = diesel_engine.create_crankshaft()
    print(diesel_crankshaft.do_some_staff_with_crankshaft())
