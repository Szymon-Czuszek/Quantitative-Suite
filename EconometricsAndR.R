# Generate sample data
set.seed(42)
x <- runif(100)  # Independent variable
y <- 2 * x + 1 + 0.1 * rnorm(100)  # Dependent variable with noise

# Add a constant term to the independent variable matrix
X <- cbind(1, x)

# Fit the OLS model
model <- lm(y ~ X)

# Print model summary
summary(model)
