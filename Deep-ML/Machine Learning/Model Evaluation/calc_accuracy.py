import numpy as np

def accuracy_score(y_true, y_pred):
    index = 0
    num_correct = 0
    while index < len(y_true) and index < len(y_pred):
        if y_true[index] == y_pred[index]:
            num_correct += 1

        index += 1
    
    return num_correct / len(y_pred)