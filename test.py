import image_processing_DIO

from image_processing_DIO.processing import combination
from image_processing_DIO.utils import io, plot

img = io.read_image('/home/ernesto/Imagens/2022-10-12_10-55.png')

# combination.find_difference()
plot.plot_image(img)