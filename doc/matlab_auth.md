# Machine Learning LTE RF Fingerprinter

## MATLAB Installation Notes

```
apt install ubuntu-desktop tightvncserver  
apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal xterm gcc

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
---
