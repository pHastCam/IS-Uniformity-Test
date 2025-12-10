This repository supports a University of Washington project to develop a low-cost imaging tool that measures pH changes induced by coatings that host dye indicators.  The first milestone of this project is to use pH indicator strips as reliable quantitative sensors, achieving specs established by UNICEF. Ultimately, we plan to use these tools to screen for hypoxic-ischemic encephalopathy in babies.

## Integrating Sphere Construct
The figure below shows the 3D-printed integrating-sphere setup.  Panel A shows a cut-away model of the sphere.  The trough at the base hosts a ring lamp consisting of red AlInGaP LEDs.  The baffle above the trough shields the camera from direct line-of-sight with the LEDs.  The camera mount is best shown in Panel B.  The smartphone display shows locating features for the test sample (test sample not included in the image).  To evaluate uniformity and noise, we place a Labsphere diffuse reflectance standard (Panel C) within the locating features inside the sphere.  We then take five consecutive images, one of which is shown in Panel D.
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/set-up.jpg"> 
</p>
<br>

## Uniformity/Noise Evaluation
The smartphone camera captures the diffuse reflectance standard as a RAW file.  The uniformity.ipynb file in this repository then plots the digital number (z-axis) as a function of pixel location (x and y axis) and produces the plots shown below. The first set of images (labeled A and B) is of a single image. From here we see that there are three types of non-uniformities: (a) a gross curvature pointed to the limited lighting uniformity (Panel A), (b) a high frequency feature associated with camera noise (variable) and target texture (fixed) (also Panel A), and (c) electronic banding associated with both the LED pulse-width-modulation and the rolling shutter speed (Panel B).  
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/uniformity.png"> 
</p>
<br>

<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/uniformity_stack.png"> 
</p>
<br>

## High Frequency Noise - Teasing out Deterministic vs. Stochastic Noise
<br><br>
<p align="center" width="100%">
    <img width="60%" src="https://github.com/pHastCam/IS-Uniformity-Test/blob/main/HF_Noise_Eval.png"> 
</p>
<br>
