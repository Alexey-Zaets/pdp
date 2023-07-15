# personal development plan
## Algorithms
### Sorting algorithms
#### Sorting algorithm selection criteria
| Criteria                                    | Sorting algorithm                              |
|:------------------------------------------- |:-----------------------------------------------|
| Only a few items                            | Insertion sort                                 |
| The elements are almost sorted already      | Insertion sort                                 |
| Worst case performance matters              | Heapsort                                       |
| Performance is important in the middle case | [Quick sort](algorithms/sorting/quick_sort.py) |
| Evenly distributed elements                 | Block sort                                     |
| As little code as possible                  | Insertion sort                                 |
| Sort stability required                     | [Merge sort](algorithms/sorting/merge_sort.py) |

## Design patterns
### Creational Design Patterns:
Responsible for convenient and secure object creation
#### Singleton
[Singleton](patterns/creational/singleton.py) guarantees that there is only one instance of the class.
#### Factory method
[Factory method](patterns/creational/factory_method.py) defines a common interface for creating objects,
without being tied to specific classes of created objects.
#### Abstract factory
[Abstract factory](patterns/creational/abstract_factory.py) allows you to create families of related objects,
without being tied to specific classes of created objects.
#### Builder
[Builder](patterns/creational/builder.py) allows you to create complex objects step by step, makes it possible
to use the same construction code to obtain different representations of objects.
#### Prototype
[Prototype](patterns/creational/prototype.py) allows you to copy objects without going into the details of their
implementation.
### Structural Design Patterns:
Responsible for building maintainable class hierarchies
### Adapter
[Adapter](patterns/structural/adapter.py) allows objects with incompatible interfaces to work together.
