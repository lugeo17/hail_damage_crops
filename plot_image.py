from typing import Any, Optional, Tuple

def plot_image2(
    image: np.ndarray, factor: float = 1.0, clip_range: Optional[Tuple[float, float]] = None, **kwargs: Any) -> None:
    """Utility function for plotting RGB images."""
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    if clip_range is not None:
        im = ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        im = ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    cbar = fig.colorbar(im)




from typing import Any, Optional, Tuple

def plot_image2(
    image: np.ndarray, factor: float = 1.0, clip_range: Optional[Tuple[float, float]] = None, **kwargs: Any) -> None:
    """Utility function for plotting RGB images."""
    fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(15, 15))
    if clip_range is not None:
        im = ax.imshow(np.clip(image * factor, *clip_range), **kwargs)
    else:
        im = ax.imshow(image * factor, **kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    lims = ax.imshow(image, cmap='RdBu', vmin=-1.0, vmax=1.0)
    cbar = fig.colorbar(lims)
    plt.show()


