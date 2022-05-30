import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.optimize import curve_fit

class omc:
    """
    =====================================================================================================
    Routines for carrying out various processes of O-C studies
    =====================================================================================================
    """
    def __init__(self):
        self.get_o_values = self.get_o_values()
        self.clock = self.clock(P, T0)

    def get_c_value(T0, P, E):
        """
        -----------------------------------------------------------------------------------------------------
        Uses a given start time and period to return the time value at a specified epoch number. This assumes
        that T0 and P are entered in the same units, but those units can be whatever the user desires.
        -----------------------------------------------------------------------------------------------------
            Takes in:
                ▢ T0: float64
                    start time in whatever units are desired (should at least be same unit as P)
                ▢ P: float64
                    period of system in whatever units are desired (should at least be same unit as T0)
                ▢ E: int or array_like
                    epoch number to get time value at
        -----------------------------------------------------------------------------------------------------
            Outputs: float or array_like
                ▢ epoch value at specified epoch number in units used for T0 and P
        -----------------------------------------------------------------------------------------------------
        """
        return T0 + P*E

    def generate_c_values(T0, P, E_final):
        """
        -----------------------------------------------------------------------------------------------------
        Uses a given start time, period, and desired ending epoch number to return the calculated values
        between the start time and end epoch. This assumes that T0 and P are entered in the same units, but
        those units can be whatever the user desires.
        -----------------------------------------------------------------------------------------------------
            Takes in:
                ▢ T0: float64
                    start time in whatever units are desired (should at least be same unit as P)
                ▢ P: float64
                    period of system in whatever units are desired (should at least be same unit as T0)
                ▢ E_final: int
                    final epoch number to get time value at
        -----------------------------------------------------------------------------------------------------
            Outputs: array_like
                ▢ epoch values between T0 and the last epoch specified by E_final
        -----------------------------------------------------------------------------------------------------
        """
        return get_c_value(T0, P, np.arange(T0, E_final+1, 1))

    class get_o_values:
        """
        =====================================================================================================
        Subclass with specific routines for deriving observed values using various functional forms that can
        be tailored to an individual system.
        =====================================================================================================
        """
        def __init__(self):

        def via_window():

        def via_appending():

    class clock:
        """
        =====================================================================================================
        Subclass to store information about your variable source
        =====================================================================================================
            Takes in:
                ▢ T0: float64
                    start time in whatever units are desired (should at least be same unit as P)
                ▢ P: float64
                    period of system in whatever units are desired (should at least be same unit as T0)
        -----------------------------------------------------------------------------------------------------

        """
        def __init__(self, P, T0):
            self.P = np.float64(P)
            self.T0 = np.float64(T0)
