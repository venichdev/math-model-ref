#!/usr/bin/env python3
"""
Example 4: Model Validation
===========================

Demonstrates validation against real vehicle data (Nissan Leaf 2018).
"""

import sys
sys.path.insert(0, '../src')

from ev_calculator import *


def main():
    """Validate model against Nissan Leaf 2018 EPA data."""

    print("\n" + "="*70)
    print("EXAMPLE 4: Model Validation (Nissan Leaf 2018)")
    print("="*70)

    # Run validation
    print("\nValidating against EPA test data...")
    validator = ModelValidator()
    results = validator.validate_nissan_leaf_2018()

    # Display results
    print("\n" + "="*70)
    print(f"Vehicle: {results['vehicle']}")
    print("="*70)
    print(f"\n{'Metric':<25} {'EPA Data':<15} {'Model':<15} {'Error'}")
    print("-"*70)

    print(f"{'City Energy':<25} {results['city']['epa']:<15.1f} "
          f"{results['city']['model']:<15.1f} {results['city']['error_percent']:>+7.2f}%")

    print(f"{'  [kWh/100km]':<25}")

    print(f"\n{'Highway Energy':<25} {results['highway']['epa']:<15.1f} "
          f"{results['highway']['model']:<15.1f} {results['highway']['error_percent']:>+7.2f}%")

    print(f"{'  [kWh/100km]':<25}")

    print(f"\n{'Combined Energy':<25} {results['combined']['epa']:<15.1f} "
          f"{results['combined']['model']:<15.1f} {results['combined']['error_percent']:>+7.2f}%")

    print(f"{'  [kWh/100km]':<25}")

    print(f"\n{'Range':<25} {results['range']['epa']:<15.0f} "
          f"{results['range']['model']:<15.0f} {results['range']['error_percent']:>+7.2f}%")

    print(f"{'  [km]':<25}")

    print("\n" + "="*70)

    # Assessment
    max_error = max(
        abs(results['city']['error_percent']),
        abs(results['highway']['error_percent']),
        abs(results['combined']['error_percent']),
        abs(results['range']['error_percent'])
    )

    if max_error < 5:
        assessment = "✓ EXCELLENT - Within ±5% (thesis acceptable)"
    elif max_error < 10:
        assessment = "✓ GOOD - Within ±10% (acceptable for early design)"
    else:
        assessment = "⚠ FAIR - Model needs calibration"

    print(f"\nVALIDATION RESULT: {assessment}")
    print(f"Maximum error: {max_error:.2f}%")
    print("="*70)

    print("\nNote: Simplified drive cycles used. For certification,")
    print("      use official WLTP/EPA test data files.")

    return results


if __name__ == "__main__":
    results = main()
    print("\n✓ Example completed successfully!\n")
