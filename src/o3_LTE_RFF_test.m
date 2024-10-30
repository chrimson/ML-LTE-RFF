%% Configure Tool
fprintf('Configure tool\n');
strength = 0.1 % Amplitude effect (0.1)
trunc = 5000 % Adjusted length of waveform for development (5000 for now)
dev = 0.05 % Deviation from fingerprint parameters (0.05 is +/-0.025)
rep = 50 % Adjustable repetitive factor (10-80 looks good)
rng(12417) % Random generator seed

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

%% RF Fingerprint
% Choose a set of parameters from ue_rff parms.asc
A = 7.392780e-03
B = 4.779907e-03
C = 3.828342e-03
D = 2.717704e-02
J = 3.091687e-03
K = 6.344656e-02

base = 1 - dev / 2;
rff = 1 + ...
    (base+rand*dev)*J*sin((base+rand*dev)*A*t + (base+rand*dev)*B) + ...
    (base+rand*dev)*K*cos((base+rand*dev)*C*t + (base+rand*dev)*D);

fid = fopen('target_rff.asc', 'w');
fprintf(fid, '%.4f\n', rff');
fclose(fid);

fprintf('\nDone\n');
