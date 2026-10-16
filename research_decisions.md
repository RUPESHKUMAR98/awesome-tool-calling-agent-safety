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
