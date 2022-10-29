import feather
import os

researchPath = os.environ['RESEARCH_PATH']
featherPath = f'{researchPath}\\week5\\test.feather'
df = feather.read_dataframe(featherPath)
print(df.head())