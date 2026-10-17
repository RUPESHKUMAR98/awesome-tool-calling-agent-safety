# Research Decisions

## 1. Research Question
How do different checkpoint policies affect the reliability and execution overhead of simulated tool-calling workflows?

## 2. Policies to Compare
- **No checkpoint:** The workflow runs without intermediate checks.
- **Fixed checkpoint:** The workflow is checked at predefined intervals.
- **Risk-triggered checkpoint:** The workflow is checked when a predefined risk rule is activated.

## 3. Experimental Environment
Python will be used to simulate multi-step workflows with configurable failure probabilities.

## 4. Evaluation Metrics
- End-to-end success rate
- Failure propagation
- Number of checks or interventions
- Execution overhead

## 5. Fair Comparison
All policies will be tested using comparable workflow scenarios and documented experimental settings. The checkpoint rules and failure-handling procedures will be defined before the main experiments.

## 6. Reproducibility
The project will record configuration settings, random seeds, code, and experimental results so that runs can be repeated.

## 7. Current Status
The research brief has been saved. The simulation has not yet been implemented or validated.

## 8. Next Action
Create a small Python simulation and verify that it behaves correctly under controlled success and failure cases.
## Simulation Methodology and Limitations

### Simulation Setup

The preliminary experiment compares three checkpoint policies in a simulated chained tool-calling workflow:

1. **No checkpoint:** No checkpoint-based recovery is performed.
2. **Fixed checkpoint:** Checkpoints occur at predefined intervals.
3. **Risk-triggered checkpoint:** Checkpoints are triggered by simulated risk flags.

The simulation uses 1,000 trials, 10 workflow steps per trial, a configured failure probability of 0.2, a configured risk-flag probability of 0.3, and a fixed checkpoint interval of 2 steps.

### Metrics

The simulation records:

- Successful workflow rate
- Average number of checks
- Average number of propagated steps
- Average number of recoveries

### Preliminary Results

In the current simulation run, the observed success rates were:

| Policy | Success rate |
|---|---:|
| No checkpoint | 10.4% |
| Fixed checkpoint | 100.0% |
| Risk-triggered checkpoint | 65.3% |

### Limitations

These results depend on the simulation's assumptions and implementation. In particular, checkpoint recovery is simplified, and risk-triggered checks depend on simulated risk flags rather than a real error detector. The results therefore should not be generalized to real-world AI agents.

Future work should test alternative parameter settings, validate the recovery assumptions, and examine how checkpoint policies affect execution overhead and failure propagation.
