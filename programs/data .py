import pandas as pd


def load_data(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Data Loaded Successfully!")
        return df
    except Exception as e:
        print("Error loading file:", e)
        return None


def clean_data(df):
    df = df.dropna()  
    print("Data cleaned: Removed missing values.")
    return df


def process_data(df, column_name):
    if column_name in df.columns:
        avg_value = df[column_name].mean()
        print(f"Average {column_name}: {avg_value:.2f}")
        return avg_value
    else:
        print("Column not found!")
        return None


def save_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Processed data saved to {output_file}")


if __name__ == "__main__":
    file_path = "input_data.csv" 
    output_file = "processed_data.csv"
    column_name = "Sales"  

    df = load_data(file_path)
    if df is not None:
        df = clean_data(df)
        process_data(df, column_name)
        save_data(df, output_file)
