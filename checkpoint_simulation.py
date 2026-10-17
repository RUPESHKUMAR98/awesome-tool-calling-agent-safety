
import random
import pandas as pd

# Generate the same scenarios for all policies
random.seed(42)

N = 1000
STEPS = 10
FAILURE_PROBABILITY = 0.2
RISK_PROBABILITY = 0.3
CHECKPOINT_INTERVAL = 2

scenarios = []

for run in range(N):
    failures = [
        random.random() < FAILURE_PROBABILITY
        for _ in range(STEPS)
    ]
    risk_flags = [
        random.random() < RISK_PROBABILITY
        for _ in range(STEPS)
    ]
    scenarios.append((failures, risk_flags))


def simulate(policy, scenarios):
    successful_runs = 0
    total_checks = 0
    total_propagated_steps = 0
    total_recoveries = 0

    for failures, risk_flags in scenarios:
        corrupted = False
        propagated_steps = 0
        checks = 0
        recoveries = 0

        for i in range(STEPS):
            # A new failure corrupts the workflow state
            if failures[i]:
                corrupted = True

            if corrupted:
                propagated_steps += 1

            step = i + 1

            if policy == "Fixed checkpoint":
                should_check = (
                    step % CHECKPOINT_INTERVAL == 0
                    or step == STEPS
                )
            elif policy == "Risk-triggered checkpoint":
                should_check = risk_flags[i]
            else:
                should_check = False

            if should_check:
                checks += 1

                # A check detects and repairs a corrupted state
                if corrupted:
                    corrupted = False
                    recoveries += 1

        if not corrupted:
            successful_runs += 1

        total_checks += checks
        total_propagated_steps += propagated_steps
        total_recoveries += recoveries

    return {
        "Policy": policy,
        "Success rate (%)": 100 * successful_runs / N,
        "Average checks": total_checks / N,
        "Propagated steps": total_propagated_steps / N,
        "Recoveries": total_recoveries / N
    }


results_v2 = [
    simulate("No checkpoint", scenarios),
    simulate("Fixed checkpoint", scenarios),
    simulate("Risk-triggered checkpoint", scenarios)
]

comparison_v2 = pd.DataFrame(results_v2)
display(comparison_v2)
comparison_v2.to_csv(
    "checkpoint_comparison_v2.csv",
    index=False
)

print("Simulation results saved successfully.")
