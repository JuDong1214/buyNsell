clear
close all

data = csvread('ETHYEAR.csv', 1, 2);
%data = csvread('apple stonks.csv', 1, 5);
closingPrice = data(:,1);
plot(closingPrice);
xlabel("Number of days after September 24");
ylabel("Dollars ($)");
hold on

x = 1;
y = 1;
movingAvgRange = 12;
n = movingAvgRange + 1;


while (n <= length(closingPrice))
   
    %averagePrice(n) = (closingPrice(n) + closingPrice(n-1) + closingPrice(n-2) + closingPrice(n-3))/4;
    averagePrice(n) = mean(closingPrice((n-movingAvgRange):n));

    if closingPrice(n) > averagePrice(n) && closingPrice(n-1) < averagePrice(n-1)
        plot(n, closingPrice(n), 'g o');
        bought(x) = closingPrice(n);
        x = x + 1;
       
    end
    if closingPrice(n) < averagePrice(n) && closingPrice(n-1) > averagePrice(n-1)
        plot(n, closingPrice(n), 'r o');
        sold(y) = closingPrice(n);
        y = y + 1;
       
    end
 
    n = n+1;
    plot(averagePrice, 'k--');
end
if length(sold) == length(bought)
    profits = sold(2:end) - bought(1:end - 1);
end
if length(sold) > length(bought)
    profits = sold(2:end) - bought(1:end);
end
totalProfits = sum(profits);
profitWithoutAlgorithm = closingPrice(end) - closingPrice(1);
disp(totalProfits);
disp(profitWithoutAlgorithm);
grid on

