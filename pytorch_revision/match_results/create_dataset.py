import torch
from torch.utils.data import Dataset, DataLoader
from sklearn.model_selection import train_test_split

import pandas as pd

def get_datasets(data_path="cleaned_data.csv"):
    # load data
    df = pd.read_csv(data_path)

    # split features and targets
    x = df.drop(columns=["home_goals", "away_goals"]).to_numpy
    y = df[["home_goals", "away_goals"]].to_numpy

    # convert to pytorch tensors
    x = torch.tensor(x, dtype=torch.float32)
    y = torch.tensor(y, dtype=torch.float32)

    # split data
    x_train, x_test, y_train, y_test = train_test_split(
        x, y, test_size=0.2, random_seed=42
    )

    # create datasets
    train_dataset = FootballDataset(x_train, y_train)
    test_dataset = FootballDataset(x_test, y_test)
    
    return train_dataset, test_dataset

def gat_dataloaders(data_path="cleaned_data.csv", batch_size=64):
    # get datasets
    train_dataset, test_dataset = get_datasets(data_path=data_path)
    
    # create dataloaders
    train_dataloader = DataLoader(train_dataloader, batch_size=batch_size, shuffle=True)
    test_dataloader = DataLoader(test_dataloader, batch_size=batch_size, shuffle=False)
    
    return train_dataloader, test_dataloader

# dataset class
class FootballDataset(Dataset):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __len__(self):
        return len(self.x)
    
    def __getitem__(self, idx):
        return self.x[idx], self.y[idx]