import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

np.random.seed(0)  # For reproducibility

arr = np.random.normal(80, 30, 100)


print(arr)

flat = arr.flatten()
print(f'Flattened array: {flat}')

# Create a DataFrame
df = pd.DataFrame({'Column1': arr})


# Plotting
plt.scatter(df.index, df['Column1'])
plt.title('Scatter Plot of Column1')
plt.xlabel('Index')
plt.ylabel('Value')
plt.show()

