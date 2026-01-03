This repository supports a University of Washington project to develop a low-cost imaging tool that measures pH changes induced by coatings that host dye indicators.  The first milestone of this project is to use pH indicator strips as reliable quantitative sensors, achieving specs established by UNICEF. Ultimately, we plan to use these tools to screen for hypoxic-ischemic encephalopathy in babies.

## Integrating Sphere Construct
The figure below shows the 3D-printed integrating-sphere setup.  Panel A shows a cut-away model of the sphere.  The trough at the base hosts a ring lamp consisting of red AlInGaP LEDs.  The baffle above the trough shields the camera from direct line-of-sight with the LEDs.  The camera mount is best shown in Panel B.  The smartphone display shows locating features for the test sample (test sample not included in the image).  To evaluate uniformity and noise, we place a Labsphere diffuse reflectance standard (Panel C) within the locating features inside the sphere.  We then take five consecutive images, one of which is shown in Panel D.
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/set-up.jpg"> 
</p>
<br>

## Uniformity/Noise Evaluation
The smartphone camera captures the diffuse reflectance standard as a RAW image file.  The 'Curve Analysis.ipynb' in this repository then plots the digital number (z-axis) as a function of pixel location (x and y axis) and produces the plots shown below. The first set of graphs (labeled A and B) is of a single image. From here we see that there are three types of non-uniformities: (a) a gross curvature pointed to the limited lighting uniformity (Panel A), (b) a high frequency feature associated with camera noise (variable) and target texture (fixed) (also Panel A), and (c) electronic banding associated with both the LED pulse-width-modulation and the rolling shutter or readout speed (Panel B).  
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/uniformity.png"> 
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

<table style="margin-left: auto; margin-right: auto;">
  <thead>
    <tr>
      <th>Window</th>
      <th>Centroid (cx, cy)</th>
      <th>Patch top-left (x0, y0)</th>
      <th>Curvature span (p95–p5)</th>
      <th>% of mean</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>center</td>
      <td>(200, 200)</td>
      <td>(185, 185)</td>
      <td>2.33 DN</td>
      <td>0.74%</td>
    </tr>
    <tr>
      <td>right_lower</td>
      <td>(300, 100)</td>
      <td>(285, 85)</td>
      <td>4.32 DN</td>
      <td>1.38%</td>
    </tr>
    <tr>
      <td>right_upper</td>
      <td>(300, 300)</td>
      <td>(285, 285)</td>
      <td>4.26 DN</td>
      <td>1.36%</td>
    </tr>
    <tr>
      <td>left_lower</td>
      <td>(100, 100)</td>
      <td>(85, 85)</td>
      <td>4.38 DN</td>
      <td>1.39%</td>
    </tr>
    <tr>
      <td>left_upper</td>
      <td>(100, 300)</td>
      <td>(85, 285)</td>
      <td>3.30 DN</td>
      <td>1.05%</td>
    </tr>
  </tbody>
  <caption>
    2D quadratic curvature metric on 30×30 windows (centroids inset by 100 px; curvature = p95–p5 of fitted surface).
  </caption>
</table>

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

