%% Configure Tool
function [] = s3_LTE_RWF_test(rep, str, A, B, C, D, J, K)

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
    % Choosing a set of parameters from ue_rwf_parms.asc has now been
    % parameterized with CLI arguments

    % So the deviation (limited by dev=0.05) multiplicative factor would be
    % between 0.975 and 1.025
    base = 1 - dev / 2;
    rff = 1 + ...
        (base+rand*dev)*J*sin((base+rand*dev)*A*t + (base+rand*dev)*B) + ...
        (base+rand*dev)*K*cos((base+rand*dev)*C*t + (base+rand*dev)*D);

    rwf = waveform .* rff';

    fid = fopen(sprintf('%dx%d_target_rwf.asc', rep, str), 'w');
    % fprintf(fid, '%.4f\n', rff');
    fprintf(fid, '%.4f + %.4fj\n', [real(rwf(:)), imag(rwf(:))].');
    fclose(fid);
    
    fprintf('\nDone\n');

end
