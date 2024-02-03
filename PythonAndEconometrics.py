#!/usr/bin/env python
# coding: utf-8

# # Python & Econometrics

# ## Import Libraries:

# ###### import numpy as np: NumPy is used for numerical operations, and the alias np is a common convention.

# In[1]:


import numpy as np


# ###### import statsmodels.api as sm: Statsmodels is a library for estimating and testing statistical models, and sm is a common alias.

# In[2]:


import statsmodels.api as sm


# ## Generate Sample Data:

# ###### np.random.seed(42): Sets the random seed for reproducibility.

# In[3]:


np.random.seed(42)


# ###### x = np.random.rand(100, 1): Generates a 1-dimensional array with 100 random values between 0 and 1.

# In[4]:


x = np.random.rand(100, 1)  # Independent variable


# ###### y = 2 * x + 1 + 0.1 * np.random.randn(100, 1): Creates the dependent variable with a linear relationship to x and adds some random noise.

# In[5]:


y = 2 * x + 1 + 0.1 * np.random.randn(100, 1)  # Dependent variable with noise


# ## Add Constant Term:

# ###### X = sm.add_constant(x): Adds a constant term (intercept) to the independent variable matrix.
# ###### This is necessary for the OLS model to estimate the intercept.

# In[6]:


X = sm.add_constant(x) # Add a constant term to the independent variable matrix


# ## Fit the OLS Model:

# ###### model = sm.OLS(y, X).fit(): Fits the OLS model to the data.

# In[7]:


model = sm.OLS(y, X).fit() # Fit the OLS model


# ## Print Model Summary:

# ###### print(model.summary()): Prints a summary of the OLS regression results.
# ###### The summary includes coefficients, standard errors, t-values, p-values, and R-squared.

# In[8]:


print(model.summary()) # Print the summary of the model

