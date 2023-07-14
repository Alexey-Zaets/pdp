class Target:
    """
    The target class declares an interface that client code can work with.
    """
    def request(self):
        return "Target: The default target's behavior."


class Adaptee:
    """
    The custom class contains some useful behavior, but its interface
    incompatible with existing client code. An adaptable class needs
    some rework before client code can use it.
    """
    def specific_request(self):
        return ".eetpadA eht fo roivaheb laicepS"


class Adapter(Target, Adaptee):
    """
    The Adapter makes the interface of the Adapted class compatible
    with the target interface through multiple inheritance.
    """
    def request(self):
        return f"Adapter: (TRANSLATED) {self.specific_request()[::-1]}"


class CompositionAdapter(Target):
    """
    The Adapter makes the interface of the Adapted class compatible
    with the target interface through multiple inheritance.
    Uses composition.
    """
    def __init__(self, adaptee):
        self.adaptee = adaptee

    def request(self):
        return f"Adapter: (TRANSLATED) {self.adaptee.specific_request()[::-1]}"


def client_code(target):
    """
    The client code supports all classes that use the Target interface.

    :param target:
    :return:
    """
    print(target.request(), end='')


if __name__ == '__main__':
    target = Target()
    client_code(target)

    adaptee = Adaptee()
    adapter = Adapter()
    client_code(adapter)

    adapter = CompositionAdapter(adaptee)
    client_code(adapter)