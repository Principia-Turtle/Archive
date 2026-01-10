# @title Spell Power vs Haste: The Tipping Point
import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURATION ---
BASE_DMG = 760   # Average Base Damage (e.g., Rank 13 Fireball)
COEFF = 1.15     # Spell Coefficient (1.0 + 0.15 Emp. Fireball)
HASTE_COST = 15.77 # Rating for 1% Haste

# --- CALCULATION ---
# We simulate gear going from 0 to 2000 Spell Power
sp_range = np.linspace(0, 2000, 100)

# Formula for SP Cost: 0.01 * (Base/Coeff + CurrentSP)
# This calculates how much SP rating is needed to add 1% to your total output
sp_cost_curve = 0.01 * ((BASE_DMG / COEFF) + sp_range)

# --- PLOTTING ---
plt.figure(figsize=(10, 6), dpi=100)

# Plot SP Cost (Blue Line)
plt.plot(sp_range, sp_cost_curve, label='Spell Power Cost (Rising)', color='#1f77b4', linewidth=3)

# Plot Haste Cost (Orange Line)
plt.axhline(y=HASTE_COST, color='#ff7f0e', linestyle='--', linewidth=2, label=f'Haste Cost (Constant {HASTE_COST})')

# Calculate Intersection
crossover = (HASTE_COST / 0.01) - (BASE_DMG / COEFF)

# Annotate Tipping Point
plt.plot(crossover, HASTE_COST, 'ko', zorder=5)
plt.annotate(f'Tipping Point: ~{int(crossover)} SP\n(Switch to Haste)', 
             (crossover, HASTE_COST), xytext=(crossover+150, HASTE_COST-2),
             arrowprops=dict(facecolor='black', shrink=0.05))

plt.title('Stat Efficiency: When to Stop Stacking SP', fontsize=14, fontweight='bold')
plt.xlabel('Current Spell Power', fontsize=12)
plt.ylabel('Rating Needed for 1% Gain (Lower is Better)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
