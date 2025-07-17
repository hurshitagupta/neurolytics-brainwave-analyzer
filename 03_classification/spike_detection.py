import numpy as np

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '02_analysis')))
from subject_analysis import calculate_avg_signals


brain_data = np.load("./brain_data.npy")
avg_data = calculate_avg_signals(brain_data)


def spike_detection(subjects,signals):
    for subject in subjects:
        print("*"*30)
        print("Abnormal Spikes Of Subject",subject)
        
        for j,signal in enumerate(signals):

            spikes = np.where(brain_data[subject,:,j] > avg_data[subject][j])[0]
            print(f"{signal} : {spikes}\n")


def main():
    
    subjects = [0,1,2,3,4]
    signals = ["delta","theta","alpha","beta"]

    spike_detection(subjects,signals)

    
if __name__ == "__main__":
    main()



