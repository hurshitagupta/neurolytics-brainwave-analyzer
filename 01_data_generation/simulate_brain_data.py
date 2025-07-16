import numpy as np

# creating 3D numpy array that stores brainwave signal for 5 subjects, 60 sec and 4signals(delta, theta, alpha and beta)

brain_data = np.random.randint(0,101,size=1200).reshape(5,60,4)
print("Subject 0 | First 5 seconds | Delta Signal:",brain_data[0,:5,0])

#signal names
signals = np.array(["Delta", "Theta", "Alpha","Beta"])
print("Signal order for axis=2 :",signals)

#shape of the brain data
print("Shape of brain data:",np.shape(brain_data))

#definition of each axis:
print("Axis 0: Subjects(0-4)")
print("Axis 1: Seconds(0-59)")
print("Axis 2: Signals[Delta, Theta, Alpha, Beta]")

np.save("brain_data.npy",brain_data)