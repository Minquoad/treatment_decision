""" Author : Guénaël Dequeker
THE FOLLOWING CODE IS FOR READ ONLY"""

import random

from progress_bar import ProgressBar
from treatment import Trial
import playground

# LIST OF EXPERIENCE PARAMETERS

PARALLEL_UNIVERSES_COUNT = 10_000  # the count of universes in the multiverse

# the number a treatment created will be randomize for each universes
# 1 <= MIN_TREATMENTS_COUNT <= MAX_TREATMENTS_COUNT
MIN_TREATMENTS_COUNT = 50
MAX_TREATMENTS_COUNT = 50

# the survival rate of the disease will be randomize in each univers
# 0 <= MIN_DISEASE_SURVIVAL <= MAX_DISEASE_SURVIVAL <= 1
MIN_DISEASE_SURVIVAL = 0.2
MAX_DISEASE_SURVIVAL = 0.3

# the survival rate of the treated patients will be randomize for each treatments
# 0 <= MIN_TREATED_SURVIVAL <= MAX_TREATED_SURVIVAL <= 1
MIN_TREATED_SURVIVAL = 0.3
MAX_TREATED_SURVIVAL = 1.0

# each trial in each univers will be done on a random number of patients
# 2 <= MIN_TRIAL_PATIENT_COUNT <= MAX_TRIAL_PATIENT_COUNT
# MIN_TRIAL_PATIENT_COUNT and MAX_TRIAL_PATIENT_COUNT should be even
MIN_TRIAL_PATIENT_COUNT = 16
MAX_TRIAL_PATIENT_COUNT = 128

# END LIST OF EXPERIENCE PARAMETERS

MIN_GROUP_SIZE = MIN_TRIAL_PATIENT_COUNT // 2
MAX_GROUP_SIZE = MAX_TRIAL_PATIENT_COUNT // 2


def main():
    player_score = compute_player_score()
    player_score = round(100 * player_score, 1)
    print(f"You survived in {player_score} % of the universes")

    god_score = compute_god_score()
    god_score = round(100 * god_score, 1)
    print(f"God score : {god_score} %")


def compute_player_score():
    """ will simulation PARALLEL_UNIVERSES_COUNT universes
    then, will return the overall multiverse survival of the player """

    progress_bar = ProgressBar(label="Computing universes")

    survivals_count = 0
    for i in range(PARALLEL_UNIVERSES_COUNT):
        if simulate_universe():
            survivals_count += 1
        progress_bar.set_progression((i + 1) / PARALLEL_UNIVERSES_COUNT)

    progress_bar.end("\n\n")

    return survivals_count / PARALLEL_UNIVERSES_COUNT


def simulate_universe():
    """ simulates a universe and uses playground.choose_trial to take a decision
    return true in cas of survival in the simulated universe """

    # untreated_survival is the probability to survive if not treated
    # this is an exact law of the universe, the player will not have this information
    untreated_survival = random.uniform(MIN_DISEASE_SURVIVAL, MAX_DISEASE_SURVIVAL)

    trials: list[Trial] = []

    treated_survivals: dict[Trial, float] = {}

    for _ in range(random.randint(MIN_TREATMENTS_COUNT, MAX_TREATMENTS_COUNT)):
        group_size = random.randint(MIN_GROUP_SIZE, MAX_GROUP_SIZE)

        # treated_survival is the probability to survive if treated
        # this is an exact law of the universe, the player will not have this information
        # therefore it is stored in a separate dict and not in the given-to-player Trial object
        treated_survival = random.uniform(MIN_TREATED_SURVIVAL, MAX_TREATED_SURVIVAL)

        trial = Trial(group_size, untreated_survival, treated_survival)

        trials.append(trial)
        treated_survivals[trial] = treated_survival

    chosen_trial = playground.choose_trial(trials)

    if chosen_trial is None:  # None means no treatment
        chosen_survival = untreated_survival
    else:
        chosen_survival = treated_survivals[chosen_trial]

    return random.uniform(0, 1) <= chosen_survival


def compute_god_score():
    """ Does the same thing as the simulate_universes function
    but do not use playground.choose_trial.
    Instead of using trials, it takes a decision according to the real (secret) treatment survival.
    The obtained score is the score you obtain if you know all
    the variables and not only the trials facts """

    survivals_count = 0
    for _ in range(PARALLEL_UNIVERSES_COUNT):
        best_survival = random.uniform(MIN_DISEASE_SURVIVAL, MAX_DISEASE_SURVIVAL)
        for _ in range(random.randint(MIN_TREATMENTS_COUNT, MAX_TREATMENTS_COUNT)):
            treated_survival = random.uniform(MIN_TREATED_SURVIVAL, MAX_TREATED_SURVIVAL)
            if treated_survival > best_survival:
                best_survival = treated_survival
        if random.uniform(0, 1) <= best_survival:
            survivals_count += 1

    return survivals_count / PARALLEL_UNIVERSES_COUNT


if __name__ == "__main__":
    main()
