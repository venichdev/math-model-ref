#!/usr/bin/env python3
"""
Example 2: Temperature Impact on Range
======================================

Demonstrates how temperature affects EV range (winter vs summer).
"""

import sys
sys.path.insert(0, '../src')

from ev_calculator import *
import numpy as np


def main():
    """Analyze temperature impact on EV range."""

    print("\n" + "="*70)
    print("EXAMPLE 2: Temperature Impact on Range")
    print("="*70)

    # Base range from EPA/WLTP rating
    base_range = 400  # km

    # Create calculator
    vehicle = VehicleParameters()
    battery = BatteryParameters()
    powertrain = PowertrainParameters()
    aux = AuxiliaryLoads()
    calc = EnergyCalculator(vehicle, powertrain, battery, aux)

    # Test different temperatures
    temperatures = [-20, -10, 0, 10, 20, 25, 30, 40]

    print(f"\nBase Range: {base_range} km (at optimal conditions)")
    print("\n" + "="*70)
    print(f"{'Temperature':<15} {'Range':<12} {'Loss':<12} {'Factors'}")
    print("-"*70)

    for temp in temperatures:
        result = calc.predict_range_with_adjustments(
            base_range,
            temperature=temp,
            terrain_factor=1.0,
            traffic_factor=1.0
        )

        print(f"{temp:>6}°C        {result['adjusted_range_km']:<12.0f} "
              f"{result['range_loss_percent']:<12.1f} "
              f"(t:{result['f_temp']:.2f} h:{result['f_hvac']:.2f})")

    print("="*70)

    # Highlight winter impact
    winter_result = calc.predict_range_with_adjustments(base_range, temperature=-10)
    print(f"\n⚠️  WINTER IMPACT (-10°C):")
    print(f"   Range loss: {winter_result['range_loss_percent']:.0f}%")
    print(f"   Usable range: {winter_result['adjusted_range_km']:.0f} km")
    print(f"   Lost range: {winter_result['range_loss_km']:.0f} km")

    # Visualize (if matplotlib available)
    try:
        temp_range = np.linspace(-20, 40, 50)
        EVVisualizer.plot_range_comparison(base_range, temp_range)
    except Exception as e:
        print(f"\n⚠️  Visualization skipped: {e}")

    return winter_result


if __name__ == "__main__":
    result = main()
    print("\n✓ Example completed successfully!\n")
