<<<<<<< HEAD
﻿from DataStructs.List import arlt
from DataStructs.List import sllt
from typing import Callable


def selection_sort(lt: any, sort_crit:Callable):
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "LINKEDLIST":
        lst = sllt
        
    _size = lst.size(lt)
    pos1 = 0
    while pos1 < _size:
        minimum = pos1
        pos2 = pos1 + 1
        while (pos2 < _size):
            if(sort_crit(lst.get_element(lt, pos2), (lst.get_element(lt, minimum)))):
                minimum = pos2
            pos2 += 1    
        lst.exchange(lt, pos1, minimum)
        pos1 += 1
    return lt   
=======
﻿from Src.Func.DataStructs.List import arlt
from Src.Func.DataStructs.List import sllt
from typing import Callable


def sort(lt: dict, sort_crit: Callable) -> dict:
    if lt["type"] == "ARRAYLIST":
        lst = arlt
    elif lt["type"] == "SINGLELINKED":
        lst = sllt

    size = lst.size(lt)
    i = 0
    while i < size:
        _min = i
        j = i + 1
        while j < size:
            if sort_crit(lst.get_element(lt, j),
                         lst.get_element(lt, _min)):
                _min = j
            j += 1
        lst.exchange(lt, i, _min)
        i += 1
    return lt
>>>>>>> 49de53edb74c4580677f66e5abb67f667f5c851f
