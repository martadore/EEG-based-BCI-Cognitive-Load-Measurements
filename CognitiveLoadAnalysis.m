clc
close all
clear all

%% Init
% Sampling Frequency
Fs = 125;

% Band Def
Delta = [0 4];
Theta = [4 8];
Alpha = [8 13];
Beta = [13 30];
Gamma = [31 60];


%% Import Preprocessed data
d1 = xlsread("rest1_data.csv"); % pre resting data cleaned
d2 = xlsread("rest2_data.csv"); % post resting data cleaned
d3 = xlsread("easy_data.csv"); % Easy task data cleaned
d4 = xlsread("hard_data.csv"); % Hard task data cleaned

disp("data import complete")
%% Further Preprocessing
% Equalize Data length
x_rest1 = d1((end-300000+1:end),:);
x_rest2 = d2;                           % Less than 300000 samples hence kept as it is. 
x_easy = d3((end-300000+1:end),:);
x_hard = d4((end-300000+1:end),:);


% Remove Interpolated Channels
include = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,18,19];

x_rest1 = x_rest1(:,include);
x_rest2 = x_rest2(:,include);
x_easy = x_easy(:,include);
x_hard = x_hard(:,include);
%% Plot Data
figure(1)
subplot(4,1,1)
plot(x_rest1)
title("Recorded Time Series")
ylabel("Pre Rest")

subplot(4,1,2)
plot(x_rest2)
ylabel("Post Rest")

subplot(4,1,3)
plot(x_easy)
ylabel("Easy Task")

subplot(4,1,4)
plot(x_hard)
ylabel("Hard Task")
xlabel("Time")


%% Calculate Event Averaged Bandpowers
% idx = [1,2,3,4,5,6,7,9,10,11,12,14];
% for i = idx
for i = 1:16
    % Rest 1 Cognitive Load
    pdelta(i,1) = bandpower(x_rest1(:,i),Fs,Delta);
    ptheta(i,1) = bandpower(x_rest1(:,i),Fs,Theta);
    palpha(i,1) = bandpower(x_rest1(:,i),Fs,Alpha);
    pbeta(i,1) = bandpower(x_rest1(:,i),Fs,Beta);
    pgamma(i,1) = bandpower(x_rest1(:,i),Fs,Gamma);

    % Low Cognitive Load
    pdelta(i,2) = bandpower(x_easy(:,i),Fs,Delta);
    ptheta(i,2) = bandpower(x_easy(:,i),Fs,Theta);
    palpha(i,2) = bandpower(x_easy(:,i),Fs,Alpha);
    pbeta(i,2) = bandpower(x_easy(:,i),Fs,Beta);
    pgamma(i,2) = bandpower(x_easy(:,i),Fs,Gamma);


    % High Cognitive Load
    pdelta(i,3) = bandpower(x_hard(:,i),Fs,Delta);
    ptheta(i,3) = bandpower(x_hard(:,i),Fs,Theta);
    palpha(i,3) = bandpower(x_hard(:,i),Fs,Alpha);
    pbeta(i,3) = bandpower(x_hard(:,i),Fs,Beta);
    pgamma(i,3) = bandpower(x_hard(:,i),Fs,Gamma);


    % Rest 2 Congitive Load
    pdelta(i,4) = bandpower(x_rest2(:,i),Fs,Delta);
    ptheta(i,4) = bandpower(x_rest2(:,i),Fs,Theta);
    palpha(i,4) = bandpower(x_rest2(:,i),Fs,Alpha);
    pbeta(i,4) = bandpower(x_rest2(:,i),Fs,Beta);
    pgamma(i,4) = bandpower(x_rest2(:,i),Fs,Gamma);
end

%% Visualize the Spectrum

figure(2)
subplot(2,3,1)
plot(pdelta')
xlabel("Session Type")
ylabel("Spectral Power")
title("Delta")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})

subplot(2,3,2)
plot(ptheta')
xlabel("Session Type")
ylabel("Spectral Power")
title("Theta")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})

subplot(2,3,3)
plot(palpha')
xlabel("Session Type")
ylabel("Spectral Power")
title("Alpha")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})

subplot(2,3,4)
plot(pbeta')
xlabel("Session Type")
ylabel("Spectral Power")
title("Beta")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})

subplot(2,3,5)
plot(pgamma')
xlabel("Session Type")
ylabel("Spectral Power")
title("Gamma")
legend("F7","Fp1","Fp2","F8","F3","Fz","F4","C3","P8","P7","Pz","P4","T3","P3","C4","T4")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})

%% All Frontal Theta vs Pariental Alpha differences

figure(3)
subplot(1,2,1)
plot(ptheta(1:7,:)')
xlabel("Session Type")
ylabel("Spectral Power")
title("Frontal Theta")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})
legend("F7","Fp1","Fp2","F8","F3","Fz","F4")

subplot(1,2,2)
plot(pdelta([9,10,11,12,14],:)')
xlabel("Session Type")
ylabel("Spectral Power")
title("Pariental Alpha")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})
legend("P8","P7","Pz","P4","P3")
%% Calculate Cognitive load

% ERD/ERS   
for i = 1:16  
   Desync_index(i,:) = [100*(abs(bandpower(x_rest1(:,i),Fs,[0 50])-bandpower(x_easy(:,i),Fs,[0 50]))/bandpower(x_rest1(:,i),Fs,[0 50])), 100*(abs(bandpower(x_rest1(:,i),Fs,[0 50])-bandpower(x_hard(:,i),Fs,[0 50]))/bandpower(x_rest1(:,i),Fs,[0 50]))];
end

% TAR
for i = 1:4
%     disp(i)
%     disp(ptheta(5,i))
%     disp(ptheta(7,i))
%     disp(palpha(9,i))
%     disp(palpha(10,i))
%     disp(" ")
    TAR(i,1) = (ptheta(5,i) + ptheta(7,i))/(palpha(9,i)+palpha(10,i));
end


figure(4)
subplot(2,1,1)
y = [Desync_index(:,1) Desync_index(:,2)];
bar(y)
xlabel("Electrode")
ylabel("Cognitive Load")
title("ERD/ERS based Cognitive Load")
xticks([1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16])
xticklabels({"F7","Fp1","Fp2","F8","F3","Fz","F4","C3","P8","P7","Pz","P4","T3","P3","C4","T4"})


subplot(2,1,2)
bar(TAR)
xlabel("Session Type")
ylabel("Cognitive Load")
title("TAR based Cognitive Load")
xticks([1 2 3 4])
xticklabels({"Rest1","Task1","Task2","Rest2"})
