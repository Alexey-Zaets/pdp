# personal development plan

## Algorithms

### Sorting algorithms
[Bubble sort](algorithms/sorting/bubble_sort.py)  **best case 0(n), average and worst case O(n^2)**

[Insertion sort](algorithms/sorting/insertion_sort.py)  **best case 0(n), average and worst case O(n^2)**

[Merge sort](algorithms/sorting/merge_sort.py)  **best, average and worst case O(n * log2 n)**

[Selection sort](algorithms/sorting/selection_sort.py) **worst case, average case, best case O(n^2)**

[Quick sort](algorithms/sorting/quick_sort.py)  **best case O(n * log2 n), worst case O(n^2)**

**Sorting algorithm selection criteria**

| Criteria                                    | Sorting algorithm                                      |
|:------------------------------------------- |:-------------------------------------------------------|
| Only a few items                            | [Insertion sort](algorithms/sorting/insertion_sort.py) |
| The elements are almost sorted already      | [Insertion sort](algorithms/sorting/insertion_sort.py) |
| Worst case performance matters              | Heapsort                                               |
| Performance is important in the middle case | [Quick sort](algorithms/sorting/quick_sort.py)         |
| Evenly distributed elements                 | Block sort                                             |
| As little code as possible                  | [Insertion sort](algorithms/sorting/insertion_sort.py) |
| Sort stability required                     | [Merge sort](algorithms/sorting/merge_sort.py)         |

## Design patterns

### Creational Design Patterns:
> Responsible for convenient and secure object creation

[Singleton](patterns/creational/singleton.py) guarantees that there is only one instance of the class.

[Factory method](patterns/creational/factory_method.py) defines a common interface for creating objects,
without being tied to specific classes of created objects.

[Abstract factory](patterns/creational/abstract_factory.py) allows you to create families of related objects,
without being tied to specific classes of created objects.

[Builder](patterns/creational/builder.py) allows you to create complex objects step by step, makes it possible
to use the same construction code to obtain different representations of objects.

[Prototype](patterns/creational/prototype.py) allows you to copy objects without going into the details of their
implementation.

### Structural Design Patterns:
> Responsible for building maintainable class hierarchies

[Adapter](patterns/structural/adapter.py) allows objects with incompatible interfaces to work together.
