# Author : Guénaël Dequeker
""" PLAYGROUND IS HERE !!! survive as much as you can """

from typing import Optional

from treatment import Trial


def choose_trial(trials: list[Trial]) -> Optional[Trial]:
    """ Each trial tests a different treatment with a different number of patients
    return one of the trials : its corresponding treatment will be your treatment
    return None for no treatment """

    best_trial = None
    best_treatment_survival = -1

    for trial in trials:
        treatment_survival = trial.treatment_survival
        if treatment_survival > best_treatment_survival:
            best_trial = trial
            best_treatment_survival = treatment_survival

    return best_trial
