# README

## How to Run the Project

1. Simply execute **Run All** on `data_exploration.ipynb`. This will automatically load the dataframe containing the extracted features, already located in the `datasets/` directory.

2. Alternatively:
   - Run `feature_extraction.ipynb` to extract the features specifying the audio signals paths.
   - Update the **path** in **Section 2** of `data_exploration.ipynb` to point to the generated CSV file.


**Note**: Ensure the generated CSV file is correctly saved in the desired location to avoid loading errors.

**Note**: In the `submissions/` there are already the csv files used for the final submission of the project results

## Overview

This project focuses on the processing and analysis of audio signals. The workflow is divided across two Jupyter Notebook files: `feature_extraction.ipynb` and `data_exploration.ipynb`. Below, we describe the steps implemented in each notebook.



## Directory Structure

- **`notebooks/`**:
  - Contains the Jupyter Notebooks used in the project:
    - `feature_extraction.ipynb`: For feature extraction and preprocessing.
    - `data_exploration.ipynb`: For dataset exploration, feature selection, and model tuning.
    - `utils.py`: For utility functions for load audios.

- **`models/`**:
  - Contains pre-trained models that have already undergone grid search and hyperparameter tuning.

- **`datasets/`**:
  - Contains the dataset ready for feature selection and testing of the models.
  
- **`submissions/`**:
  - Contains the CSV files used for the final submissions of the project results.

## Steps in `feature_extraction.ipynb`

1. **Audio Signal Handling**:

   - Load the audio signals for processing.

2. **Signal Filtering**:

   - Apply filtering techniques to clean the audio data and remove noise.

3. **Signal Trimming**:

   - Trim or segment the audio signals to a fixed duration of 5 seconds.

4. **Feature Extraction**:

   - Extract features from the audio signals across different domains, including:
     - **Time Domain** features.
     - **Frequency Domain** features.
     - **MFCCs (Mel-Frequency Cepstral Coefficients)**.
     - **Chroma** features.
     - **Fundamental Frequency**.
     - **Amplitude Envelope**.

## Steps in `data_exploration.ipynb`

1. **Initial Dataset Exploration**:

   - Perform an initial exploration of the dataset, including basic statistics and visualizations.
   - Apply preprocessing steps to prepare the data for further analysis.

2. **Feature and Model Selection**:

   > **Important:** Starting from this section, you need to provide the CSV file containing the features extracted from `feature_extraction.ipynb`. The notebook `feature_extraction.ipynb` outputs a dataframe that is already concatenated with the original dataset. In the datasets/ directory there is the .csv file with all the feature extracted and ready for the feature selection of this point.

   - Use the dataframe resulting from the concatenation of the initial dataset and the extracted features.
   - Conduct feature selection to identify the most relevant attributes for the modeling process.

3. **Model Selection and Hyperparameter Tuning**:

   - Explore and select the best machine learning models for the task.
   - Perform hyperparameter tuning to optimize model performance.

## Purpose

The extracted and processed features, combined with the initial dataset, enable a robust pipeline for feature selection, model building, and optimization. This workflow facilitates the development of accurate and efficient predictive models.
