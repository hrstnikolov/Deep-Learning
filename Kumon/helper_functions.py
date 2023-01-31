import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def print_image(image, ax=None, name=None):
    """Prints a single image."""
    if not ax:
        fig, ax = plt.subplots(1, 1)
    ax.imshow(image, cmap='gray')
    if name:
        ax.set_title(name)
    ax.axis('off')

    
def print_images(images, names=None):
    """Prints multiple images in a row."""
    fig, axs = plt.subplots(nrows=1, ncols=len(images), figsize=(4 * len(images), 3))
    
    if not names:
        names = [''] * len(images)
    
    for ax, image, name in zip(np.ravel(axs), images, names):
        print_image(image, ax, name)

    plt.tight_layout()
    
    
def describe_image(image):
    '''Prints out the value range and shape of an image.'''
    print(f'min: {image.min():2.2f}')
    print(f'max: {image.max():2.2f}')
    print(f'shape: {image.shape}')
    

def describe_images(images, names=None):
    '''Prints out the value range and shape for multiple images.'''
    if not names:
        names = [''] * len(images)
    for image, name in zip(images, names):
        if name:
            print(name)
        describe_image(image)
        print()