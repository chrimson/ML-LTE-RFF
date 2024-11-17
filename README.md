# Machine Learning LTE RF Fingerprinter

[chrimson.github.io/ML-LTE-RFF](https://chrimson.github.io/ML-LTE-RFF)  
[github.com/chrimson/ML-LTE-RFF](https://github.com/chrimson/ML-LTE-RFF)

## AWS EC2

Ubuntu 24.04  
g4dn.xlarge - 4 vCPU, 16 MiB memory, NVIDIA GPU (0.53 USD / hour)

## Linux

As root
```
apt update -y
apt upgrade -y
apt install -y python3-pip
pip install -U tensorflow[and-cuda] --root /
pip install -U scikit-learn --root /
pip install -U flask --root /
```

## NVIDIA CUDA-enabled GPU Driver

Follow NVIDIA instructions to download and install CUDA Toolkit Installer, legacy kernel module flavor of Driver Installer, and cuDNN Base Installer:

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local

https://developer.nvidia.com/cudnn-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local

Be sure to reboot. Then test, which may throw errors, but the resulting list will contain an installed GPU

```
python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"
```

## MATLAB

Be sure MATLAB R2024b is installed with its LTE Toolbox, and has been launched with a one-time password. Instructions found at [matlab.mathworks.com](https://matlab.mathworks.com)  

## Git

Clone this repository
```
git clone https://github.com/chrimson/ML-LTE-RFF.git
```

Begin trial by seeing `README.md` in the `generate` subdirectory

## License
[MIT](LICENSE)
