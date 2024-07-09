clear

data = readmatrix("data\NFO3163P1D230529N01T230BEV-44 001-000000A-000001.csv");

data_fft = fft(data(:, 3));
data_fft = abs(data_fft);

subplot(2,1,1)
plot(data(:, 3))
subplot(2,1,2)
plot(data_fft)
ylim([0, 100])