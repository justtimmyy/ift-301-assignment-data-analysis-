import matplotlib.pyplot as plt
food = ['sausage','spinach','pineapple','mushroom','prawns']
x = [50,25,16,55,30]
plt.barh(food,x,0.5, color='red', edgecolor='black')
plt.xlabel('amount')
plt.ylabel('Food')
plt.show()