import pandas as pd

print("This is me Ghulam Qadir")
# Creating a simple DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [24, 27, 22],
    'City': ['New York', 'Los Angeles', 'Chicago']
}

df = pd.DataFrame(data)

# Displaying the DataFrame
print(df.describe())