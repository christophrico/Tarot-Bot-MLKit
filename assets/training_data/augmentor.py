import Augmentor
import os

path = "./../training_data"
class_folders = os.listdir(path)

for folder in class_folders:
    # instantiate the pipeline
    p = Augmentor.Pipeline("./../training_data/{}".format(folder))

    # add in operatons to it
    p.rotate(probability=0.3, max_left_rotation=15, max_right_rotation=15)
    p.skew(probability=0.3, magnitude=0.2)
    p.shear(probability=0.4, max_shear_left=15, max_shear_right=15)
    p.crop_random(probability=0.3, percentage_area=0.7, randomise_percentage_area=True)
    p.random_distortion(probability=0.5, grid_width=5, grid_height=5, magnitude=5)
    p.random_erasing(probability=0.3, rectangle_area=0.6)

    p.random_brightness(probability=0.7, min_factor=0.5, max_factor=2)
    p.greyscale(probability=0.3)
    p.random_color(probability=0.6, min_factor=0.5, max_factor=2)
    p.random_contrast(probability=0.5, min_factor=0.5, max_factor=2)

    p.sample(500)
