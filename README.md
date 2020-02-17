# stackoverflow_research
Research of Stack Overflow 2019 survey data to determine characteristics and skills of Data Scientists.

### Table of Contents

1. [Installation](#installation)
2. [Project Motivation](#motivation)
3. [File Descriptions](#files)
4. [Results](#results)
5. [Licensing, Authors, and Acknowledgements](#licensing)


## Installation <a name="installation"></a>

The code was written using the Anaconda distribution of Python and should run without issues using Python 3.*.

## Project Motivation<a name="motivation"></a>

Data from Stack Overflow from the year 2019 was used to help answer:

1. What are some defining characteristics of a Data Scientists/Machine Learning Specialists?
2. What type(s) of technologies do Data Scientists/Machine Learning Specialists use?
3. Can we identify if someone classifies themselves as a Data Scientists/Machine Learning Specialists based 
on a subset of answers from the Stack Overflow survey?

## File Descriptions <a name="files"></a>

There are two notebooks that showcase the worked related to the questions above.  Each of the notebooks are 
exploratory in searching through the data pertaining to the questions showcased in the project motivation section. Markdown cells 
were used to assist in walking through the thought process for individual steps.

* research.ipynb
* ds_detector.ipynb
* charts.xlsx (charts used in the blog post)

Note: in order to replicate the results, you will need to create a directory named "2019" in the same directory the notebooks are located in.  Within this directory, you need to place the 2019 survey results and schema found [here](https://insights.stackoverflow.com/survey).  The file names is "survey_results_public.csv" and "survey_results_schema.csv"

## Results<a name="results"></a>

The main findings of the code can be found at the post available [here](https://medium.com/@scott.lilleboe/can-you-become-a-data-scientist-d0b06611dbeb).

## Licensing, Authors, Acknowledgements<a name="licensing"></a>

Credit must be given to Stack Overflow for the data.  You can find the Licensing for the data and other descriptive 
information [here](https://insights.stackoverflow.com/survey).  Credit should also be given to Udacity for creating 
the [Data Science](https://www.udacity.com/course/data-scientist-nanodegree--nd025) Nanodegree that this project is 
part of.

