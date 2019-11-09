
from img_data import ImgData 
import numpy as np 
from matplotlib import pyplot as plt


"""
    every class call method should have only these two params data.imgs and data.labels

"""
class display_images_per_class:

    def __init__(self,no_times=1,figsize=(8,3)):

        self.no_times=no_times
        self.figsize=figsize
        
    def __call__(self,data.imgs,data.labels):
      
      class_names=list(np.unique(data.labels))

      for i in range(self.no_times):
        
        fig = plt.figure(figsize=self.figsize)
        for i in range(num_classes):
            ax = fig.add_subplot(2, 5, 1 + i, xticks=[], yticks=[])
            idx = np.where(data.labels[:]==i)[0]
            features_idx = data.imgs[idx,::]
            img_num = np.random.randint(features_idx.shape[0])
            im = features_idx[img_num]
            ax.set_title(class_names[i])
            plt.imshow(im)

        plt.show()

    

