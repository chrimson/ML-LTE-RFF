### MULLET - ML LTE Fingerprinter
[Web Page](https://chrimson.github.io/MULLET)

---

### MATLAB
LTE Uplink RMC  
RF Fingerprint  
Impairments

2>/dev/null

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
pip install -U tensorflow[and-cuda] --root /
pip install -U scikit-learn --root /
```

apt remove python3-blinker

pip install flask

https://developer.nvidia.com/cuda-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local

https://developer.nvidia.com/cudnn-downloads?target_os=Linux&target_arch=x86_64&Distribution=Ubuntu&target_version=24.04&target_type=deb_local

Reboot

python3 -c "import tensorflow as tf; print(tf.config.list_physical_devices('GPU'))"

### Docker
Containers

### Kubernetes

### Ubuntu
https://stackoverflow.com/questions/38723138/matlab-execute-script-from-linux-command-line  
NGINX

https://www.google.com/search?q=flask+web+service+example&sca_esv=825ec49c2d0202bf&rlz=1C1RXQR_enUS985US986&sxsrf=ADLYWIILSdMbYqKWhJ_c7wrKgObAKc4cqw%3A1731730155186&ei=6xo4Z6WCC63X5NoP8OmhsQk&oq=flask+web+service&gs_lp=Egxnd3Mtd2l6LXNlcnAiEWZsYXNrIHdlYiBzZXJ2aWNlKgIIATIFEAAYgAQyChAAGIAEGBQYhwIyBhAAGBYYHjIGEAAYFhgeMgYQABgWGB4yCBAAGIAEGKIEMggQABiABBiiBDIIEAAYgAQYogRI_k1Qkx1YpkBwBHgBkAEAmAH1AaABuhCqAQU5LjUuM7gBA8gBAPgBAZgCFaACkRHCAgoQABiwAxjWBBhHwgIEECMYJ8ICChAjGIAEGCcYigXCAgsQABiABBiRAhiKBcICERAuGIAEGLEDGNEDGIMBGMcBwgIKEAAYgAQYQxiKBcICCBAAGIAEGLEDwgILEAAYgAQYsQMYgwHCAgoQLhiABBgnGIoFwgINEAAYgAQYsQMYQxiKBcICDRAAGIAEGLEDGBQYhwLCAgUQLhiABMICCxAAGIAEGIYDGIoFmAMAiAYBkAYIkgcGMTMuNS4zoAeEdg&sclient=gws-wiz-serp

Explanation:
Import necessary modules: We import Flask to create the web application and jsonify to convert data to JSON format.
Create Flask app: We create an instance of the Flask class.
Define sample data: A simple list of dictionaries to represent employee data.
Create a route:
@app.route('/employees', methods=['GET']): This decorator defines the URL endpoint (/employees) and the HTTP method (GET) that triggers the function.
get_employees(): This function returns the employee data as JSON.
Run the app:
if __name__ == '__main__':: This ensures the app runs only when the script is executed directly.
app.run(debug=True): Starts the Flask development server in debug mode.
To run the example:
Save the code as a Python file (e.g., app.py).
Open your terminal and navigate to the directory where you saved the file.
Run python app.py.
Access the service in your web browser at http://127.0.0.1:5000/employees. You should see the employee data in JSON format.


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
