import pandas as pd
import numpy as np

def apply_transform(series, code):
    try:
        if code == 1:
            return series
        elif code == 2:
            return series.diff()
        elif code == 3:
            return series.diff().diff()
        elif code == 4:
            return np.log(series)
        elif code == 5:
            return np.log(series).diff()
        elif code == 6:
            return np.log(series).diff().diff()
        elif code == 7:
            return series.pct_change().diff()
        else:
            return pd.Series([np.nan] * len(series), index=series.index)
    except Exception:
        return pd.Series([np.nan] * len(series), index=series.index)

def load_and_transform(fred_csv_path, transform_csv_path):
    df = pd.read_csv(fred_csv_path, index_col=0, parse_dates=True)
    tf = pd.read_csv(transform_csv_path)
    df.columns = df.columns.str.strip()
    tf['Category'] = tf['Category'].str.strip()

    output = pd.DataFrame(index=df.index)
    failed_cols = []

    for _, row in tf.iterrows():
        col = row['Category']
        code = row['Transformation']
        if col in df.columns:
            try:
                transformed = apply_transform(df[col], code)
                output[col] = transformed
            except Exception as e:
                failed_cols.append((col, str(e)))

    # Replace inf/-inf with NaN
    output = output.replace([np.inf, -np.inf], np.nan)

    # Drop all rows with any NaNs
    output.dropna(inplace=True)

    # Clip extremely large or small values to prevent PCA blow-up
    output = output.clip(lower=-1e10, upper=1e10)

    if failed_cols:
        print("The following columns failed to transform:")
        for col, err in failed_cols:
            print(f" - {col}: {err}")

    return output  
