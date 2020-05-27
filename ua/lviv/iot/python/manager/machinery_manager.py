import doctest
from ua.lviv.iot.python.models.machinery import Machinery


class MachineryManager:

    def __init__(self, machineries_list=None):
        if machineries_list is None:
            self.machineries_list = []
        else:
            self.machineries_list = machineries_list

    def __del__(self):
        return

    def search_by_machineries_fuel_type(self, fuel_type):
        """
        >>> ski_lift_maker_machine = Machinery(2005, 10, 1800, 15000, 'eight_x_eight', 'gas')
        >>> rider_trace_maker_machine = Machinery(2002, 10, 1700, 13700, 'six_x_six', 'gas')
        >>> skis_trace_maker_machine = Machinery(1998, 9, 1430, 12700, 'four_x_four', 'gas')
        >>> some_machinery = Machinery(1994, 8, 1384, 1205, 'four_x_two', 'gas')
        >>> machineries = [ski_lift_maker_machine, rider_trace_maker_machine, skis_trace_maker_machine, some_machinery]
        >>> manager = MachineryManager(machineries)
        >>> found_machineries = manager.search_by_machineries_fuel_type('gas')
        >>> print(len(found_machineries))
        4
        """

        result_machineries = []
        machineries = self.machineries_list
        for machinery in machineries:
            if machinery.fuel_type == fuel_type:
                result_machineries.append(machinery)
        sorted_result_machineries = sorted(result_machineries, key=lambda attract: attract.machiene_mileage)
        return sorted_result_machineries


if __name__ == "main":
    doctest.testmod(verbose=True)