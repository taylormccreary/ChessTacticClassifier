"""Uses the data in the csv of fens, moves and tactics
to create features that we use to train on"""
import pandas as pd

if __name__ == "__main__":
    df_data = pd.read_csv('..\\data\\training_data_unprocessed.csv')
    df_features = pd.DataFrame()
    df_features["tactic"] = df_data["Tactic"]
    print(df_features)
    