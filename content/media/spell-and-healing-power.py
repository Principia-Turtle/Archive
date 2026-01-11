# @title Spell Power vs Haste (Using User's Base Damage)
import matplotlib.pyplot as plt
import numpy as np

# --- CONFIGURATION ---
# User's specific values
BASE_DMG = 652.5   # Base Average (575 + 730)/2
COEFF = 1.15       # Empowered Fireball (1.0 + 0.15)
HASTE_COST = 15.77 # Rating for 1% Haste

# Calculated Ghost SP
GHOST_SP = BASE_DMG / COEFF

# --- CALCULATION ---
# We simulate gear going from 0 to 2000 Spell Power
sp_range = np.linspace(0, 2000, 100)

# Formula for SP Cost: 0.01 * (GhostSP + CurrentSP)
sp_cost_curve = 0.01 * (GHOST_SP + sp_range)

# --- PLOTTING ---
plt.figure(figsize=(10, 6), dpi=100)

# Plot SP Cost (Blue Line)
plt.plot(sp_range, sp_cost_curve, label='Spell Power Cost (Rising)', color='#1f77b4', linewidth=3)

# Plot Haste Cost (Orange Line)
plt.axhline(y=HASTE_COST, color='#ff7f0e', linestyle='--', linewidth=2, label=f'Haste Cost (Constant {HASTE_COST})')

# Calculate Intersection
# 0.01 * (Ghost + SP) = 15.77
# Ghost + SP = 1577
# SP = 1577 - Ghost
crossover = (HASTE_COST / 0.01) - GHOST_SP

# Annotate Tipping Point
plt.plot(crossover, HASTE_COST, 'ko', zorder=5)
plt.annotate(f'Tipping Point: ~{int(crossover)} SP\n(Switch to Haste)', 
             (crossover, HASTE_COST), xytext=(crossover+150, HASTE_COST-2),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Annotate Ghost SP (Origin)
plt.scatter([0], [sp_cost_curve[0]], color='blue')
plt.annotate(f'Start Cost: {sp_cost_curve[0]:.2f} Rating\n(Due to {int(GHOST_SP)} Ghost SP)',
             (0, sp_cost_curve[0]), xytext=(100, sp_cost_curve[0]+2),
             arrowprops=dict(facecolor='blue', alpha=0.3, shrink=0.05))

plt.title(f'Stat Efficiency (Base Dmg: {BASE_DMG})', fontsize=14, fontweight='bold')
plt.xlabel('Current Spell Power', fontsize=12)
plt.ylabel('Rating Needed for 1% Gain (Lower is Better)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
