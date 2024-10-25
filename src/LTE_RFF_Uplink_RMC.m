% Generated by MATLAB(R) 24.2 (R2024b) and LTE Toolbox 24.2 (R2024b).
% matlab -nodisplay -nodesktop -nosplash -r "run('LTE_RFF_Uplink_RMC.m');exit;"

%% Generating Uplink RMC waveform
fprintf('Uplink RMC configuration\n');
cfg = struct('RC', 'A1-1', ...
    'NULRB', 100, ...
    'DuplexMode', 'FDD', ...
    'NCellID', 0, ...
    'RNTI', 1, ...
    'TotSubframes', 10, ...
    'Windowing', 0);

cfg.PUSCH.RVSeq = [0 2 3 1];
cfg = lteRMCUL(cfg);

fprintf('Input bit source\n');
in = [1; 0; 0; 1];

fprintf('Generation\n');
[waveform, grid, cfg] = lteRMCULTool(cfg, in);

Fs = cfg.SamplingRate;
fprintf('Sample rate %f Hz\n', Fs);


fprintf('Truncate waveform\n')
if length(waveform) > 2000
    waveform = waveform(1:2000);
end


fprintf('Add RF Fingerprint\n')
fingerprint_strength = 0.1;

% Create a unique fingerprint patter
numberOfSamples = length(waveform);
time = (0:numberOfSamples-1) / Fs;

% Add a phase shift to simulate a fingerprint
phase_shift = 2*pi*0.5;
% phase_shift = 2*pi*rand();  % Since we don't want random fingerprints for now
phase_modulation = fingerprint_strength * cos(2 * pi * 0.5 * time + phase_shift);

%Frequency shift to simulate subltle RF variations
freq_modulation = fingerprint_strength * cos(2 * pi * 0.2 * time);

% Apply fingerprint to waveform
fingerprinted_signal = waveform .* cos(phase_modulation + freq_modulation);

%Normalize
waveform = fingerprinted_signal / max(abs(fingerprinted_signal));


%% Impairments
fprintf('IQ imbalance\n');
waveform = iqimbal(waveform, 8, (180/pi)*pi/5);

fprintf('Phase noise\n');
phaseNoise = comm.PhaseNoise('FrequencyOffset', [6144000 12288000], ...
    'Level', [-60 -80], ...
    'SampleRate', Fs);
waveform = phaseNoise(waveform);

fprintf('DC offset\n');
waveform = waveform + 0.1 + 0.2i;

fprintf('AWGN\n');
waveform = awgn(waveform, 20, 'measured');

fprintf('Exporting\n');
fid = fopen('LTE_RFF_Uplink_RMC_waveform_data.ascii', 'w');
fprintf(fid, '%.4f + %.4fi\n', [real(waveform(:)), imag(waveform(:))].');
fclose(fid);

fprintf('Done\n');