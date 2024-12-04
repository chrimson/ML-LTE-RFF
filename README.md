# Machine Learning LTE RF Fingerprinter
Brad Williams · Chris Limson  
GMU CYSE 640 Wireless Network Security  
Fall 2024 · Moinul Hossain, PhD  
[chrimson.github.io/ML-LTE-RFF](https://chrimson.github.io/ML-LTE-RFF)  

[DRAFT Google Docs Report](https://docs.google.com/document/d/1mlsd07kRbTbVgw_j96UPIAueAYd6eIsNKaPmCONiCx8)  

[CYSE640_BradChris_ProjectFinalPresentation.pdf](https://github.com/chrimson/ML-LTE-RFF/blob/main/doc/CYSE640_BradChris_ProjectFinalPresentation.pdf)  
[CYSE640_BradChris_ProjectProposalReport.pdf](https://github.com/chrimson/ML-LTE-RFF/blob/main/doc/CYSE640_BradChris_ProjectProposalReport.pdf)  
[CYSE640_BradChris_ProjectProposalPresentation.pdf](https://github.com/chrimson/ML-LTE-RFF/blob/main/doc/CYSE640_BradChris_ProjectProposalPresentation.pdf)

## Infrastructure Setup

### AWS EC2

Ubuntu 24.04  
g4dn.xlarge - 4 vCPU, 16 GiB memory, GPU (0.53 USD / hour)  
100 GiB storage

### Linux

As root. Copy TensorFlow inline brackets exactly
```
apt update -y
apt upgrade -y
apt install -y python3-pip
apt remove -y python3-blinker
pip install -U tensorflow[and-cuda] --root /
pip install -U scikit-learn --root /
pip install -U flask --root /
```

### NVIDIA CUDA-enabled GPU Driver

Follow NVIDIA instructions to download and install CUDA Toolkit Installer and _legacy kernel module flavor_ of Driver Installer:

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local

Be sure to reboot. Then test
```
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

Errors will be thrown but ultimately, the resulting list will contain an installed GPU
```
[PhysicalDevice(name='/physical_device:GPU:0', device_type='GPU')]
```

### MATLAB

Download and install MATLAB R2024b with its LTE Toolbox, and launch it initially with a one-time password. Instructions found at [doc/matlab_auth.md](doc/matlab_auth.md)  

### Git

Clone this repository
```
git clone https://github.com/chrimson/ML-LTE-RFF.git
```

Begin trial by seeing `README.md` in the [`generate`](https://chrimson.github.io/ML-LTE-RFF/generate) subdirectory

## License
[MIT](LICENSE)
