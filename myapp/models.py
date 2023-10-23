from django.db import models
from random import randint

class DataFrame(models.Model):
    title = models.CharField(max_length=255)
    categories = models.JSONField()
    data = models.JSONField()

    def add_data(self, category, values):
        if category in self.categories:
            self.data[category].extend(values)
        else:
            print(f"Error: {category} is not a valid category.")

    def to_dataframe(self):
        # Convert data to a pandas DataFrame
        return pd.DataFrame(self.data)
    

class DataFramesSet(models.Model):
    data_frames = models.ManyToManyField(DataFrame)

    def add_data_frame(self, data_frame):
        self.data_frames.add(data_frame)

    def get_data_frame(self, data_frame_title):
        return self.data_frames.filter(title=data_frame_title).first()

    def get_data_frames_dict(self):
        res = {}
        for data_frame in self.data_frames.all():
            res[data_frame.title] = data_frame.data
        return res
    
    def export_to_excel(self):
        for data_frame in self.data_frames.all():
            df = data_frame.to_dataframe()
            df.to_excel(f"{data_frame.title}.xlsx", index=False)
            

# Example usage:
# frame_categories = ['comunidad', 'primer nivel', 'segundo nivel', 'centros']

# # Create DataFrame instances
# frame_1 = DataFrame(title="Region1", categories=frame_categories, data={cat: [] for cat in frame_categories})
# frame_1.add_data("comunidad", [10, 10])
# frame_1.add_data("primer nivel", [10, 10])

# frame_2 = DataFrame(title="Region2", categories=frame_categories, data={cat: [] for cat in frame_categories})
# frame_2.add_data("comunidad", [20, 20])
# frame_2.add_data("primer nivel", [20, 20])

# # Create DataFramesSet instance
# my_data_frames_set = DataFramesSet.objects.create()
# my_data_frames_set.add_data_frame(frame_1)
# my_data_frames_set.add_data_frame(frame_2)

# # Export all data frames to Excel
# my_data_frames_set.export_to_excel()
