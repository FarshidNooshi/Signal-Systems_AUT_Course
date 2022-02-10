clc
clear
close all

%% Phase one ==============================
[phase1sample,Fs]=audioread('phase1sample.wav');
% plot signal
figure
plot(phase1sample(1:250))
% fourier transform
figure
f_phase1sample = abs(fft(phase1sample));
plot(f_phase1sample)
% filter the noise
figure
b = 14000 ;
f_phase1sample = f_phase1sample .* [ones(b,1);zeros(length(f_phase1sample)-2*b,1);ones(b,1)];
plot(f_phase1sample)
% ifft and play signal
figure
denoised_signal = abs(ifft(f_phase1sample));
sound(denoised_signal,Fs);
audiowrite('denoised_signal.wav',denoised_signal,Fs);
plot(denoised_signal(1:250))