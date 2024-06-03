import pandas as pd

class InterpolateHelper:
    def __init__(self, csv_path):
        self.data = pd.read_csv(csv_path)
    
    def interpolate(self, x):
        x_col = self.data['x']
        y_col = self.data['y']
        
        closest_index = (x_col - x).abs().idxmin()

        closest_x = x_col[closest_index]
        closest_y = y_col[closest_index]
        
        next_index = closest_index + 1
        if next_index >= len(x_col):
            return closest_y  # Return the closest y value if there are no more values
        
        next_x = x_col[next_index]
        next_y = y_col[next_index]
        
        # Perform linear interpolation
        interpolated_y = closest_y + (x - closest_x) * (next_y - closest_y) / (next_x - closest_x)
        
        return interpolated_y