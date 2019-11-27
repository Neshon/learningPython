import matplotlib.pyplot as plt
from random_walk import RandomWalk


rm = RandomWalk()
rm.will_walk()
point_numbers = list(range(rm.num_points))
# plt.scatter(rm.x_values, rm.y_values, c=point_numbers,cmap=plt.cm.Blues,
#             edgecolors='none', s=15)
# plt.scatter(0, 0, c='green', edgecolors='none', s=100)
# plt.scatter(rm.x_values[-1], rm.y_values[-1], c='red', edgecolors='none',
#             s=100)
plt.plot(rm.x_values, rm.y_values, linewidth=1)
plt.show()



