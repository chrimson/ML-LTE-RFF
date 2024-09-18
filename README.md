## SILENCER

### Signals Intelligence Wireless Network Security
### Brad Williams · Chris Limson
GMU CYSE 640 Wireless Network Security  
Fall 2024 · Moinul Hossain, PhD  
SIGINT Project  

## Resources

MATLAB  
Simulink  
GNU Radio  

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

## Documentation
For more detail,
[Proposal.pdf](Proposal.pdf)

## Reference
[https://chrimson.github.io/SILENCER](https://chrimson.github.io/SILENCER)  


## License
[MIT](LICENSE)
