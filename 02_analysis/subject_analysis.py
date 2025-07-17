import numpy as np

#Task 1 : average signal intensity
"""
For each subject:
What is their average value for:
1. Delta
2. Theta
3. Alpha
4. Beta
"""   

#Task 2:Maximum Signal Value + Time of Peak
"""
For each subject:
1. What is the maximum signal value across all 60 seconds and 4 signals?
2. When (which second) did that peak occur?
3. Which signal type was it? (Delta, Theta, Alpha, Beta)
"""

def load_brain_data(path="./brain_data.npy"):
    return np.load(path)  #importing the data from brain_data.npy file

def calculate_avg_signals(brain_data):
    delta_avg = np.mean(brain_data[:,:,0],axis=1) #calculating delta_avg
    theta_avg = np.mean(brain_data[:, :, 1], axis=1) #calculating theta_avg
    alpha_avg = np.mean(brain_data[:, :, 2], axis=1) #calculating alpha_avg
    beta_avg = np.mean(brain_data[:, :, 3], axis=1) #calculating beta_avg

    return np.hstack([delta_avg,theta_avg,alpha_avg,beta_avg]).reshape(5,4)  #combining the avgs

def display_avg_signals(avg_data,signals):
    print("Average Signal Intensity 📶")
    for i in range(5):
        print("-" * 28)
        print(f"Subject {i} 🧠\n")
        for j,sig in zip(range(4),signals):
            print(f"{sig} -> {avg_data[i][j]}") #printing the avg data for each signal/subj

def display_max_signal_info(brain_data, signals):
    for i in range(5):
        subject_data = brain_data[i]  #taking the seconds and all signal values for each subject
        max_val = np.max(subject_data)  #extracting the maximum value
        max_pos = np.argwhere(subject_data == max_val) #extracting the positions

        print(f"\n********** SUBJECT {i} **********")
        print("Max Value:", max_val)

        for sec,signal in max_pos:  #extracting the seconds and signal from the position
            print(f"→ Peak occurred at second {sec}, signal type: {signals[signal]}")


def main(): #loading all the data
    signals = ["Delta", "Theta", "Alpha", "Beta"] 
    brain_data = load_brain_data()
    avg_data = calculate_avg_signals(brain_data)
    
    display_avg_signals(avg_data,signals)
    display_max_signal_info(brain_data,signals)

if __name__ == "__main__":
    main()