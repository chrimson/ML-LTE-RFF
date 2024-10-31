%% Configure Tool
fprintf('Configure tool\n');
trunc = 5000 % Adjusted length of waveform for development (5000 for now)
dev = 0.05 % Deviation from fingerprint parameters (0.05 is +/-0.025)
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
rwf_len = length(waveform);
t = 1 : rwf_len;

%% RF Fingerprint
% Choose a set of parameters from ue_rwf_parms.asc
A = 1.478556e-03
B = 9.559815e-04
C = 7.656685e-04
D = 5.435408e-03
J = 7.729217e-03
K = 1.586164e-01

base = 1 - dev / 2;
rff = 1 + ...
    (base+rand*dev)*J*sin((base+rand*dev)*A*t + (base+rand*dev)*B) + ...
    (base+rand*dev)*K*cos((base+rand*dev)*C*t + (base+rand*dev)*D);

rwf = waveform .* rff';

fid = fopen('target_rwf.asc', 'w');
% fprintf(fid, '%.4f\n', rff');
fprintf(fid, '%.4f + %.4fj\n', [real(rwf(:)), imag(rwf(:))].');
fclose(fid);

fprintf('\nDone\n');
