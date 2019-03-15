data <- read.csv("Corvallis.csv", header=T, sep=";")

x = data[, 9]
temps = data[, 8] 

plot(x,
     temps,
     type="l",
     xlim=c(0, 22450),
     xlab="Days since May 1, 1952",
     ylab="Average Temperature (Degrees C)",
     main="Corvallis Temperature History 1952-2013")

x0 = 8.0214197
x1 = 0.00010694836
x2 = 4.2808907
x3 = 8.1868578
x4 = -0.79063079
x5 = -0.29536021

y = function(x){x0 +
    x1*x+
    x2*cos(2*pi*x/365.25) + 
    x3*sin(2*pi*x/365.25) +
    x4*cos(2*pi*x/365.25/10.7) + 
    x5*sin(2*pi*x/365.25/10.7)}
curve(y, 
      add=TRUE, 
      xlim=(c(0, 22450)),
      col='green',
      xlab="Days since May 1, 1952",
      ylab="Average Temperature (Degrees C)",
      lwd=2)

z = function(x){x0 +
    x1*x}
curve(z, 
      add=TRUE, 
      xlim=(c(0, 22450)),
      col='red',
      xlab="Days since May 1, 1952",
      ylab="Average Temperature (Degrees C)",
      lwd=5)
