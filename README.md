# Fraud-agents-detection

We propose a two-stage detection model to detect fraud-agents in Online Microfinance.

The first stage focuses on agent detection from all borrowers, and the second stage conducting the final fraud-agent detection from the agents detected in the first stage.

## Usage

The first stage - Agent Detection Model
* Rule Based Agents Detection
  
  1. Remarks extract.py is used to extract a list of finance-related keyword from the borrowers’ address books.
  2. Remarks identify.py is used to find the agents (AG_1) by counting the number of remarks that contain any of the finance-related keywords for all the remarks on a single phone number.
  
* Machine Learning based Agents Detection
  1. model.py is used to detect the agents (AG_2) from normal-borrowers.

The second stage - Fraud-agent Detection Model
* Temporary Fraud-agents Detection
  1. model.py is used to detect expanded fraud-agents from agents (AG_1)
  
* Final Fraud-agents Detection
  1. model.py is used to detect final fraud-agents from agents (AG_2)


## Requirements
* numpy
* xgboost
* math




