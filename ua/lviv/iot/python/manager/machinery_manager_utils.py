import doctest
from ua.lviv.iot.python.models.machinery import Machinery
from ua.lviv.iot.python.models.sort_type import SortType


class MachineryManagerUtils:

    def __init__(self, machinery_list=None):
        if machinery_list is None:
            self.machinery_list = []
        else:
            self.machinery_list = machinery_list

    def __del__(self):
        return

    def sort_by_mileage(self, type_of_sorting: SortType):
        """
        >>> ski_lift_maker_machine = Machinery(2005, 10, 1800, 15000, "eight_x_eight", "gas")
        >>> rider_trace_maker_machine = Machinery(2005, 10, 1800, 18000, "eight_x_eight", "diesel")
        >>> skis_trace_maker_machine =  Machinery(2005, 10, 1800, 20000, "eight_x_eight", "petrol")
        >>> machinery= [ski_lift_maker_machine, rider_trace_maker_machine, skis_trace_maker_machine]
        >>> manager_utils =  MachineryManagerUtils(machinery)
        >>> sorted_machinery_descending = manager_utils.sort_by_mileage(SortType.DESCENDING.value)
        >>> for machinery in sorted_machinery_descending: print(machinery.machiene_mileage)
        20000
        18000
        15000
        >>> sorted_machinery_ascending = manager_utils.sort_by_mileage(SortType.ASCENDING.value)
        >>> for machinery in sorted_machinery_ascending: print(machinery.machiene_mileage)
        15000
        18000
        20000
        """

        machinery = self.machinery_list
        sorted_machinery = sorted(machinery, key=lambda machinery: machinery.machiene_mileage)
        if type_of_sorting == SortType.ASCENDING.value:
            return sorted_machinery
        elif type_of_sorting == SortType.DESCENDING.value:
            return sorted_machinery[::-1]
        else:
            return sorted_machinery




