# Sleep Analysis Project

## Overview

This project focuses on analyzing sleep patterns using data from the Physionet Sleep Accelerometer Dataset [1]. The aim was to extract meaningful insights from sleep data to aid in sleep research. See _sleep_analysis_report.pdf_ for detailed analysis.

## Prerequisites

Before running the code, ensure you have the following:

- Python 3.x
- Necessary Python libraries: Install them using the requirements.txt file provided in the repository. You can do this by running the command:

```bash
  pip install -r requirements.txt
```

## Data Acquisition

To run the code, you must first download the required dataset. Follow these steps:

1. Visit the Physionet Sleep Accelerometer Dataset at [Physionet](https://physionet.org/content/sleep-accel/1.0.0/labels/#files-panel).
2. Download the dataset.
3. Extract the contents of the .zip file.
4. Place the extracted data in the `data` folder of this project.
   - Ensure that the `data` folder structure remains unchanged.

## Project Structure

- **sleep_analysis_notebook.ipynb**: Jupyter notebook with detailed analysis.
- **utils.py**: Contains utility functions.
- **preprocessing.py**: Contains functions for data processing.
- **data/**: Folder to place the downloaded data.
- **sleep_analysis_report.pdf**: Project report.
- **requirements.txt**: Contains required dependencies.

## References

[1] Walch, O. (2019). Motion and heart rate from a wrist-worn wearable and labeled sleep from polysomnography (version 1.0.0). PhysioNet. https://doi.org/10.13026/hmhs-py35.

[2] Walch, O., Huang, Y., Forger, D., & Goldstein, C. (2019). Sleep stage prediction with raw acceleration and photoplethysmography heart rate data derived from a consumer wearable device, Sleep 42(12). https://doi.org/10.1093/sleep/zsz180

[3] Goldberger, A., Amaral, L., Glass, L., Hausdorff, J., Ivanov, P. C., Mark, R., ... & Stanley, H. E. (2000). PhysioBank, PhysioToolkit, and PhysioNet: Components of a new research resource for complex physiologic signals. Circulation [Online]. 101 (23), pp. e215–e220.
