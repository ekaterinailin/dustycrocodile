import imageio
import numpy as np
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')
data = []
for i in range(2000,2016):
	data.append('map'+str(i)+'.png')
filenames = np.array(data)
images=[]
for filename in filenames:
	images.append(imageio.imread(filename))
imageio.mimsave('gif.gif', images, duration=1)
