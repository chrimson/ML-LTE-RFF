% matlab -nodisplay -nodesktop -nosplash -r "run('LTE_RFF_Waveform_NN.m');exit;"

fprintf('Configure LTE Uplink RMC\n');
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

fprintf('Parameters, declaration\n\n');
num_samples = 50;
trunc_size = 2000;
waveforms = zeros(trunc_size, num_samples);
rff = zeros(trunc_size, num_samples);

%% Generate waveforms
for sample = 1:num_samples

    %% Init
    fprintf('Generate initial waveform %d\n', sample);
    [waveform_tmp, grid, cfg] = lteRMCULTool(cfg, in);

    Fs = cfg.SamplingRate;
    fprintf('Sample rate %d Hz\n', Fs);

    fprintf('Truncate waveform\n')
    if length(waveform_tmp) > trunc_size
        waveform_tmp = waveform_tmp(1:trunc_size);
    end

%% RFF
    fprintf('Apply RF Fingerprint\n')
    fingerprint_strength = 0.1;

    % Create a unique fingerprint pattern
    numberOfSamples = length(waveform_tmp);
    time = (0:numberOfSamples-1) / Fs;

    % Add a phase shift to simulate a fingerprint, for now randomly just so we
    % can generate many RFF waveforms
    phase_shift = 2*pi*rand();
    phase_modulation = fingerprint_strength * cos(2 * pi * 0.5 * time + phase_shift);

    %Frequency shift to simulate subltle RF variations
    freq_modulation = fingerprint_strength * cos(2 * pi * 0.2 * time);

    rff(:,sample) = cos(phase_modulation + freq_modulation);
    % Apply fingerprint to waveform
    fingerprinted_signal = waveform_tmp .* rff(:,sample);

    %Normalize
    waveform_tmp = fingerprinted_signal / max(abs(fingerprinted_signal));

%% Impairments
    fprintf('IQ imbalance\n');
    waveform_tmp = iqimbal(waveform_tmp, 8, (180/pi)*pi/5);

    fprintf('Phase noise\n');
    phaseNoise = comm.PhaseNoise('FrequencyOffset', [6144000 12288000], ...
        'Level', [-60 -80], ...
        'SampleRate', Fs);
    waveform_tmp = phaseNoise(waveform_tmp);

    fprintf('DC offset\n');
    waveform_tmp = waveform_tmp + 0.1 + 0.2i;

    fprintf('AWGN\n\n');
    waveform_tmp = awgn(waveform_tmp, 20, 'measured');
    waveform_real = real(waveform_tmp(:));
    waveforms(:,sample) = waveform_real;
end

fprintf('Generated dataset of %d waveforms with fingerprints\n\n', ...
    num_samples);


%% Train NN
fprintf('Train Neural Network with dataset\n');
net = feedforwardnet(5); % The number of layers
net.trainParam.epochs = 100; % Number of epochs
trained_net = train(net, waveforms', rff');

fprintf('Done\n');


%{

test_waveform = <create a singular waveform to test>
predicted = net(test_waveform)

%}