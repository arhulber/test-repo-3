# %% [markdown]
# First attempt at spectroscopy csv data analysis

# %%
import pandas as pd
import matplotlib.pyplot as plt
import os

# Load data
data = pd.read_csv("sampledata.csv")

# Plot absorption spectrum
plt.figure(figsize=(8, 5))
plt.plot(data['wavelength_nm'], data['absorbance'], marker='o', linestyle='-')
plt.xlabel("Wavelength (nm)")
plt.ylabel("Absorbance")
plt.title("Absorption Spectrum")
plt.grid(True)

plt.show #JUST SHOWS THE plot below

# Make sure 'plots/' directory exists, this will create a folder called plots for the figure to go
#os.makedirs("plots", exist_ok=True)

# Save figure
#output_path = "plots/absorption_plot.png" #defines the path where you want to put the figure, names it absorption_plot.png
#plt.savefig(output_path, dpi=300) #this just saves it into the path, idk what dpi does
#plt.close()

#print(f"Spectrum saved to: {output_path}")

# %%



