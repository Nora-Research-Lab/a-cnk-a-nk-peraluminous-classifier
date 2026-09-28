import math
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# Molecular weights
MW_AL2O3 = 101.96
MW_CAO = 56.08
MW_NA2O = 61.98
MW_K2O = 94.20

def classify(al2o3_wt, cao_wt, na2o_wt, k2o_wt):
    """
    Compute A/CNK, A/NK and classification label from oxide weight percents.
    Returns (a_cnk, a_nk, label).
    """
    # Convert wt% to moles
    mol_Al2O3 = al2o3_wt / MW_AL2O3
    mol_CaO = cao_wt / MW_CAO
    mol_Na2O = na2o_wt / MW_NA2O
    mol_K2O = k2o_wt / MW_K2O

    a_cnk = mol_Al2O3 / (mol_CaO + mol_Na2O + mol_K2O)
    a_nk = mol_Al2O3 / (mol_Na2O + mol_K2O)

    # Classification
    if a_cnk > 1.1:
        label = "Strongly peraluminous"
    elif a_cnk > 1.0:
        label = "Weakly peraluminous"
    elif a_nk > 1.0:
        label = "Metaluminous"
    else:
        label = "Peralkaline"

    return round(a_cnk, 2), round(a_nk, 2), label

def plot_diagram(a_cnk, a_nk):
    """Create A/CNK vs A/NK diagram with shaded fields and plotted point."""
    fig, ax = plt.subplots(figsize=(4, 4), dpi=100)

    # Shaded fields
    # Peralkaline: A/NK < 1 (left-lower)
    # Metaluminous: A/CNK < 1 and A/NK > 1 (right-lower)
    # Weakly peraluminous: 1 < A/CNK < 1.1 (rectangular band)
    # Strongly peraluminous: A/CNK > 1.1 (right-upper)

    x = np.linspace(0, 2, 400)
    # Peralkaline region: A/NK < 1 (entire left of A/NK=1)
    ax.fill_betweenx([0, 1], 0, 2, color='lightcoral', alpha=0.3, label='Peralkaline')
    # Metaluminous: A/CNK < 1, A/NK > 1
    ax.fill_betweenx([1, 2], 0, 1, color='lightblue', alpha=0.3, label='Metaluminous')
    # Weakly peraluminous: A/CNK between 1 and 1.1, any A/NK (but limited axes to 0-2)
    ax.axvspan(1, 1.1, ymin=0, ymax=1, color='lightyellow', alpha=0.5, label='Weakly peraluminous')
    # Strongly peraluminous: A/CNK > 1.1
    ax.fill_betweenx([0, 2], 1.1, 2, color='lightgreen', alpha=0.3, label='Strongly peraluminous')

    # Boundary lines
    ax.axhline(y=1, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(x=1, color='gray', linestyle='--', linewidth=0.8)
    ax.axvline(x=1.1, color='gray', linestyle=':', linewidth=0.8)

    # Plot the data point
    ax.plot(a_cnk, a_nk, 'ko', markersize=8, zorder=5)
    ax.annotate(f'({a_cnk}, {a_nk})', (a_cnk, a_nk),
                textcoords="offset points", xytext=(5,5), fontsize=8)

    ax.set_xlim(0, 2)
    ax.set_ylim(0, 2)
    ax.set_xlabel('A/CNK')
    ax.set_ylabel('A/NK')
    ax.set_title('A/CNK vs A/NK')
    ax.legend(loc='upper right', fontsize=6)
    ax.grid(True, linestyle=':', alpha=0.5)

    plt.tight_layout()
    return fig
