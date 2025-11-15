import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# ------------------------------------------------------
# Step 1 — Enter your risks (Likelihood, Impact)
# These values match your Excel risk register
# ------------------------------------------------------

risk_points = {
    "R1": (4, 5),  # Likelihood, Impact
    "R2": (4, 4),
    "R3": (3, 5),
    "R4": (3, 4),
    "R5": (2, 5),
    "R6": (3, 3),
    "R7": (2, 3),
}

# Create a Likelihood x Impact grid (1–5 scale)
likelihoods = np.arange(1, 6)
impacts = np.arange(1, 6)
matrix = np.outer(likelihoods, impacts)


# ------------------------------------------------------
# Step 2 — Build heatmap
# ------------------------------------------------------
plt.figure(figsize=(7, 7))

# Show heatmap
plt.imshow(matrix, cmap="YlOrRd", origin="lower")

plt.colorbar(label="Risk Score (L x I)")

# Labels and tick marks
plt.xticks(range(5), impacts)
plt.yticks(range(5), likelihoods)
plt.xlabel("Impact (1–5)")
plt.ylabel("Likelihood (1–5)")
plt.title("Risk Heatmap — Law Firm Risk Register")

# ------------------------------------------------------
# Step 3 — Plot each risk point & label it
# ------------------------------------------------------
for rid, (likelihood, impact) in risk_points.items():
    plt.scatter(impact - 1, likelihood - 1, s=150, c="black")
    plt.text(impact - 1 + 0.05, likelihood - 1 + 0.05, rid,
             color="white", fontsize=10, fontweight="bold")


# ------------------------------------------------------
# Step 4 — Save heatmap
# ------------------------------------------------------
plt.tight_layout()
plt.savefig("Risk_Heatmap.png", dpi=200)
plt.close()

print("Heatmap saved as Risk_Heatmap.png")
