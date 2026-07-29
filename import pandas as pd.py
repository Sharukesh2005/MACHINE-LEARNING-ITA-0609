import pandas as pd

# -------------------------------
# Function to initialize S and G
# -------------------------------
def initialize(data):
    num_attr = len(data.columns) - 1
    S = ['0'] * num_attr
    G = [['?' for _ in range(num_attr)]]
    return S, G

# ---------------------------------------
# Candidate Elimination Algorithm
# ---------------------------------------
def candidate_elimination(data):

    concepts = data.iloc[:, :-1].values
    target = data.iloc[:, -1].values

    S, G = initialize(data)

    print("Initial Specific Hypothesis (S):", S)
    print("Initial General Hypothesis (G):", G)

    for i, instance in enumerate(concepts):

        if target[i] == "Yes":

            # Update Specific Hypothesis
            for j in range(len(S)):
                if S[j] == '0':
                    S[j] = instance[j]
                elif S[j] != instance[j]:
                    S[j] = '?'

            # Remove inconsistent hypotheses from G
            G = [g for g in G if all(g[k] == '?' or g[k] == S[k] for k in range(len(S)))]

        else:

            new_G = []

            for g in G:
                for j in range(len(S)):
                    if S[j] != '?' and instance[j] != S[j]:
                        new_hypothesis = g.copy()
                        new_hypothesis[j] = S[j]

                        if new_hypothesis not in new_G:
                            new_G.append(new_hypothesis)

            G = new_G

        print("\nStep", i + 1)
        print("Training Example:", instance, "->", target[i])
        print("Specific Hypothesis (S):", S)
        print("General Hypothesis (G):", G)

    print("\n===============================")
    print("Final Specific Boundary (S):", S)
    print("Final General Boundary (G):")

    for g in G:
        print(g)


# ---------------------------------------
# Main Program
# ---------------------------------------

data = pd.read_csv("training_data.csv")

candidate_elimination(data)