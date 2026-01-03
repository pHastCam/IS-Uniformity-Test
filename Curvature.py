#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


INFO = """
Computes local low-spatial-frequency curvature as the 5–95% DN range of a
2-D quadratic illumination model fitted to a win×win sub-ROI centered at
(cx, cy) within a 2-D image.

analyze(im, cx, cy, win, margin)

Required arguments:
  im      : 2D numpy array
            Image data in DN.
  cx, cy  : int
            Sub-ROI center location in full-image pixel coordinates.
  win     : int
            Width (and height) in pixels of the square sub-ROI.
  margin  : int
            Minimum allowed distance (in pixels) between the sub-ROI center
            and the image edge; enforced as a validity check.

Notes:
  - Curvature represents smooth, low-spatial-frequency deviation from the
    mean illumination field.
  - The function raises an error if the requested ROI center violates the
    margin constraint.
"""


def info():
    """Print information about the flat_field function."""
    print(INFO)

def analyze(im, cx, cy, win, margin):

    H, W = im.shape
    mean_dn = im.mean()

    # Enforce margin constraint (do NOT silently move the ROI)
    if cx < margin or cx > W - margin or cy < margin or cy > H - margin:
        raise ValueError(
            f"ROI center (cx={cx}, cy={cy}) violates margin={margin} constraint"
        )

    # Convert centroid to top-left
    x0 = int(round(cx - win / 2))
    y0 = int(round(cy - win / 2))

    # Clamp only to protect against rounding
    x0 = int(np.clip(x0, 0, W - win))
    y0 = int(np.clip(y0, 0, H - win))

    patch = im[y0:y0+win, x0:x0+win]

    yy, xx = np.mgrid[0:win, 0:win]

    A = np.column_stack([
        np.ones(win * win),
        xx.ravel(),
        yy.ravel(),
        (xx**2).ravel(),
        (xx * yy).ravel(),
        (yy**2).ravel()
    ])

    coef, *_ = np.linalg.lstsq(A, patch.ravel(), rcond=None)

    fit = (
        coef[0]
        + coef[1]*xx + coef[2]*yy
        + coef[3]*xx**2 + coef[4]*xx*yy + coef[5]*yy**2
    )

    p5  = np.percentile(fit, 5)
    p95 = np.percentile(fit, 95)

    curv_range = float(p95 - p5)
    curv_pct   = float(100 * curv_range / mean_dn)

    return curv_range, curv_pct, (x0, y0)


