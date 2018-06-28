# Acoustic signature recognition

Heavly based on the work of Dr. Scott Hawley's work, with modifications where needed.
Please visit his github for more details. 
https://github.com/drscotthawley/panotti


## Installation

### Prerequisites

* Python 3.5
* numpy
* keras
* tensorflow
* librosa
* matplotlob
* h5py
* sox


### Usage

* Clone repo locally
* Create folder named "Samples/"
	* Create subfolders with a namespace corresponding to classnames
	* (vessel_small, vessel_large, background_noise)
* Run "preprocess_data.py"
* Run "train_network.py"
* Run "eval_network.py"



