""" Author : Guénaël Dequeker
THE FOLLOWING CODE IS FOR READ ONLY"""

import random

class Trial:
    """ This class simulate a trial result based on 
    """
    def __init__(self, group_size, untreated_survival, treated_survival):
        self._control_group_survivors = 0
        self._control_group_deaths = 0
        self._experimental_group_survivors = 0
        self._experimental_group_deaths = 0

        for _ in range(group_size):# result for the control group (treated with placebo)
            if random.uniform(0, 1) <= untreated_survival:
                self._control_group_survivors += 1
            else:
                self._control_group_deaths += 1

        for _ in range(group_size):# result for the experimental group (treated)
            if random.uniform(0, 1) <= treated_survival:
                self._experimental_group_survivors += 1
            else:
                self._experimental_group_deaths += 1

    @property
    def control_group_survivors(self):
        """ the number of patients who survived in the untreated group """
        return self._control_group_survivors

    @property
    def control_group_deaths(self):
        """ the number of patients who died in the untreated group """
        return self._control_group_deaths

    @property
    def experimental_group_survivors(self):
        """ the number of patients who died in the untreated group """
        return self._experimental_group_survivors

    @property
    def experimental_group_deaths(self):
        """ the number of patients who died in the untreated group """
        return self._experimental_group_deaths

    @property
    def group_size(self):
        """ using the experimental group would also have done the job """
        return self._control_group_survivors + self._control_group_deaths
