### MULLET - ML LTE Fingerprinter
[Web Page](https://chrimson.github.io/MULLET)

---

### MATLAB
LTE Uplink RMC  
RF Fingerprint  
Impairments

### GNU Radio
Python  
SigMF

### MongoDB
Golang

### TensorFlow
C++  
Convolutional Neural Network
```
apt update -y
apt upgrade -y
apt install -y python3-pip python3-venv
pip install -U tensorflow-cpu --root /
pip install -U scikit-learn --root /
```

### Docker
Containers

### Kubernetes

### Ubuntu
https://stackoverflow.com/questions/38723138/matlab-execute-script-from-linux-command-line  
NGINX

apt install ubuntu-desktop tightvncserver  
apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal xterm gcc

vncserver :1  
vim ~/.vnc/xstartup  
```
#!/bin/sh

export XKL_XMODMAP_DISABLE=1
unset SESSION_MANAGER
unset DBUS_SESSION_BUS_ADDRESS

[ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
[ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
xsetroot -solid grey

vncconfig -iconic &
gnome-panel &
gnome-settings-daemon &
metacity &
nautilus &
gnome-terminal &
```
vncserver -kill :1  
vncserver :1  

export XAUTHORITY=/home/ubuntu/.Xauthority


/etc/ssh/sshd_config  
ChallengeResponseAuthentication yes

useradd -ms /bin/bash Chris

matlab -nodisplay -nosplash -nodesktop -r "run('path/to/your/script.m');exit;"

### AWS

---

### License
[MIT](LICENSE)
