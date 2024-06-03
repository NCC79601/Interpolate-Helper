# Interpolate-Helper
Tiny tool useful for interpolating data

## Usage
```python
from interpolate_helper import Interpolator

interpolator = Interpolator('path_to_csv.csv')

print(interpolator.interpolate(x=100)) # desired x coord
```

CSV file should only include two columns: x and y. Example:
```csv
x,y
100,50
150,60
200,70
```