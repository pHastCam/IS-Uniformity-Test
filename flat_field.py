#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.patches as patches
import warnings


# In[2]:


INFO = """
flat_field(img, titleA, titleB, name)

Required arguments:
  img     : 2D numpy array (your cropped flat-field image)
  titleA  : string, title for the profile view
  titleB  : string, title for the bird's-eye view
  name    : string, filename to save the output figure (e.g. 'plot.png')
"""

def info():
    """Print information about the flat_field function."""
    print(INFO)



# In[3]:


def flat_field(img, titleA, titleB, name):

    x = np.arange(0, img.shape[1])
    y = np.arange(0, img.shape[0])
    X,Y = np.meshgrid(x, y)

    fig = plt.figure(figsize=(12, 6))

    #Profile
    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.tick_params(axis='x', labelsize=16, pad=2)
    ax.tick_params(axis='z', labelsize=16, pad=18)
    ax.plot_surface(X, Y, img, cmap='cividis')
    ax.set_zlim(np.average(img)*0.66, np.average(img)*1.33)
    ax.set_zlabel('Digital Number\n\n\n\n', fontsize=18)
    ax.set_xlim(0, 400)
    ax.set_xlabel('\n\nPixel Position', fontsize=18)
    ax.set_title(titleA, fontsize=28)
    ax.w_xaxis.line.set_lw(1.)
    ax.set_xticks([])
    ax.set_yticks([])

    z_label_plane = 150   
    y_label_offset = Y.min()-20  

    for x in range(0, 401, 100):
        ax.text(x, y_label_offset, z_label_plane, str(x), fontsize=16, ha='center')
        ax.plot([x, x],
            [y_label_offset, y_label_offset],  
            [z_label_plane+25, z_label_plane+40],  
            color='k', lw=.5)
    
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.view_init(0, 90)

    #Bird's eye view
    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.tick_params(axis='x', labelsize=16, pad=2)
    ax.tick_params(axis='y', labelsize=16, pad=10)
    p = ax.plot_surface(X, Y, img, cmap='cividis')
    ax.set_title(titleB, pad=38, fontsize=28)
    ax.set_xlabel('\n\nPixel Position', fontsize=18)
    ax.set_ylabel('Pixel Position\n\n\n', fontsize=18)
    cbar = fig.colorbar(p, ax=ax)
    cbar.ax.tick_params(labelsize=16)
    cbar.set_label('\nDigital Number', fontsize=16)
    ax.set_zticks([])
    ax.w_zaxis.line.set_lw(0.)
    ax.grid(False)
    ax.xaxis.pane.fill = False
    ax.yaxis.pane.fill = False
    ax.zaxis.pane.fill = False
    ax.view_init(90, 90)

    plt.savefig(name, bbox_inches='tight', dpi=400)
    plt.show()

