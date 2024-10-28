rng(61223)
rff_strength = 0.1;

%% Generating Uplink RMC waveform
% Uplink RMC configuration
cfg = struct('RC', 'A1-1', ...
    'NULRB', 100, ...
    'DuplexMode', 'FDD', ...
    'NCellID', 0, ...
    'RNTI', 1, ...
    'TotSubframes', 10, ...
    'Windowing', 0);

cfg.PUSCH.RVSeq = [0 2 3 1];
cfg = lteRMCUL(cfg);

% input bit source:
in = [1; 0; 0; 1];

% Generation
[waveform, grid, cfg] = lteRMCULTool(cfg, in);
wf_size = length(waveform);


%% RFF
t = 1 : wf_size;
A = 100*pi*rand()/wf_size;
B = 100*pi*rand()/wf_size;
C = 100*pi*rand()/wf_size;
D = 100*pi*rand()/wf_size;
M = rand() * rff_strength;
N = rand() * rff_strength;
for i = 1:10
    f = 1 + (0.95+rand*.1)*M*sin((0.95+rand*.1)*A*t + (0.95+rand*.1)*B) + ...
        (0.95+rand*.1)*N*cos((0.95+rand*.1)*C*t + (0.95+rand*.1)*D);
    plot(t, f);
    hold on;
end
rff = f';
waveform = waveform .* rff;

m = strings(6, 1);
for i = 1:6
    elm = randi(256) - 1;
    m(i) = dec2hex(elm, 2);
end
mac = sprintf('%s-%s-%s-%s-%s-%s', m);
if ~exist(mac, 'dir')
    mkdir(mac);
end


max=0;
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
