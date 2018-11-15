import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

cb_matrix = pd.DataFrame([[-50, -500],[-50,0]], columns = ['Fraud', 'Not Fraud'], index = ['Fraud', 'Not Fraud'])
thresholds = np.arange(0.0, 1.0, 0.01)




def calculate_payout(confusion_matrix, cb_matrix):
    return (confusion_matrix, cb_matrix).values.sum()



def profit_curve(cb_matrix, confusion_matrix, threshold):
    profits = []
    for threshold in thresholds:
        profits.append(calculate_payout(confusion_matrix, cb_matrix))

    fig, ax = plt.subplots()
    ax.plot(thresholds, profits)
    ax.set_xlabel('thresholds')
    ax.set_ylabel('profits')
    ax.set_title('Profit Curve')