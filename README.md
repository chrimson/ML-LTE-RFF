# SILENCER

### Signals Intelligence (SIGINT) Wireless Network Security
### Brad Williams · Chris Limson
GMU CYSE 640 Wireless Network Security  
Fall 2024 · Moinul Hossain, PhD  
SIGINT Project  

## Resources

For download or online with GMU's Campus-Wide License, MATLAB and Simulink https://matlab.mathworks.com  
Download details:  
matlab_R2024b_Windows.exe (220 MB; SHA256: 2a32ddff3186306f5ed6c1b2dc996ee0978b5990f623f6511a651728e3c269f3)

GNU Radio https://www.gnuradio.org  
On Ubuntu 22.04

```
sudo apt install gnuradio
```

## Notes
We will describe the basics of what SIGINT is and how Wireless Network Security applies to it, general methodologies, logistics and systems that are fundamental

And then areas that are potentially open for innovation, development and investigation. How signal analysis can still be written for MATLAB to include environmental or experimental simulations

Hardware on an assigned plane (consisting of special things like the ugly AWACS) picks up RF signals of a questionable nation state

Raw signal waveforms are recorded and sent via securely encrypted channel to ground base station, then maybe again to where more powerful servers can organize collected data, crunch numbers

Signal analysis tools like MATLAB, Simulink and GNU Radio identifies which ones are valid, what can be cleaned up or extracted from noise, based on properties, patterns or behaviors

When does decryption occur? Are these necessarily always network data, or might it be analog/voice

Info source -> encrypt -> encode -> modulation -> air -> antenna -> radio frequency receiver -> tune to the freq of interest -> digitize (convert analog signal from the air into samples)

Digitized samples can be processed in the same place as the receiver, or they can be forwarded to a data center for processing. Also known as the forwarding channel

Demodulation -> decode -> decrypt -> info

At the info source, voice is "digitized", "compressed (voice coding)" After this it follows the same "encrypt -> encode -> modulation"

HW challenge, no simulator, no research, etc.

20-30 research papers

Malicious access point detection of secure facility

Man-in-the-middle attacking radio signatures

Honeypot

## Documentation
(Placeholders)  
[CYSE640_BradChris_ProjectProposalPresentation.pdf](docs/CYSE640_BradChris_ProjectProposalPresentation.pdf)  
[CYSE640_BradChris_ProjectProposalReport.pdf](docs/CYSE640_BradChris_ProjectProposalReport.pdf)  
[CYSE640_BradChris_ProjectFinalPresentation.pdf](docs/CYSE640_BradChris_ProjectFinalPresentation.pdf)  
[CYSE640_BradChris_ProjectFinalReport.pdf](docs/CYSE640_BradChris_ProjectFinalReport.pdf)  

## Reference
[https://chrimson.github.io/SILENCER](https://chrimson.github.io/SILENCER)  

## License
[MIT](LICENSE)
