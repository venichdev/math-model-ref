# Examples

This directory contains working examples demonstrating how to use the EV Calculator.

## Available Examples

### 1. Basic Range Calculation
**File:** `basic_range_calculation.py`

Simple highway range calculation for a typical EV.

```bash
python basic_range_calculation.py
```

**What it demonstrates:**
- Creating vehicle, battery, and powertrain parameters
- Generating a constant-speed drive cycle
- Calculating energy consumption
- Estimating range

### 2. Temperature Impact
**File:** `temperature_impact.py`

Analyzes how temperature affects EV range (winter vs summer).

```bash
python temperature_impact.py
```

**What it demonstrates:**
- Temperature-based range adjustment
- HVAC impact modeling
- Range loss calculation
- Visualization of range vs temperature

### 3. WLTP Cycle Simulation
**File:** `wltp_cycle.py`

Full WLTP drive cycle simulation with visualization.

```bash
python wltp_cycle.py
```

**What it demonstrates:**
- WLTP drive cycle generation
- Complete energy consumption analysis
- SOC tracking over time
- Publication-quality visualization
- Regenerative braking energy recovery

### 4. Model Validation
**File:** `validation_demo.py`

Validates model against real vehicle data (Nissan Leaf 2018).

```bash
python validation_demo.py
```

**What it demonstrates:**
- Model validation methodology
- Comparison with EPA test data
- Error calculation
- Assessment criteria for thesis use

## Running Examples

### Prerequisites

```bash
pip install numpy matplotlib scipy
```

### Run All Examples

```bash
# From the examples directory
python basic_range_calculation.py
python temperature_impact.py
python wltp_cycle.py
python validation_demo.py
```

### Expected Output

Each example will:
1. Print results to console
2. Generate plots (if matplotlib available)
3. Save visualizations to PNG files

## Output Files

Examples may create:
- `wltp_results.png` - WLTP cycle visualization
- Other visualization files as specified

## Customization

Feel free to modify the examples:
- Change vehicle parameters
- Adjust battery capacity
- Try different drive cycles
- Experiment with temperatures

## For Your Thesis

These examples can serve as:
- Starting point for your own simulations
- Template for thesis code
- Validation methodology reference
- Figure generation for publications

## Need Help?

- Read `../docs/QUICK_START.md` for detailed tutorial
- Check `../docs/IMPLEMENTATION_README.md` for API reference
- See `../src/ev_calculator.py` for inline documentation
