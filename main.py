import pandas as pd

training_data = pd.read_csv('poker-hand-training-true.data', header=None)

testing_data = pd.read_csv('poker-hand-testing.data', header=None)

merge_data = pd.concat([training_data, testing_data])

merge_data.to_csv('poker-hand-data.csv', index=False, header=None)

shuffled_data = merge_data.sample(frac=1).reset_index(drop=True)

shuffled_data.to_csv('poker-hand-data-shuffled.csv', index=False, header=None)