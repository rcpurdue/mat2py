% ex7: Plots, MATLAB

n = randn(10000, 1);

histogram(x, 50, 'edgecolor', 'w');
xlabel('Bin');
ylabel('Value');
title('Histogram, Normal Distribution');
text(-3.5, 600, 'n=10,000, bins=50');
axis([-4, 4, 0, 800]);
grid('on');
shg();
