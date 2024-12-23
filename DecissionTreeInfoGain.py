import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# Load the dataset
data = pd.read_csv('play_tennis.csv')

# Remove the 'day' column since it's not needed
data = data.drop(columns=['day'])

# Features and target
X = data.drop(columns=['play'])
y = data['play']

# Convert categorical data to numbers
X = pd.get_dummies(X)

# Split the dataset (90% train, 10% test)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

# Function to calculate entropy
def entropy(y):
    vals, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    ent = -np.sum(probs * np.log2(probs))
    return ent

# Function to calculate information gain
def info_gain(y, left, right):
    total_entropy = entropy(y)
    left_weight = len(left) / len(y)
    right_weight = len(right) / len(y)
    gain = total_entropy - (left_weight * entropy(left) + right_weight * entropy(right))
    return gain

# Find the best split
def best_split(X, y):
    best_feature = None
    best_value = None
    best_gain = 0
    for feature in X.columns:
        values = X[feature].unique()
        for value in values:
            left = y[X[feature] <= value]
            right = y[X[feature] > value]
            if len(left) > 0 and len(right) > 0:
                gain = info_gain(y, left, right)
                if gain > best_gain:
                    best_gain = gain
                    best_feature = feature
                    best_value = value
    return best_feature, best_value

# Recursive function to build the tree
def build_tree(X, y):
    # If all labels are the same, return that label
    if len(np.unique(y)) == 1:
        return y.iloc[0]
    
    # Find the best split
    feature, value = best_split(X, y)
    if feature is None:
        return y.mode()[0]
    
    # Split the data
    left_indices = X[feature] <= value
    right_indices = X[feature] > value
    left_tree = build_tree(X[left_indices], y[left_indices])
    right_tree = build_tree(X[right_indices], y[right_indices])
    
    return (feature, value, left_tree, right_tree)

# Function to print the tree
def print_tree(tree, spacing=""):
    if isinstance(tree, str):
        print(spacing + "Predict:", tree)
        return
    feature, value, left, right = tree
    print(spacing + f"[{feature} <= {value}]")
    print(spacing + '--> True:')
    print_tree(left, spacing + "  ")
    print(spacing + '--> False:')
    print_tree(right, spacing + "  ")

# Build and display the tree
tree = build_tree(X_train, y_train)
print_tree(tree)
