%% Configure Tool
function [] = s1_LTE_RWF_dataset(rep, str)

    fprintf('Configure tool\n');
    trunc    = 5000          % Adjusted length of waveform for development (5000 for now)
    dev      = 0.05          % Deviation from fingerprint parameters (0.05 is +/-0.025)
    num_rwf  = 50            % Number of RFF Waveforms (RWF)
    num_var  = 50            % Number of Variants for each RWF

    data = sprintf('%dx%d_ue_rwf_data', rep, str)  % Dataset directory
    rng(61223)               % Random generator seed

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

    if ~exist(data, 'dir')
        mkdir(data);
    end

    %% RFF Waveforms (RWF)
    % So the deviation (limited by dev=0.05) multiplicative factor would be
    % between 0.95 and 1.05
    base = 1 - dev / 2;
    t = 1 : trunc;
    for rwf_iter = 1:num_rwf
        A = rep*pi*rand/trunc;
        B = rep*pi*rand/trunc;
        C = rep*pi*rand/trunc;
        D = rep*pi*rand/trunc;
        J = rand * str/100;
        K = rand * str/100;

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

        fprintf('\nRFF Waveform %d, MAC %s\n', rwf_iter, mac);
        for variant = 1:num_var
            fprintf('Variant %d\n', variant);
            rff = 1 + ...
                (base+rand*dev)*J*sin((base+rand*dev)*A*t + (base+rand*dev)*B) + ...
                (base+rand*dev)*K*cos((base+rand*dev)*C*t + (base+rand*dev)*D);
    %        plot(t, rff);
    %        title('RFFs without Waveforms');
    %        hold on;

            [waveform, grid, cfg] = lteRMCULTool(cfg, in);
            waveform = waveform(1:trunc);

            rwf = waveform .* rff';

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
                fid = fopen(sprintf('%dx%d_ue_rwf_parm.asc', rep, str), 'a+');
                fprintf(fid, sprintf('%s %d,%d,%d,%d,%d,%d\n', mac, A, B, C, D, J, K));
            end
            fid = fopen(sprintf('%s/%04d', mac_path, max+1), 'w');
    %        fprintf(fid, '%.4f + %.4fi\n', [real(waveform(:)), imag(waveform(:))].');
    %        fprintf(fid, '%.4f\n', rff');
            fprintf(fid, '%.4f + %.4fj\n', [real(rwf(:)), imag(rwf(:))].');
            fclose(fid);

        end
    end

    %{
    %% Visualize
    % Specify the sample rate of the waveform in Hz
    Fs = cfg.SamplingRate;


    % Time Scope
    timeScope = timescope('Title', 'Last waveform without RFF', ...
        'Position', [10 550 500 500], ...
        'SampleRate', Fs, ...
        'TimeSpanOverrunAction', 'scroll', ...
        'TimeSpanSource', 'property', ...
        'TimeSpan', 9.7656e-07);
    timeScope(waveform);
    release(timeScope);

    % Spectrum Analyzer
    spectrum = spectrumAnalyzer('Title', 'Last spectrum without RFF', ...
        'Position', [520 550 500 500], ...
        'SampleRate', Fs);
    spectrum(waveform);
    release(spectrum);


    % Time Scope
    timeScope_rwf = timescope('Title', 'Last waveform with RFF', ...
        'Position', [10 10 500 500], ...
        'SampleRate', Fs, ...
        'TimeSpanOverrunAction', 'scroll', ...
        'TimeSpanSource', 'property', ...
        'TimeSpan', 9.7656e-07);
    timeScope_rwf(rwf);
    release(timeScope_rwf);

    % Spectrum Analyzer
    spectrum_rwf = spectrumAnalyzer('Title', 'Last spectrum with RFF', ...
        'Position', [520 10 500 500], ...
        'SampleRate', Fs);
    spectrum_rwf(rwf);
    release(spectrum_rwf);
    %}

    fprintf('\nDone\n');

end
