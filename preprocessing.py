import numpy as np
import pandas as pd

def process_steps(df):
    # convert timestamps to hourly bins
    df['timestamp'] = df['timestamp'] / 3600
    df['hour_bin'] = np.floor(df['timestamp'])

    # group by hourly bins and sum the step counts in each bin
    res_df = df.groupby('hour_bin')['steps'].sum().reset_index()
    
    return res_df

def process_heart_rate(df):
    # convert timestamps to bins of 30 seconds
    df.loc[:, 'timestamp'] = np.floor(df['timestamp'] / 30)

    # calculate mean and standard deviation of heart rate for each bin
    res_df = df.groupby('timestamp').agg({'heartrate': ['mean', 'std']}).reset_index()

    # flatten the multi-level column names
    res_df.columns = ['timestamp', 'heartrate', 'heartrate_std']

    # convert timestamp back to its original scale
    res_df['timestamp'] = res_df['timestamp'] * 30

    return res_df

def process_motion(df):
    # convert timestamp to 30-second epochs
    df.loc[:, 'timestamp'] = np.floor(df['timestamp'] / 30)

    df_processed = df.copy()

    # calculate the magnitude of acceleration
    df_processed['magnitude'] = (df_processed['x']**2 + df_processed['y']**2 + df_processed['z']**2)**0.5
    
    # group by 'timestamp' and calculate mean and std
    grouped = df_processed.groupby('timestamp').agg({'x': ['mean', 'std'], 
                                                     'y': ['mean', 'std'], 
                                                     'z': ['mean', 'std'], 
                                                     'magnitude': ['mean', 'std']}).reset_index()

    # flatten the multi-level column names
    grouped.columns = ['timestamp', 'x_mean', 'x_std', 'y_mean', 'y_std', 'z_mean', 'z_std', 'magnitude', 'magnitude_std']
    
    # convert timestamp back to its original scale
    grouped['timestamp'] = grouped['timestamp'] * 30
    
    return grouped



def measure_sleep(df, start=0, end=0):
    # filter the dataframe for rows where the label is 1-5, representing sleep
    filtered_df = df[(df['label'] == 1) | (df['label'] == 2) | (df['label'] == 3) | (df['label'] == 5)]

    # convert the start and end to seconds
    start_in_secs = start * 3600
    end_in_secs = end * 3600
    
    # filter the dataframe for rows falling into the start and end range
    if start != 0 or end != 0:
        filtered_df = filtered_df[(filtered_df['timestamp'] >= start_in_secs) & (filtered_df['timestamp'] <= end_in_secs)]

    # return the number of rows in the filtered dataframe
    return len(filtered_df)

def measure_deep_sleep(df, start=0, end=0):
    # filter the dataframe for rows where the label is 3 - N3
    filtered_df = df[(df['label'] == 3)]

    # convert the start and end to seconds
    start_in_secs = start * 3600
    end_in_secs = end * 3600
    
    # filter the dataframe for rows falling into the start and end range
    if start != 0 or end != 0:
        filtered_df = filtered_df[(filtered_df['timestamp'] >= start_in_secs) & (filtered_df['timestamp'] <= end_in_secs)]

    # return the number of rows in the filtered dataframe
    return len(filtered_df)

def steps_count(df, start=0, end=0):
    # filter the dataframe for rows falling into the start and end range
    if start != 0 or end != 0:
        filtered_df = df[(df['hour_bin'] >= start) & (df['hour_bin'] <= end)]
        # return the number of rows in the filtered dataframe
        return filtered_df['steps'].sum()
    else:
        return df['steps'].sum()


def count_awakenings(df):
    if df.empty:
        return 0 

    wake_up_counts = []
    previous_stage = df.iloc[0]['label']
    
    # iterate over rows seraching for a change in sleep to wake state
    for _, row in df.iterrows():
        current_stage = row['label']
        if previous_stage in [1, 2, 3, 5] and current_stage == 0:
            wake_up_counts.append(1)
        # if the wake continues add 1 to the duration of it
        if previous_stage == 0 and current_stage == 0 and len(wake_up_counts) > 0:
            wake_up_counts[len(wake_up_counts)-1] += 1
        previous_stage = current_stage

    # count the awakening lasting more than 8 periods (4 mins)
    count = 0
    for i in wake_up_counts:
        if i >= 8:
            count += 1

    return count
