# Machine Learning LTE RF Fingerprinter

## MATLAB Installation Notes

This is mostly instructions for installing VNC so the GUI-only MATLAB installer can be run

As root:
```
apt install -y ubuntu-desktop tightvncserver  
apt install -y gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal xterm gcc
```

As user:
```
vncserver :1  
vim ~/.vnc/xstartup  
```

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

```
vncserver -kill :1  
vncserver :1  
```

```
export XAUTHORITY=/home/ubuntu/.Xauthority
firefox
```

Log into https://matlab.mathworks.com and download installer


```
sudo ./install
```

Include the LTE Toolkit and any of its requirements, and launch it initially with a one-time password