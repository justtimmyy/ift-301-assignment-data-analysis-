#Number2(a)
import matplotlib.pyplot as plt
breathHeld = [22.22,30.57,17.47,22.39,26.90,36.85,27.33,29.55,13.87,34.66,60.75,67.41,42.19,59.74,52.64,43.37,73.27,59.09,51.15,58.32]
plt.figure(figsize=(9,5))
plt.hist(breathHeld, bins=10,color='red', edgecolor = 'blue')
plt.xlabel('Breath Held')
plt.ylabel('Frequency')
plt.title('The histogram of breath held')
plt.show()


#Number 2(B)
import matplotlib.pyplot as plt
maleBreath = [60.75,67.41,42.19,59.74,52.64,43.37,73.27,59.09,51.15,58.32]
femaleBreath = [22.22,30.57,17.47,22.39,26.90,36.85,27.33,29.55,13.87,34.66]
plt.plot(maleBreath, [0] * len(maleBreath), 'o', label='Male', color='red')
plt.plot(femaleBreath, [1] * len(femaleBreath), 'o', label='Female', color='black')
plt.title('Side by side plot of breath held by gender')
plt.xlabel('Breath held')
plt.yticks([0,1], ['Male', 'Female'])
plt.legend()
plt.show()