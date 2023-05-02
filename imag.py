from scipy import datasets
from scipy import misc
a = datasets.face()
from matplotlib import pyplot
pyplot.imsave('vk.webp', a)
import matplotlib.pyplot as plt
plt.imshow(a)
plt.show()

