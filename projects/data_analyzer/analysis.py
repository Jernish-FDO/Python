import pandas as pd
import numpy as np

# Let's crunch some numbers, buddy!
def analyze_data():
    # Creating some random data
    data = {
        'Day': range(1, 8),
        'Study_Hours': [2, 3, 5, 4, 6, 8, 10],
        'Coffee_Cups': [1, 2, 2, 1, 3, 4, 5]
    }
    
    df = pd.DataFrame(data)
    
    print("--- 📊 Weekly Stats ---")
    print(df)
    
    print("\n--- 📈 Correlations ---")
    print(df.corr())
    
    print(f"\nAverage Study Hours: {df['Study_Hours'].mean():.2f}")

if __name__ == "__main__":
    analyze_data()
