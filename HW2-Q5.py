import numpy as np

# Q5 - Part 3: Programming Implementation

# Step 1 (Q5.3.1): Accept the confusion matrix as input
conf_matrix = np.array([
    [5, 10, 5],     # Predicted Cat
    [15, 20, 10],   # Predicted Dog
    [0, 15, 10]     # Predicted Rabbit
])

def compute_metrics(matrix):
    num_classes = matrix.shape[0]
    precisions, recalls = [], []

    # Step 2 (Q5.3.2): Compute per-class precision and recall
    print("Per-Class Precision and Recall:")
    for i in range(num_classes):
        TP = matrix[i, i]
        FP = np.sum(matrix[:, i]) - TP
        FN = np.sum(matrix[i, :]) - TP

        precision = TP / (TP + FP) if (TP + FP) != 0 else 0
        recall = TP / (TP + FN) if (TP + FN) != 0 else 0

        precisions.append(precision)
        recalls.append(recall)
        print(f"Class {i+1}: Precision = {precision:.4f}, Recall = {recall:.4f}")

    # Step 3 (Q5.3.3): Compute macro-averaged precision and recall
    macro_precision = np.mean(precisions)
    macro_recall = np.mean(recalls)

    # Step 3 continued (Q5.3.3): Compute micro-averaged precision and recall
    TP_total = np.trace(matrix)
    FP_FN_total = np.sum(matrix) - TP_total

    micro_precision = TP_total / (TP_total + FP_FN_total)
    micro_recall = TP_total / (TP_total + FP_FN_total)

    # Step 4 (Q5.3.4): Print all results clearly
    print("\nMacro-Averaged Precision:", round(macro_precision, 4))
    print("Macro-Averaged Recall   :", round(macro_recall, 4))
    print("Micro-Averaged Precision:", round(micro_precision, 4))
    print("Micro-Averaged Recall   :", round(micro_recall, 4))

# Run the function
compute_metrics(conf_matrix)