# SILENCE

### Signals Intelligence Wireless Network Security
### Brad Williams · Chris Limson
GMU CYSE 640 Wireless Network Security  
Fall 2024 · Moinul Hossain, PhD  

![](images/monolith.jpg)

The goal of collecting data from devices that employ Long-Term Evolution (LTE) presents challenges with the protection of confidentiality and authentication of integrity

When authorities do it, it's called SIGINT. When hackers do it, it's called eavesdropping.
For the sake of avoiding confusion about which perspective we mean, let's simply adhere to the convention that the attacker collects the wireless signals while the defender protects them

Initial attack demonstrated by how basic MATLAB model receives LTE. Uses LTE Toolbox end-to-end link-level simulation

Defender's counter-attack might be to obfuscate the validity of the channel, by generating multiple honeypots

Counter-counter-attack would then be to simulate radio fingerprinting of primary device, versus burner phones, to select authenticated. RF impairments with Communications Toolbox, Simulink


## Resources

Step-by-step instructions [https://chrimson.github.io/SILENCE](https://chrimson.github.io/SILENCE)

For download or online with GMU's Campus-Wide License, MATLAB and Simulink https://matlab.mathworks.com  
Download details:  
matlab_R2024b_Windows.exe (220 MB; SHA256: 2a32ddff3186306f5ed6c1b2dc996ee0978b5990f623f6511a651728e3c269f3)

GNU Radio https://www.gnuradio.org  
On Ubuntu 24.04  
```
sudo apt install gnuradio

gnuradio-companion
```


## Reference

Performance Evaluation of LTE Radio Fingerprinting using Field Measurements [https://ieeexplore.ieee.org/document/7454387](https://ieeexplore.ieee.org/document/7454387)

LTE Device Identification Based on RF Fingerprint with Multi-Channel Convolutional Neural Network [https://ieeexplore.ieee.org/document/9685067](https://ieeexplore.ieee.org/document/9685067)

Performance evaluation of LTE radio fingerprint positioning with timing advancing [https://ieeexplore.ieee.org/abstract/document/7459984](https://ieeexplore.ieee.org/abstract/document/7459984)

Radio Frequency Fingerprints Extraction for LTE-V2X: A Channel Estimation Based Methodology [https://arxiv.org/pdf/2301.01446](https://arxiv.org/pdf/2301.01446)

Improving security of the Internet of Things via RF fingerprinting based device identification system [https://link.springer.com/article/10.1007/s00521-021-06115-2](https://link.springer.com/article/10.1007/s00521-021-06115-2)

RF fingerprinting for user locationing in LTE/WLAN networks [https://jyx.jyu.fi/handle/123456789/51204#](https://jyx.jyu.fi/handle/123456789/51204#)

Enhanced Device FingerPrinting in 4G LTE Communication Networks [http://drsr.daiict.ac.in/handle/123456789/1055](http://drsr.daiict.ac.in/handle/123456789/1055)


## Documentation
(placeholders for now)  
[CYSE640_BradChris_ProjectProposalPresentation.pdf](docs/CYSE640_BradChris_ProjectProposalPresentation.pdf)  
[CYSE640_BradChris_ProjectProposalReport.pdf](docs/CYSE640_BradChris_ProjectProposalReport.pdf)  
[CYSE640_BradChris_ProjectFinalPresentation.pdf](docs/CYSE640_BradChris_ProjectFinalPresentation.pdf)  
[CYSE640_BradChris_ProjectFinalReport.pdf](docs/CYSE640_BradChris_ProjectFinalReport.pdf)  


## Notes
Web references below should be taken with a grain of salt 🧂  
https://en.wikipedia.org/wiki/Radio_fingerprinting  
[Google: radio fingerprinting matlab](https://www.google.com/search?q=radio+fingerprinting+matlab&oq=radio+fingerprinting+matlab&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIKCAMQABiABBiiBDIKCAQQABiABBiiBDIKCAUQABiABBiiBNIBCTQwOTA0ajFqNKgCDrACAQ&client=ms-android-motorola-rvo3&sourceid=chrome-mobile&ie=UTF-8)    
HW challenge, no simulator, no research, etc.  
20-30 research papers  
Malicious access point detection of secure facility  
Man-in-the-middle attacking radio signatures  
[Archive](archive.md)


## License
[MIT](LICENSE)
