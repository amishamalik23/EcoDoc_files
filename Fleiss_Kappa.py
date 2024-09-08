import pandas as pd
import numpy as np
import statsmodels.stats.inter_rater as irr

# Load the data from the Excel file
file_path = 'C:/Users/amish/OneDrive/Desktop/inter-rater agreement/uber_ground_truth.xlsx'  # Update this to the correct path
  
data = pd.read_excel(file_path, sheet_name='whatsapp')

# Strip any leading/trailing whitespace from column names
data.columns = data.columns.str.strip()

# Extract the necessary columns for ratings
ratings = data[['Total Yes', 'Total No', 'Total N/A']]

# Ensure each row sums to 5 ratings
ratings['Total'] = ratings.sum(axis=1)
ratings = ratings[ratings['Total'] == 5].drop(columns=['Total'])

# Transform into matrix format required for Fleiss' kappa
ratings_matrix = ratings.to_numpy()

# Calculate Fleiss' kappa
kappa = irr.fleiss_kappa(ratings_matrix, method='fleiss')

# Print the result
print("Fleiss' kappa:", kappa)
