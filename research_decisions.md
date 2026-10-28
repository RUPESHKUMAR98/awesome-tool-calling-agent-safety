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

The research brief and experimental decisions have been documented. A preliminary Python simulation has been implemented to compare no-checkpoint, fixed-checkpoint, and risk-triggered-checkpoint policies. The simulation records success rate, average checks, propagated steps, and recoveries. Baseline validation tests for the random failure generator have been documented as passed. Preliminary comparison results and sensitivity-analysis results have also been generated.

Further validation of checkpoint detection, failure propagation, recovery behavior, and the full comparison model remains necessary. The simulation uses synthetic failures and simplified recovery assumptions.

## 8. Next Action

Complete the remaining validation of the checkpoint policies, verify that the recorded results match the simulation code, review the sensitivity-analysis results, and document the experimental findings, reproducibility steps, and limitations. Ensure that all required code, result files, graphs, and documentation are available in the GitHub repository.

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
## Sensitivity Analysis

### Experimental Setup
A sensitivity analysis was conducted using five failure-probability settings: 0.0, 0.1, 0.2, 0.3, and 0.4. The simulation used 1,000 trials and 10 steps per workflow. The three checkpoint policies evaluated were no checkpoint, fixed checkpoint, and risk-triggered checkpoint.

### Observed Results
The simulation results show that the no-checkpoint policy becomes less successful as the failure probability increases. The fixed-checkpoint policy maintains a 100% success rate under the current deterministic recovery assumptions. The risk-triggered policy also shows declining success rates as failure probability increases.

### Interpretation and Limitations
These results illustrate how checkpoint policies behave under the selected synthetic simulation settings. They should not be interpreted as proof of performance in real-world tool-calling agents. Risk flags are generated synthetically rather than from a validated error detector, and checkpoint recovery is simplified. Further experiments should test different checkpoint intervals, recovery assumptions, and risk-flag quality.
