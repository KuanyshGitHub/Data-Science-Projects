---
title: "Data cleaning and initial analysis"
date: 2020-04-20
---
The purpose of this project is to train my __cleaning and analysis skills__ in python

In this project I'll clean and analyze the employee exit surveys from Department of Education, Training and Employment(DETE) and Technical and Further Education(TAFE) institute in Queensland, Australia.
Data survey can be found at [DETE](https://data.gov.au/dataset/ds-qld-fe96ff30-d157-4a81-851d-215f2a0fe26d/details?q=exit%20survey) and [TAFE](https://data.gov.au/dataset/ds-qld-89970a3b-182b-41ea-aea2-6f9f17b5907e/details?q=exit%20survey)

Note: The original encoding types of DETE_SURVEY is `UTF-8` where TAFE_SURVEY is `Windows-1252`. Since I prefer more UTF-8 encoding type, I have converted Windows-1252 to UTF-8

My end goal here to answer for following questions:
 - __Are employees who only worked for the institutes for a short period of time resigning due to some kind of dissatisfaction? What about employees who have been there longer?__
 - __Are younger employees resigning due to some kind of dissatisfaction? What about older employees?__

 ```python
     import pandas as pd
     import numpy as np
     import matplotlib.pyplot as plt

     dete_survey = pd.read_csv('dete_survey.csv')

     #Quick exploration of the data
     pd.options.display.max_columns = 150 # to avoid truncated output
     dete_survey.head()
 ```
