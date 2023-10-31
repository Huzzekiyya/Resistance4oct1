import pandas as pd
import matplotlib.pyplot as plt

filename = "conductance_Session2_Shimmer_D349_Calibrated_PC_calm1.csv"
df = pd.read_csv(filename, delimiter='\t', skiprows=[0, 2])
df.head(5)
# Create a new figure with two subplots arranged horizontally
plt.figure(figsize=(20, 4))  # Adjust the figure size as needed
plt.suptitle("Shimmer Data")

# Plot GSR Skin Resistance
plt.subplot(121)  # 1 row, 2 columns, first subplot
plt.plot(df['Shimmer_D349_TimestampSync_Unix_CAL'], df['Shimmer_D349_GSR_Skin_Resistance_CAL'])
plt.title('GSR Skin Resistance Over Time')
plt.xlabel('timestamp')
plt.ylabel('GSR Skin Resistance')
plt.grid(True)

# Plot GSR Skin Conductance
plt.subplot(122)  # 1 row, 2 columns, second subplot
plt.plot(df['Shimmer_D349_TimestampSync_Unix_CAL'], df['Shimmer_D349_GSR_Skin_Conductance_CAL'])
plt.title('GSR Skin Conductance CAL')
plt.xlabel('timestamp')
plt.ylabel('GSR Skin Conductance')
plt.grid(True)

plt.show()