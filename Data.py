import pandas as pd

class Data:
    def __init__(self, df: pd.DataFrame) -> None:
        self.df = df
        self.length = len(df)
        self.unpack = ', '.join(df.columns) + " = df.row(i)"
    

    def row(self, i: int) -> tuple:
        if i in self.df.index:
            return tuple([self.df.at[i, column] for column in self.df.columns if not column.startswith('_')])
        raise KeyError(f"index {i} is out of range for a Data object.")
    

    def __getattr__(self, attr):
        if hasattr(self.df, attr):
            return self.df.__getattr__(attr)
        raise AttributeError()
    
    
    def __len__(self) -> int:
        return self.length
    

    def __getitem__(self, key):
        return self.df[key]
