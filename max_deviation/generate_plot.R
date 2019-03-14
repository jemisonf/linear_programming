xs <- c(1, 2, 3, 5, 7, 8, 10)
ys <- c(3, 5, 7, 11, 14, 15, 19)
y = function(x){1.7142857*x + 1.8571429}
plot(
  xs,
  ys,
  xlim=c(0, 11),
  ylim=c(0, 20),
  xlab="x",
  ylab="y",
  main="y = 1.7142857x + 1.8571429 and sample points"
)
curve(y, add=TRUE, xlim=(c(-2, 20)))
