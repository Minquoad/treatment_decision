# Author : Guénaël Dequeker
""" PLAYGROUNG IS HERE !!! survive as much as you can """

def choose_trial(trials):
    """ "trials" is a tuple of Trial objects (see class desciption in trial.py)
    each trial tests a different treatment with a different number of patients
    return the index of a trial : its corresponding treatment will be your treatment
    return None for no treatment
    """

    best_trial_index = None
    best_treatment_survival = -1

    for i, trial in enumerate(trials):
        treatment_survival = trial.experimental_group_survivors / trial.group_size
        if treatment_survival > best_treatment_survival:
            best_trial_index = i
            best_treatment_survival = treatment_survival

    return best_trial_index

