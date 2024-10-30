%% Configure Tool
fprintf('Configure tool\n');
strength = 0.25 % Amplitude effect (0.1)
trunc = 5000 % Adjusted length of waveform for development (5000 for now)
dev = 0.05 % Deviation from fingerprint parameters (0.05 is +/-0.025)
rep = 10 % Adjustable repetitive factor (10-80 looks good)
num_wf = 50
num_dev = 50
rng(61223) % Random generator seed
data = 'ue_rff_data'

%% Generating LTE Compliant Uplink RMC waveform
% Configuration
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

% Input bit source:
in = [1; 0; 0; 1];

% Generation
fprintf('Generation\n');
[waveform, grid, cfg] = lteRMCULTool(cfg, in);
waveform = waveform(1:trunc);
wf_len = length(waveform);
t = 1 : wf_len;

if ~exist(data, 'dir')
    mkdir(data);
end

%% RF Fingerprint
base = 1 - dev / 2;
for wf_iter = 1:num_wf
    A = rep*pi*rand/wf_len;
    B = rep*pi*rand/wf_len;
    C = rep*pi*rand/wf_len;
    D = rep*pi*rand/wf_len;
    J = rand * strength;
    K = rand * strength;
    
    m = strings(6, 1);
    for octet = 1:6
        octet_val = randi(256) - 1;
        m(octet) = dec2hex(octet_val, 2);
    end
    mac = sprintf('%s-%s-%s-%s-%s-%s', m);
    mac_path = sprintf('%s/%s', data, mac);
    if ~exist(mac_path, 'dir')
        mkdir(mac_path);
    end

    fprintf('\nWaveform %d, RFF %s\n', wf_iter, mac);
    
    for deviation = 1:num_dev
        fprintf('Deviation %d\n', deviation);
        rff = 1 + ...
            (base+rand*dev)*J*sin((base+rand*dev)*A*t + (base+rand*dev)*B) + ...
            (base+rand*dev)*K*cos((base+rand*dev)*C*t + (base+rand*dev)*D);
%        plot(t, rff);
%        hold on;

        wf = waveform .* rff';

        max=-1;
        list = dir(mac_path);
        for i = 1:length(list)
            names = {list.name};
            num = str2double(cell2mat(names(i)));
            if ~isnan(num)
                if num > max
                    max = num;
                end
            end
        end
        if max+1 == 0
            fid = fopen('ue_rff_parms.asc', 'a+');
            fprintf(fid, sprintf('%s %d %d %d %d %d %d\n', mac, A, B, C, D, J, K));
        end
        fid = fopen(sprintf('%s/%04d', mac_path, max+1), 'w');
%        fprintf(fid, '%.4f + %.4fi\n', [real(waveform(:)), imag(waveform(:))].');
%        fprintf(fid, '%.4f\n', rff');
        fprintf(fid, '%.4f + %.4fj\n', [real(wf(:)), imag(wf(:))].');
        fclose(fid);

    end
end

%{
%% Visualize
% Specify the sample rate of the waveform in Hz
Fs = cfg.SamplingRate;


% Time Scope
timeScope = timescope('SampleRate', Fs, ...
    'TimeSpanOverrunAction', 'scroll', ...
    'TimeSpanSource', 'property', ...
    'TimeSpan', 9.7656e-07);
timeScope(waveform);
release(timeScope);

% Spectrum Analyzer
spectrum = spectrumAnalyzer('SampleRate', Fs);
spectrum(waveform);
release(spectrum);


% Time Scope
timeScope_rff = timescope('SampleRate', Fs, ...
    'TimeSpanOverrunAction', 'scroll', ...
    'TimeSpanSource', 'property', ...
    'TimeSpan', 9.7656e-07);
timeScope_rff(wf);
release(timeScope_rff);

% Spectrum Analyzer
spectrum_rff = spectrumAnalyzer('SampleRate', Fs);
spectrum_rff(wf);
release(spectrum_rff);
%}

fprintf('\nDone\n');
