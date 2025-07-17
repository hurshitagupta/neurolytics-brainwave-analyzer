import numpy as np

brain_data = np.load("./brain_data.npy")
# print(brain_data)

#Task 1 : average signal intensity
"""
For each subject:
What is their average value for:
1. Delta
2. Theta
3. Alpha
4. Beta
"""

#calculating average value for delta signal
delta_signal = brain_data[:,:,0]
avg_delta = np.mean(delta_signal,axis=1)

#calculating average value for theta signal
theta_signal = brain_data[:,:,1]
avg_theta = np.mean(theta_signal,axis=1)

#calculating average value for alpha signal
alpha_signal = brain_data[:,:,2]
avg_alpha = np.mean(alpha_signal,axis=1)

#calculating average value for beta signal
beta_signal = brain_data[:,:,3]
avg_beta = np.mean(beta_signal,axis=1)

# combining the avearges of all the signals into one array 
all_avgs = np.hstack([avg_delta,avg_theta,avg_alpha,avg_beta]).reshape(5,4)
# print("Averages of each signal for all subjects:\n",all_avgs)

signals = ["Delta", "Theta", "Alpha", "Beta"]

print("Average Signal Intensity 📶")
for i in range(5):
    print("-" * 28)
    print(f"Subject {i} 🧠\n")
    for j,sig in zip(range(4),signals):
        print(f"{sig} -> {all_avgs[i][j]}")
    

#Task 2:Maximum Signal Value + Time of Peak
"""
For each subject:
1. What is the maximum signal value across all 60 seconds and 4 signals?
2. When (which second) did that peak occur?
3. Which signal type was it? (Delta, Theta, Alpha, Beta)
"""
signals = ["Delta", "Theta", "Alpha", "Beta"]

for i in range(5):
    subject_data = brain_data[i]  #taking the seconds and all signal values for each subject
    max_val = np.max(subject_data)  #extracting the maximum value
    max_pos = np.argwhere(subject_data == max_val) #extracting the positions

    print(f"\n********** SUBJECT {i} **********")
    print("Max Value:", max_val)

    for sec,signal in max_pos:  #extracting the seconds and signal from the position
        print(f"→ Peak occurred at second {sec}, signal type: {signals[signal]}")

