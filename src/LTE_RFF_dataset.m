strength = 0.1; % Amplitude effect
trunc = 5000; % Adjusted length of waveform for development
dev = 0.06; % Deviation from fingerprint parameters
rep = 20; % Adjustable repetitive factor

num_wf = 4;
num_dev = 4;

rng(61223) % Random generator seed


%% Generating LTE Compliant Uplink RMC waveform
% Configuration
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
[waveform, grid, cfg] = lteRMCULTool(cfg, in);
wf_size = length(waveform);
t = 1 : wf_size;


%% RF Fingerprint
base = 1 - dev / 2;
for wf_iter = 1:num_wf
    A = rep*pi*rand/wf_size;
    B = rep*pi*rand/wf_size;
    C = rep*pi*rand/wf_size;
    D = rep*pi*rand/wf_size;
    M = rand() * strength;
    N = rand() * strength;
    
    m = strings(6, 1);
    for octet = 1:6
        octet_val = randi(256) - 1;
        m(octet) = dec2hex(octet_val, 2);
    end
    mac = sprintf('%s-%s-%s-%s-%s-%s', m);
    if ~exist(mac, 'dir')
        mkdir(mac);
    end
    
    for deviations = 1:num_dev
        rff = 1 + ...
            (base+rand*dev)*M*sin((base+rand*dev)*A*t + (base+rand*dev)*B) + ...
            (base+rand*dev)*N*cos((base+rand*dev)*C*t + (base+rand*dev)*D);
        plot(t, rff);
        hold on;
    
        waveform = waveform .* rff';
        
        max=-1;
        list = dir(mac);
        for i = 1:length(list)
            names = {list.name};
            num = str2double(cell2mat(names(i)));
            if ~isnan(num)
                if num > max
                    max = num;
                end
            end
        end
        
        fid = fopen(sprintf('%s/%04d', mac, max+1), 'w');
        fprintf(fid, '%.4f + %.4fi\n', [real(waveform(:)), imag(waveform(:))].');
        fclose(fid);
    end
end

%{
% Specify the sample rate of the waveform in Hz
Fs = cfg.SamplingRate;

%% Visualize
% Time Scope
timeScope = timescope('SampleRate', Fs, ...
    'TimeSpanOverrunAction', 'scroll', ...
    'TimeSpanSource', 'property', ...
    'TimeSpan', 9.7656e-07);

timeScope(waveform);
%timeScope(rff);
release(timeScope);

% Spectrum Analyzer
spectrum = spectrumAnalyzer('SampleRate', Fs);
spectrum(waveform);
release(spectrum);
%}
