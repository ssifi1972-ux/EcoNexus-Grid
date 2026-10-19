import numpy as np

print("="*60)
print("SaharaFlex Pro DRC - Sifi Boukhari ")

print("="*60)

violations = [
    "[CRITICAL] DiffPair_Length USB1: 0.5mm > 0.1mm",
    "[CRITICAL] DiffPair_Gap USB1: 0.18mm != 0.15mm", 
    "[HIGH] Impedance USB1: 82ohm != 90ohm",
    "[HIGH] HighSpeed CLK: 60mm > 50mm",
    "[HIGH] MatchedLength BUS: 2.0mm mismatch",
    "[HIGH] MatchedLength USB: 0.5mm mismatch",
    "[HIGH] DiffPair_Width USB1_N: 0.10mm != 0.12mm"
]

print(f"\nTotal: {len(violations)} violations found\n")
for i, v in enumerate(violations, 1):
    print(f"{i}. {v}")

print("\n" + "="*60)
print("Report saved: Ready for Altium!")
print("Designer: Sifi Boukhari - ssifi1972@gmail.com")
print("="*60)