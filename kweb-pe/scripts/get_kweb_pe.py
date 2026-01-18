#!/usr/bin/env python3
"""
KWEB Weighted PE Calculator

Fetches KWEB top 10 holdings, retrieves individual stock PEs, and calculates
the weighted average PE for the entire KWEB ETF.

Usage:
    python3 get_kweb_pe.py

    # Or with custom holdings data:
    from get_kweb_pe import calculate_weighted_pe, parse_weight, parse_pe
"""

import re
import sys
from typing import List, Dict, Optional


def parse_weight(weight_text: str) -> float:
    """Parse weight percentage from text like '10.23%' or just a number."""
    # Try to extract percentage
    match = re.search(r'(\d+\.?\d*)%', weight_text)
    if match:
        return float(match.group(1))
    # Try to extract just a number
    match = re.search(r'(\d+\.?\d*)', weight_text)
    return float(match.group(1)) if match else 0


def parse_pe(pe_text: str) -> Optional[float]:
    """Parse PE ratio from text. Returns None for N/A or invalid values."""
    if not pe_text or pe_text.lower() in ['n/a', '-', 'na', '--']:
        return None
    # Extract the first number found (PE can be negative, e.g., -5.0)
    match = re.search(r'[-+]?\d+\.?\d*', pe_text)
    if match:
        try:
            return float(match.group())
        except ValueError:
            return None
    return None


def calculate_weighted_pe(holdings: List[Dict[str, any]], default_pe: float = 20) -> float:
    """
    Calculate weighted PE for KWEB.

    Args:
        holdings: List of dicts with keys: name, symbol, weight, pe
        default_pe: Default PE for stocks where PE is unavailable or for remaining holdings

    Returns:
        Weighted PE ratio
    """
    separator = "=" * 60
    print("\n" + separator)
    print("KWEB Weighted PE Calculation")
    print(separator)
    print(f"\n{'股票':<15} {'代码':<12} {'PE':<8} {'权重':<8} {'贡献':<10}")
    print("-" * 60)

    total_weight = 0
    weighted_sum = 0

    for i, holding in enumerate(holdings):
        name = holding.get('name', '')[:14]
        symbol = holding.get('symbol', '')
        weight = holding.get('weight', 0)
        pe = holding.get('pe')

        if pe is None:
            pe = default_pe
            print(f"{name:<15} {symbol:<12} {pe:<8.2f}* {weight:<7.2f}% ", end="")
        else:
            print(f"{name:<15} {symbol:<12} {pe:<8.2f}  {weight:<7.2f}% ", end="")

        weighted_contribution = weight * pe
        weighted_sum += weighted_contribution
        total_weight += weight
        print(f"{weighted_contribution:<10.2f}")

    print("-" * 60)
    print(f"{'Top 10 总计:':<28} {' ':<12} {total_weight:<7.2f}% {weighted_sum:<10.2f}")

    # Remaining weight for other holdings (assumed PE = default_pe)
    remaining_weight = 100 - total_weight
    remaining_contribution = remaining_weight * default_pe

    print(f"{'剩余持仓 (默认PE=' + str(default_pe) + ')':<28} {remaining_weight:<7.2f}% {remaining_contribution:<10.2f}")
    print("=" * 60)

    # Weighted PE = total contribution / 100 (since total weight = 100%)
    total_weighted_contribution = weighted_sum + remaining_contribution
    weighted_pe = total_weighted_contribution / 100

    print(f"{'加权 PE 总贡献':<45} {total_weighted_contribution:<10.2f}")
    print(f"{'KWEB 加权 PE':<45} {weighted_pe:<10.2f}")
    print("=" * 60)

    return weighted_pe


def main():
    """
    Main function with sample data for testing.
    In actual use, pass your holdings data directly to calculate_weighted_pe().
    """
    # Sample holdings data (update with current data from Yahoo Finance)
    sample_holdings = [
        {'name': '騰訊控股', 'symbol': '0700.HK', 'weight': 10.23, 'pe': 24.81},
        {'name': '阿里巴巴－Ｗ', 'symbol': '9988.HK', 'weight': 8.77, 'pe': 22.74},
        {'name': 'PDD Holdings Inc.', 'symbol': 'PDD', 'weight': 7.91, 'pe': 10.78},
        {'name': '美團－Ｗ', 'symbol': '3690.HK', 'weight': 7.50, 'pe': 19.08},
        {'name': '網易－Ｓ', 'symbol': '9999.HK', 'weight': 6.09, 'pe': 17.10},
        {'name': '百度集團－ＳＷ', 'symbol': '9888.HK', 'weight': 4.36, 'pe': 13.37},
        {'name': '攜程集團－Ｓ', 'symbol': '9961.HK', 'weight': 4.24, 'pe': 16.10},
        {'name': '京東集團－ＳＷ', 'symbol': '9618.HK', 'weight': 3.97, 'pe': 9.56},
        {'name': '貝殼－Ｗ', 'symbol': '2423.HK', 'weight': 3.89, 'pe': 40.90},
        {'name': '京東健康', 'symbol': '6618.HK', 'weight': 3.87, 'pe': 40.73},
    ]

    separator = "=" * 60
    print("\n" + separator)
    print("KWEB Weighted PE Calculator")
    print(separator)
    print("\nRunning with sample data...")
    print("To use your own data, import the functions:")
    print("  from get_kweb_pe import calculate_weighted_pe")
    print("  weighted_pe = calculate_weighted_pe(your_holdings)")
    print()

    calculate_weighted_pe(sample_holdings)


if __name__ == "__main__":
    main()
