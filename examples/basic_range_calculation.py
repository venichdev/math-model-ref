#!/usr/bin/env python3
"""
Example 1: Basic Range Calculation
===================================

Demonstrates the simplest use case: calculating highway range for a typical EV.
"""

import sys
sys.path.insert(0, '../src')

from ev_calculator import *


def main():
    """Calculate basic highway range for a typical EV."""

    print("\n" + "="*70)
    print("EXAMPLE 1: Basic Highway Range Calculation")
    print("="*70)

    # Define vehicle parameters
    vehicle = VehicleParameters(
        mass=1800,              # kg
        frontal_area=2.3,       # m²
        drag_coefficient=0.28,  # typical modern EV
        rolling_coeff=0.010
    )

    # Battery specifications
    battery = BatteryParameters(
        nominal_capacity=75.0,  # kWh
        usable_capacity=70.0,   # kWh (with buffer)
        soc_initial=1.0         # Start at 100%
    )

    # Powertrain
    powertrain = PowertrainParameters()

    # Auxiliary loads
    aux = AuxiliaryLoads(
        hvac_power=2.0,  # kW (AC running)
        electronics=0.3,
        lighting=0.1
    )

    # Create calculator
    calc = EnergyCalculator(vehicle, powertrain, battery, aux)

    # Highway driving: 120 km/h for 1 hour
    print("\nSimulating highway driving at 120 km/h for 1 hour...")
    time, velocity = DriveCycle.generate_constant_speed(120, duration=3600)

    # Calculate energy consumption
    results = calc.calculate_energy_consumption(time, velocity)

    # Display results
    print("\n" + "="*70)
    print("RESULTS")
    print("="*70)
    print(f"Distance traveled:     {results['distance_km']:.1f} km")
    print(f"Energy consumed:       {results['E_total_kWh']:.2f} kWh")
    print(f"Consumption rate:      {results['energy_per_km']*100:.2f} kWh/100km")
    print(f"Battery SOC:           {battery.soc_initial*100:.0f}% → {results['soc_final']*100:.1f}%")
    print(f"Estimated total range: {results['estimated_range_km']:.0f} km")
    print(f"Regen energy:          {results['E_regen_recovered_kWh']:.2f} kWh")
    print("="*70)

    # Energy breakdown
    print("\nEnergy Breakdown:")
    print(f"  Traction:            {results['E_traction_kWh']:.2f} kWh")
    print(f"  Motor losses:        {results['E_motor_kWh'] - results['E_traction_kWh']:.2f} kWh")
    print(f"  Auxiliary (HVAC):    {results['E_aux_kWh']:.2f} kWh")
    print(f"  Total:               {results['E_total_kWh']:.2f} kWh")

    return results


if __name__ == "__main__":
    results = main()
    print("\n✓ Example completed successfully!\n")
