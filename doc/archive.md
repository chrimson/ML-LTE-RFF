# FILTERED

### RF Fingerprinting LTE for Device Identification
### Brad Williams · Chris Limson
GMU CYSE 640 Wireless Network Security  
Fall 2024 · Moinul Hossain, PhD  

<img src="images/monolith.jpg" width="200" height="300">

## Problem Statement
When a device attempts to connect to a base station, it needs to be authenticated and processed unless it has been authenticated before.  With LTE, it increases the complexity for authentication due to the LTE standards that are necessary to implement.  With technology becoming more advanced, there are an increasing number of ways to spoof a device’s MAC Address, IP address or other identifying information.  With Radio Frequency (RF) Fingerprinting, where due to imperfections in the hardware of a device when it is created there is a specific signal impairments emitted by the device, we can decipher the specific device attempting to connect to the base station.  Authenticating with a device’s RF fingerprint could make it quicker and more secure.  This is because there is currently no known way to spoof a RF fingerprint, thus allowing each device to be cataloged and identified off this attribute.

## Related Work
With the introduction of radio fingerprinting in [2], we are able to use machine learning models and software defined radio frequencies to give each device, although similar in nature, a specific RF fingerprint.  It is mentioned in [2] that “No higher level decoding, feature engineering, or protocol knowledge is needed, further mitigating challenges of ID spoofing and coexistence of multiple protocols in a shared spectrum” which would allow the protocols to be further strengthened in other directions.  Instead of having overlapping protocols for authentication, there is the possibility of a single authentication method based off the RF fingerprint, further reducing the overhead cost of authentication in each protocol.  One significant finding in this paper is that they have tested it at specific directions, notably ranging from 2 feet away to 50 feet away.  It is also mentioned that the identification remains accurate until it drops off after 34 feet.

In [1], the authors use RF fingerprinting on a variety of devices from different manufacturers and find that detecting and authenticating a user based on their RF fingerprint is a valid control.  With the authors implementing their scenario in 4G-LTE, it gives precedence for our development also centered in LTE.  There is a brief mention in the future work of the paper about how degradation can occur over the course of the hardware’s lifetime.  This could potentially cause it to no longer have the same fingerprint, or possibly emulate a similar fingerprint of another device.  Additionally, there is no note of intentional disruption of the hardware, potentially changing the fingerprint of the device.

## Proposed Solution
Further development into data for convolutional neural networks

Address 6.1 Research Challenges by building a standard dataset on cloud storage that is continually updated

Address challenge of hardware degradation, updating properties and still adjusting with deep learning

In the potentially additional interest of flagging malicious devices by only their fingerprints, as all other higher-level (logic, MAC addresses) can be altered
Impact of distance can be addressed with sensitivity of detection hardware

## Evaluation Plan
Apply large number of simulated devices to entire system's algorithm, showing how built dataset improves identification as more devices contribute

## Timeline and Milestones
October 16 - Replicate up to the described proof-of-concept simulations with MATLAB Communications, WLAN and LTE Toolboxes

October 30 - Build cloud database, use GNU Radio's Signal Metadata Format (SigMF) to store signal data 

November 13 - Test, Evaluate accuracy / speed / potential defensive process

November 27 - Writeup

December 4 - Present

## Resources
Step-by-step instructions [https://chrimson.github.io/FILTERED](https://chrimson.github.io/FILTERED)

For download or online with GMU's Campus-Wide License, MATLAB and Simulink https://matlab.mathworks.com  

GNU Radio https://www.gnuradio.org  
On Ubuntu 24.04  
```
sudo apt install gnuradio

gnuradio-companion
```

## Reference
[https://repository.library.neu.edu/files/neu:m044c531h/fulltext.pdf](https://repository.library.neu.edu/files/neu:m044c531h/fulltext.pdf)

[https://ece.northeastern.edu/fac-ece/ioannidis/static/pdf/2018/radio_identification.pdf](https://ece.northeastern.edu/fac-ece/ioannidis/static/pdf/2018/radio_identification.pdf)

Improving security of the Internet of Things via RF fingerprinting based device identification system [https://link.springer.com/article/10.1007/s00521-021-06115-2](https://link.springer.com/article/10.1007/s00521-021-06115-2)

Performance Evaluation of LTE Radio Fingerprinting using Field Measurements [https://ieeexplore.ieee.org/document/7454387](https://ieeexplore.ieee.org/document/7454387)

LTE Device Identification Based on RF Fingerprint with Multi-Channel Convolutional Neural Network [https://ieeexplore.ieee.org/document/9685067](https://ieeexplore.ieee.org/document/9685067)

Performance evaluation of LTE radio fingerprint positioning with timing advancing [https://ieeexplore.ieee.org/abstract/document/7459984](https://ieeexplore.ieee.org/abstract/document/7459984)

Radio Frequency Fingerprints Extraction for LTE-V2X: A Channel Estimation Based Methodology [https://arxiv.org/pdf/2301.01446](https://arxiv.org/pdf/2301.01446)

RF fingerprinting for user locationing in LTE/WLAN networks [https://jyx.jyu.fi/handle/123456789/51204#](https://jyx.jyu.fi/handle/123456789/51204#)

Enhanced Device FingerPrinting in 4G LTE Communication Networks [http://drsr.daiict.ac.in/handle/123456789/1055](http://drsr.daiict.ac.in/handle/123456789/1055)




The goal of collecting data from devices that employ Long-Term Evolution (LTE) presents challenges with the protection of confidentiality and authentication of integrity

When authorities do it, it's called SIGINT. When hackers do it, it's called eavesdropping.
For the sake of avoiding confusion about which perspective we mean, let's simply adhere to the convention that the attacker collects the wireless signals while the defender protects them

Initial attack demonstrated by how basic MATLAB model receives LTE. Uses LTE Toolbox end-to-end link-level simulation

Defender's counter-attack might be to obfuscate the validity of the channel, by generating multiple honeypots

Counter-counter-attack would then be to simulate radio fingerprinting of primary device, versus burner phones, to select authenticated. RF impairments with Communications Toolbox, Simulink

Download details:  
matlab_R2024b_Windows.exe (220 MB; SHA256: 2a32ddff3186306f5ed6c1b2dc996ee0978b5990f623f6511a651728e3c269f3)


Web references below should be taken with a grain of salt 🧂  
https://en.wikipedia.org/wiki/Radio_fingerprinting  
[Google: radio fingerprinting matlab](https://www.google.com/search?q=radio+fingerprinting+matlab&oq=radio+fingerprinting+matlab&gs_lcrp=EgZjaHJvbWUyBggAEEUYOTIKCAEQABiABBiiBDIKCAIQABiABBiiBDIKCAMQABiABBiiBDIKCAQQABiABBiiBDIKCAUQABiABBiiBNIBCTQwOTA0ajFqNKgCDrACAQ&client=ms-android-motorola-rvo3&sourceid=chrome-mobile&ie=UTF-8)  
HW challenge, no simulator, no research, etc.  
20-30 research papers  
Malicious access point detection of secure facility  
Man-in-the-middle attacking radio signatures  


~~We will describe the basics of what SIGINT is and how Wireless Network Security applies to it, general methodologies, logistics and systems that are fundamental~~

~~And then areas that are potentially open for innovation, development and investigation. How signal analysis can still be written for MATLAB to include environmental or experimental simulations~~

~~Hardware on an assigned plane (consisting of special things like the ugly AWACS) picks up RF signals of a questionable nation state~~

~~Raw signal waveforms are recorded and sent via securely encrypted channel to ground base station, then maybe again to where more powerful servers can organize collected data, crunch numbers~~

~~Signal analysis tools like MATLAB, Simulink and GNU Radio identifies which ones are valid, what can be cleaned up or extracted from noise, based on properties, patterns or behaviors~~

~~When does decryption occur? Are these necessarily always network data, or might it be analog/voice~~

~~Info source -> encrypt -> encode -> modulation -> air -> antenna -> radio frequency receiver -> tune to the freq of interest -> digitize (convert analog signal from the air into samples)~~

~~Digitized samples can be processed in the same place as the receiver, or they can be forwarded to a data center for processing. Also known as the forwarding channel~~

~~Demodulation -> decode -> decrypt -> info~~

~~At the info source, voice is "digitized", "compressed (voice coding)" After this it follows the same "encrypt -> encode -> modulation"~~
