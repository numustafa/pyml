from typing import Callable, List, Union

import numpy as np

# This is a type alias. We use it so that
# we don't have to type the type out every time
# In this instance we define that a Vector is
# either a list of floats or a numpy array.
Vector = Union[List[float], np.ndarray]


Dataset = Union[List[Vector], np.ndarray]
Label = int
LabelList = Union[List[Label], np.ndarray]
DistanceCallable = Callable[[Vector, Vector], Label]
NearestCallable = Callable[[Vector, Dataset, LabelList, DistanceCallable], Label]
