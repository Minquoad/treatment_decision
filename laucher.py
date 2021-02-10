""" Author : Guénaël Dequeker
THE FOLLOWING CODE IS FOR READ ONLY"""

import random

from trial import Trial
import playground

# LIST OF EXPERIENCE PARAMATERS

PARALLEL_UNIVERSES_COUNT = 10_000 # the count of universes in the multiver
TREATMENTS_COUNT = 50 # number of treatment each univers will develop

# the survival rate of the disease will be randominze in each univers
# 0 <= MIN_DISEASE_SURVIVAL <= MAX_DISEASE_SURVIVAL <= 1
MIN_DISEASE_SURVIVAL = 0.2
MAX_DISEASE_SURVIVAL = 0.3

# the survival rate of the treated patients will be randominze for each treatments
# 0 <= MIN_TREATED_SURVIVAL <= MAX_TREATED_SURVIVAL <= 1
MIN_TREATED_SURVIVAL = 0.3
MAX_TREATED_SURVIVAL = 1.0

# each trial in each univers will be done on a random number of patients
# 2 <= MIN_TRIAL_PATIENT_COUNT <= MAX_TRIAL_PATIENT_COUNT
# MIN_TRIAL_PATIENT_COUNT and MAX_TRIAL_PATIENT_COUNT should be even
MIN_TRIAL_PATIENT_COUNT = 16
MAX_TRIAL_PATIENT_COUNT = 128 

# END LIST OF EXPERIENCE PARAMATERS

MIN_GROUP_SIZE = int(MIN_TRIAL_PATIENT_COUNT / 2)
MAX_GROUP_SIZE = int(MAX_TRIAL_PATIENT_COUNT / 2)


def main():
    """ This comment is useless """
    simulate_universes()
    simulate_omniscient_universes()


def simulate_universes():
    """ will simulation PARALLEL_UNIVERSES_COUNT universes.
    Then, will print the performace of the playground.choose_trial function """

    survivals_count = 0
    for _ in range(PARALLEL_UNIVERSES_COUNT):
        if simulate_universe():
            survivals_count += 1

    print("You survived in {} % of the universes"
        .format(round(100 * survivals_count / PARALLEL_UNIVERSES_COUNT, 1)))


def simulate_universe():
    """ Uses playground.choose_trial to take a decision
    return true in cas of survival in the simulated universe
    """

    # untreated_survival is the probability to survive if not treated
    # this is an exact law of the universe, the player will not have this information
    untreated_survival = random.uniform(MIN_DISEASE_SURVIVAL, MAX_DISEASE_SURVIVAL)

    trials = []
    treated_survivals = []

    for _ in range(TREATMENTS_COUNT):
        # treated_survival is the probability to survive if treated
        # this is an exact law of the universe, the player will not have this information
        # therefore it is stored in a separate list and not in the given-to-player Trial object
        treated_survival = random.uniform(MIN_TREATED_SURVIVAL, MAX_TREATED_SURVIVAL)
        treated_survivals.append(treated_survival)

        group_size = random.randint(MIN_GROUP_SIZE, MAX_GROUP_SIZE)

        trials.append(Trial(group_size, untreated_survival, treated_survival))

    choosen_trial_index = playground.choose_trial(tuple(trials))
    if choosen_trial_index is None:# None means no treatment
        choosen_treatment_survival = untreated_survival
    else:
        choosen_treatment_survival = treated_survivals[choosen_trial_index]

    return random.uniform(0, 1) <= choosen_treatment_survival

def simulate_omniscient_universes():
    """ Does the same thing as the simulate_universes function
    but do not use playground.choose_trial.
    Intead, it takes a decision according to the real (secret) treatment survival.
    The obtained score is the score you obtain if you know all
    the variables and not only the trials facts.
    Then, will print the performace.
    """

    survivals_count = 0
    for _ in range(PARALLEL_UNIVERSES_COUNT):
        best_survival = random.uniform(MIN_DISEASE_SURVIVAL, MAX_DISEASE_SURVIVAL)
        for _ in range(TREATMENTS_COUNT):
            treated_survival = random.uniform(MIN_TREATED_SURVIVAL, MAX_TREATED_SURVIVAL)
            if treated_survival > best_survival:
                best_survival = treated_survival
        if random.uniform(0, 1) <= best_survival:
            survivals_count += 1

    print("God score : {} %"
        .format(round(100 * survivals_count / PARALLEL_UNIVERSES_COUNT, 1)))


if __name__ == "__main__":
    main()
