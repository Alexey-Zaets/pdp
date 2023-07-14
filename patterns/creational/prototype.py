import copy


class Entity:

    def __init__(self):
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent


class Component:

    def __init__(self, integer, list_of_objects, reference):
        self.integer = integer
        self.objects = list_of_objects
        self.reference = reference

    def copy(self):
        return type(self)(
            self.integer, copy.copy(self.objects), copy.copy(self.reference)
        )

    def deep_copy(self):
        return type(self)(
            self.integer, copy.deepcopy(self.objects), copy.deepcopy(self.reference)
        )


if __name__ == '__main__':
    objects = [{1, 2, 3}, 5, {'a': 1, 'b': 2}, [1, 2, 3]]
    circular_ref = Entity()
    component = Component(1, objects, circular_ref)
    circular_ref.set_parent(component)

    copied_component = component.copy()
    assert copied_component.integer == 1
    assert copied_component.objects == objects
    assert copied_component.reference == circular_ref

    deep_copied_component = component.deep_copy()
    assert deep_copied_component.integer == 1
    assert deep_copied_component.objects == objects
    # deep_copied_component.reference != reference ???
    assert deep_copied_component.reference == circular_ref
