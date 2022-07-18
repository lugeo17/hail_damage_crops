def plotImage(image):
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    image = image
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    im = ax.imshow(image)
    im = ax.imshow(image, vmin=-1.0, vmax=1.0)
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="3%", pad=0.1)
    cbar = fig.colorbar(im, cax=cax)
    ax.set_xticks([])
    ax.set_yticks([])