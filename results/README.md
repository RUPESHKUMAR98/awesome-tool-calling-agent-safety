# Simulation Results

This folder contains the preliminary simulation results and sensitivity analysis comparing three checkpoint policies for chained tool-calling workflows.

## Files

### Original Simulation

- `checkpoint_comparison_v2.csv` — compares success rate, average checks, propagated steps, and recoveries.
- `checkpoint_success_rate.png` — graph comparing simulated success rates.

### Sensitivity Analysis

- sensitivity_analysis_results (1).csv — numerical results for failure probabilities of 0.0, 0.1, 0.2, 0.3, and 0.4 across the three checkpoint policies.
- `sensitivity_analysis.png` — graph showing how simulated success rates change as failure probability increases.

## Methodology

The simulation uses 1,000 trials and 10 workflow steps. It compares no-checkpoint, fixed-checkpoint, and risk-triggered-checkpoint policies.

## Limitations

These results come from a simplified synthetic simulation. Risk flags are generated randomly, and checkpoint recovery follows simplified assumptions. The results should not be interpreted as proof of real-world agent performance.
