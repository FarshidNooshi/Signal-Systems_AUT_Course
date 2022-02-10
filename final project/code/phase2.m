clc
clear
close all

%% Phase two ==============================

[phase2sample,Fs]=audioread('phase2sample.wav');

% plot signal
figure
plot(phase2sample(1:250))

% fourier transform
figure
fourier_signal=abs(fft(phase2sample));
plot(fourier_signal(1:length(fourier_signal)/2+1))

% denoise
figure
b = 300;
fourier_signal(fourier_signal < b) = 0;
plot(fourier_signal)

% inverse fourier
figure
output_signal=abs(ifft([fourier_signal fourier_signal]));
plot(output_signal(1:250))

% save
audiowrite('second_phase_first_denoised_signal.wav',output_signal(2:length(output_signal)/2),Fs)

% fourier transform
figure
fourier_signal_2=abs(fft(output_signal));
plot(fourier_signal_2(2:length(fourier_signal_2)/2+1))

% under 1200 
figure
under_1200_audio = abs(ifft(equalizer_function(phase2sample,Fs,[10,10,10,10,10,10,0.1,0.1,0.1,0.1])));
plot(under_1200_audio);
audiowrite('under1200.wav',under_1200_audio,Fs)

% above 2000
figure
above_2000_audio = abs(ifft(equalizer_function(phase2sample,Fs,[0.1,0.1,0.1,0.1,10,10,10,10,10,10])));
plot(above_2000_audio);
audiowrite('above2000.wav',above_2000_audio,Fs)

%% Function:
function [fourier_signal,f] = equalizer_function(signal,Fs,amplify_cof)
    fourier_signal=pwelch(signal,[],[],[],Fs);
    f=1:Fs/2;
    for i = 1:length(fourier_signal)
        if(f(i) >= 20 && f(i) < 50)
            fourier_signal(i)=fourier_signal(i)*amplify_cof(1);
        elseif (f(i) >= 50 && f(i) < 100)
            fourier_signal(i)=fourier_signal(i)*amplify_cof(2);
        elseif (f(i) >= 100 && f(i) < 200)
            fourier_signal(i)=fourier_signal(i)*amplify_cof(3);
        elseif (f(i) >= 200 && f(i) < 500)
             fourier_signal(i)=fourier_signal(i)*amplify_cof(4);
         elseif (f(i) >= 500 && f(i) < 1000)
             fourier_signal(i)=fourier_signal(i)*amplify_cof(5);
        elseif (f(i) >= 1000 && f(i) < 2000)
            fourier_signal(i)=fourier_signal(i)*amplify_cof(6);
        elseif (f(i) >= 2000 && f(i) < 4000)
            fourier_signal(i)=fourier_signal(i)*amplify_cof(7);
         elseif (f(i) >= 4000 && f(i) < 8000)
             fourier_signal(i)=fourier_signal(i)*amplify_cof(8);
        elseif (f(i) >= 8000 && f(i) < 12000)
            fourier_signal(i)=fourier_signal(i)*amplify_cof(9);
         elseif (f(i) >= 12000 && f(i) < 20000)
            fourier_signal(i)=fourier_signal(i)*amplify_cof(10);
        end
    end
end