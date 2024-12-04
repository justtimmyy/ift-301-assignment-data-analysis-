#Number3(a)
import matplotlib.pyplot as plt
withMusic = [304,257,174,214,69,317,387,47,157,0,332,308,317,286,236,299,206,278,188,43,0,0,0,0,0]
withoutMusic = [292,270,47,288,524,292,364,316,287,75,282,149,274,319,213,3,324,2,128,219,94,164,0,0,0]
plt.plot(withMusic, [0] * len(withMusic), 'o', color='red', label='With Music')
plt.plot(withoutMusic, [1] * len(withoutMusic), 'o', color='Black', label='Without Music')
plt.title('Growth with and without music')
plt.yticks([0,1], ['With music', 'Without music'])
plt.legend(loc='best')
plt.show()


#Number 3(a)
import matplotlib.pyplot as plt
withMusic = [304,257,174,214,69,317,387,47,157,0,332,308,317,286,236,299,206,278,188,43,0,0,0,0,0]
withoutMusic = [292,270,47,288,524,292,364,316,287,75,282,149,274,319,213,3,324,2,128,219,94,164,0,0,0]
plt.hist(withMusic, bins=10, edgecolor='black', color='red', alpha=0.6, label='with music')
plt.hist(withoutMusic, bins=10, edgecolor='red', color='black', alpha=0.6, label='without music')
plt.title('Histogram of growth')
plt.xlabel('Growth')
plt.ylabel('Frequency')
plt.legend(loc='best')
plt.show()