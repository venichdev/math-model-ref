#!/usr/bin/env python3
"""
Example 3: WLTP Drive Cycle Simulation
======================================

Demonstrates full drive cycle simulation with visualization.
"""

import sys
sys.path.insert(0, '../src')

from ev_calculator import *


def main():
    """Simulate WLTP drive cycle for Tesla Model 3-like vehicle."""

    print("\n" + "="*70)
    print("EXAMPLE 3: WLTP Drive Cycle Simulation")
    print("="*70)

    # Tesla Model 3 Long Range specifications
    vehicle = VehicleParameters(
        mass=1730,
        frontal_area=2.22,
        drag_coefficient=0.23  # Excellent aerodynamics
    )

    battery = BatteryParameters(
        nominal_capacity=75.0,
        usable_capacity=72.0,
        soc_initial=0.95  # Start at 95%
    )

    powertrain = PowertrainParameters(
        motor_power_peak=258.0,  # kW
        motor_efficiency=0.96,
        regen_efficiency=0.75
    )

    aux = AuxiliaryLoads(hvac_power=1.0)

    # Create calculator
    calc = EnergyCalculator(vehicle, powertrain, battery, aux)

    # Generate WLTP cycle (30 minutes)
    print("\nGenerating WLTP Class 3 drive cycle (30 minutes)...")
    time, velocity = DriveCycle.generate_wltp_simplified(1800)

    # Simulate
    print("Simulating energy consumption...")
    results = calc.calculate_energy_consumption(time, velocity, temperature=20)

    # Display results
    print("\n" + "="*70)
    print("WLTP CYCLE RESULTS")
    print("="*70)
    print(f"Distance traveled:     {results['distance_km']:.2f} km")
    print(f"Energy consumed:       {results['E_total_kWh']:.2f} kWh")
    print(f"Consumption rate:      {results['energy_per_km']*100:.2f} kWh/100km")
    print(f"Battery SOC:           95.0% → {results['soc_final']*100:.1f}%")
    print(f"SOC used:              {(0.95 - results['soc_final'])*100:.1f}%")
    print(f"Projected range:       {results['estimated_range_km']:.0f} km")
    print(f"Regen recovered:       {results['E_regen_recovered_kWh']:.2f} kWh")
    print("="*70)

    # Visualize results
    print("\nGenerating visualization...")
    try:
        EVVisualizer.plot_drive_cycle_results(results, save_path='wltp_results.png')
        print("✓ Plot saved to: wltp_results.png")
    except Exception as e:
        print(f"⚠️  Visualization skipped: {e}")

    return results


if __name__ == "__main__":
    results = main()
    print("\n✓ Example completed successfully!\n")
