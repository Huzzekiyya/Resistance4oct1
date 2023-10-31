import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

filename = "Trial_D349_3_Session28_Shimmer__Calibrated_PC.csv"
df = pd.read_csv(filename, delimiter='\t', skiprows=[0, 2])

# Create a new figure with two subplots arranged horizontally
plt.figure(figsize=(20, 4))  # Adjust the figure size as needed
plt.suptitle("Shimmer Data")

# Plot GSR Skin Resistance
plt.subplot(121)  # 1 row, 2 columns, first subplot
plt.plot(df.iloc[:, [6]])
plt.title('GSR Skin Resistance Over Time')
plt.xlabel('timestamp')
plt.ylabel('GSR Skin Resistance')
plt.grid(True)

# Plot GSR Skin Conductance
plt.subplot(122)  # 1 row, 2 columns, second subplot
plt.plot(df.iloc[:, [5]])
plt.title('GSR Skin Conductance CAL')
plt.xlabel('timestamp')
plt.ylabel('GSR Skin Conductance')
plt.grid(True)

plt.show()
