import numpy as np

# Create a NumPy array
scores = np.array([85, 92, 78, 88, 90])

# Print the array
print("Scores:", scores)

# Get basic stats
print("Mean:", np.mean(scores))
print("Max:", np.max(scores))
print("Min:", np.min(scores))

# Add 5 bonus points to everyone
bonus_scores = scores + 5
print("Scores with bonus:", bonus_scores)
