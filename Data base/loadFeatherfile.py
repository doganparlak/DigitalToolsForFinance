import feather
import os

researchPath = os.environ['RESEARCH_PATH']
featherPath = f'{researchPath}\\Data base\\test.feather'
df = feather.read_dataframe(featherPath)
print(df.head())
