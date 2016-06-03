import sys
import pandas as pd

def main():
	filename = sys.argv[1]
	year = sys.argv[2]
	factor = sys.argv[3]
	
        filename = 'survey.csv'
       # year = '1982'
       # factor = 'sex'
year = int(year)

print (filename,year,factor)

survey_d f= pd.read_csv(filename)

sub_year = survey_df # year
grouping_df = sub_year.groupby(factor)['weight']
mean_by_group = grouping_df.mean()
	

mergeinner.groupby('sex','weight').count()

print ('hello')

if__name__ == "__main__"

main()


