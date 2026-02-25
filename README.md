# Project pHastCam: Camera and Lighting Uniformity Experiments
This code analyzes the uniformity of our lighting setup. The three python files analyze the effectiveness of image stacking as well as the impact of banding and curvature of the camera. This data allowed us to explore some of the dominant causes of lighting error and prove that our design using smartphone cameras can provide accurate data for screening specifications. 

## Installation
1. Clone the repository
    git clone https://github.com/pHastCam/IS-Uniformity-Test.git
    cd IS-Uniformity-Test
2. Create the conda environment from YAML file
    conda env create -f environment.yml
3. Activate the environment
    conda activate IS-Uniformity-Test
4. Launch Jupyter Notebook

## Usage
1. When the environment is active, launch Jupyter Notebook 
2. Open to the notebook associated with the code in the browser interface
3. Note that several cells require changes to the local path of the files on the user's computer.

## Built with
Python 3.9
Numpy 1.21
Pandas 1.3
Matplotlib 3.5
Pillow 9.3
Rawpy 0.17.3
Opencv 4.6
Notebook 6.5.2
Exiftool 0.5.5


