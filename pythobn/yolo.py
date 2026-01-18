from typing import Callable, List, Dict, Any


def positive(x):
    return x > 0


def square(x):
    return x*x


def summation(lst):
    return sum(lst)


def make_pipeline(filter_func: Callable[[float], bool], transform_func: Callable[[float], float], aggregate_func: Callable[[list], float]) -> Callable[[list], float]:

    def process(datasets):
        output = []
        for i in datasets:
            if len(i) == 0:
                output.append([])
            else:
                try:
                    filtered_dataset = list(
                        filter(lambda item: filter_func(item), i))
                    squared_dataset = list(
                        map(transform_func, filtered_dataset))
                    output.append(aggregate_func(squared_dataset))
                except TypeError:
                    output.append([])
                except ZeroDivisionError:
                    output.append([])
        return output
    return process


datasets = [
    [1, 2, 3, -1, 5],
    [10, 0, 5, 7],
    [8, 9, 'a', 4]
]
pipeline = make_pipeline(positive, square, summation)
results = pipeline(datasets)
print(results)
