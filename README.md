This repository supports a University of Washington project to develop a low-cost imaging tool that measures pH changes induced by coatings that host dye indicators.  The first milestone of this project is to use pH indicator strips as reliable quantitative sensors, achieving specs established by UNICEF. Ultimately, we plan to use these tools to screen for hypoxic-ischemic encephalopathy in babies.

## Integrating Sphere Construct
The figure below shows the 3D-printed integrating-sphere setup.  Panel A shows a cut-away model of the sphere.  The trough at the base hosts a ring lamp consisting of red AlInGaP LEDs.  The baffle above the trough shields the camera from direct line-of-sight with the LEDs.  The camera mount is best shown in Panel B.  The smartphone display shows locating features for the test sample (test sample not included in the image).  To evaluate uniformity and noise, we place a Labsphere diffuse reflectance standard (Panel C) within the locating features inside the sphere.  We then take five consecutive images, one of which is shown in Panel D.
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/set-up.jpg"> 
</p>
<br>

## Uniformity/Noise Evaluation
The smartphone camera captures the diffuse reflectance standard as a RAW image file.  The 'Curve Analysis.ipynb' in this repository then plots the digital number (z-axis) as a function of pixel location (x and y axis) and produces the plots shown below. The first set of graphs (labeled A and B) is of a single image. 

<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/uniformity.png"> 
</p>

From here we see that there are three types of non-uniformities: (a) a gross curvature pointed to the limited lighting uniformity (Panel A), (b) a high frequency feature associated with camera noise (variable) and target texture (fixed) (also Panel A), and (c) electronic banding associated with both the LED pulse-width-modulation and the rolling shutter or readout speed (Panel B) in accordance with the following equation:

<br>
<p align="center">
  <img src="https://latex.codecogs.com/svg.latex?%5Cnormalsize%20Error%3Df(curvature%2Cbanding%2CHF%20noise)"
       alt="Error = f(curvature, banding, HF noise)">
</p>


<br>
We can reduce both the banding and camera-generated high-frequency noise by stacking multiple images.  The same program stacks multiple images (in this case, 5) and replots the digital number as a function of pixel location (see Panels C and D).  
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/uniformity_stack.png"> 
</p>
<br>
From here, we will quantify the error associated with curvature, banding, and high-frequency noise.


## Curvature
Quantifying curvature is best explained using a 1D profile of the stack images.  We will then map this approach over to the 2D data. The graphs below show (a) a mask used on a 400x400 pixel ROI (same ROI used to generate the flat-field graphs above) and (b) the 1-D profile of the stacked data.  The blue line shows the original data, with clear curvature and high-frequency noise.  The orange line represents the low-spatial-frequency mean illumination profile, capturing smooth curvature while excluding the high-frequency noise.  The light blue bars on the graph align with the five smaller squares shown in the mask.  Curvature is determined within five smaller squares mapped onto the 1-D profile and is calculated as the robust DN range (5–95%) of the low-spatial-frequency mean profile over these ROI-sized windows in accordance with the equation below.

<p align="center" width="100%">
  <img src="https://latex.codecogs.com/svg.latex?%5Cnormalsize%20C_%7BW%7D%3DP_%7B95%7D%5Cleft(%5Cbar%7BI%7D_%7BLF%7D(x)%5Cright)-P_%7B5%7D%5Cleft(%5Cbar%7BI%7D_%7BLF%7D(x)%5Cright)"
       alt="Curvature DN span"/>
</p>
<br>

<p>
Here, <b><i>C</i></b> denotes the error associated with curvature;
<b><i>p</i></b><sub>5</sub> and <b><i>p</i></b><sub>95</sub> are the 5th and 95th DN percentiles
computed over the analysis window; and <b><i>I(x)</i></b> is the smoothed,
low-spatial-frequency 1-D DN profile.
</p>

<br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/Maskand1DCurve.png"> 
</p>
<br>
Curvature.py is a function that maps this analysis over to a 2-D flat-field image.  For the five small squares shown in the above mask, the calculated curvature values are presented in the table below. The curvature metric shows a consistent geometric dependence across the field of view: it is smallest in the central window (2.33 DN, 0.74% of mean) and larger in all four peripheral windows (≈3.3–4.4 DN, ≈1.05–1.39% of mean). This repeatable, smoothly varying spatial pattern is consistent with a low-spatial-frequency illumination/optical roll-off (a fixed bias field within a measurement session), rather than a stochastic term that would vary irregularly with location or average down with stacking.
<br><br>
<p align="center" width="100%">
    <img width="80%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/table_curvature.png"> 
</p>
<br>

## Banding
As shown in the flat-field graph above for a single frame, banding is directional. To calculate the banding contribution to error, we first flatten the image (remove the curvature using the analysis info from Curvature.ipynb) and then generate an average column profile (not by row, but by column).  We will use two different methods to calculate banding error from this one-dimensional data set.   

### Method 1

<br>
<p align="center" width="100%">
    <img src="https://latex.codecogs.com/svg.latex?\normalsize\sigma_{\mathrm{total}}^{2}=\sigma_{\mathrm{high\ frequency}}^{2}-\sigma_{\mathrm{mid\ frequency}}^{2}" alt="sigma5 actual squared"/> 
</p> 
<br>
<p align="center" width="100%">
    <img width="80%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/bandingbymovingwindow.png"> 
</p>
<br>


## High Frequency Noise - Teasing out Deterministic vs. Stochastic Noise
The high-frequency artifacts have two major components: one from surface texture, the other from camera noise. The surface texture is fixed or deterministic, hence stacking multiple images will not reduce this component.  The camera noise has two subcomponents: one from shot noise and the other from readout noise.  Although these two subcomponents stem from different events, both are variable and stochastic, and may be reduced by stacking by the inverse of the square root of the sample size (<img src="https://latex.codecogs.com/svg.latex?\normalsize\sqrt{N}" alt="sqrt(N)"/>).

The variance of the high-frequency artifacts may be modeled as:
<br><br>
<p align="center">
    <img src="https://latex.codecogs.com/svg.latex?\normalsize\;\sigma_{\mathrm{HF}}^{2}(N)=\sigma_{\mathrm{texture}}^{2}+\frac{\sigma_{\mathrm{noise}}^{2}}{N}" alt="HF variance model"/>
</p>
<br>
We can estimate the fraction of these high-frequency artifacts associated with each component by assuming that all high-frequency data from the first image (N=1) are due to camera noise, and then projecting how the standard deviation of the noise behaves as we increase N from 1 to 5.  We then compare these modeled results to the standard deviation of actual data as we stack images from 1 to 5.  If the two curves are identical, then we can attribute the artifacts entirely to stochastic noise from the camera.  If, on the other hand, we see a discrepancy between the two curves, the difference may be attributed to fixed features, such as sensor-fixed patterning and surface texture. The plot below shows a significant discrepancy between these two conditions.
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/HF_Noise_Eval.png"> 
</p>
<br>
For the case of the diffuse reflectance standard, you can pull the standard deviations for each condition from the graph and calculate the variance:

<br><br>
<p align="center" width="100%">
    <img src="https://latex.codecogs.com/svg.latex?\normalsize\sigma_{5,\mathrm{actual}}^{2}=8.37^{2}=70.06" alt="sigma5 actual squared"/> 
</p> 
<br>
<p align="center" width="100%">
    <img src="https://latex.codecogs.com/svg.latex?\normalsize\sigma_{5,\mathrm{camera}}^{2}=4.18^{2}=17.47" alt="sigma5 actual squared"/> 
</p> 
<br>
<p align="center" width="100%">
    <img src="https://latex.codecogs.com/svg.latex?\normalsize\sigma_{5,\mathrm{fixed}}^{2}=\sigma_{5,\mathrm{actual}}^{2}-\sigma_{5,\mathrm{camera}}^{2}=52.59" alt="sigma5 actual squared"/> 
</p> 
<br>
So the fraction of fixed high-frequency artifacts attributed to surface texture (diffuse reflectance standard) and sensor-fixed patterns (camera) is 52.59 / 70.06 = 75.1% while the fraction attributed to camera variable noise is 17.47 / 70.06 = 24.9%.

