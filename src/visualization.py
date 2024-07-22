from matplotlib.pyplot import imshow, show
from numpy import reshape, copy
from numpy.ma import getmask, masked_where

def make_image(data):
    data = copy(data)
    data = reshape(data, (len(data), len(data)))

    # Set custom color for 0.0s to white
    cmap = 'viridis'
    data[data == 0.0] = float('nan')

    # Use masked array to ignore nan values during colormap normalization
    masked_data = masked_where(getmask(data), data)

    imshow(masked_data, interpolation='none', cmap=cmap)
    show()
