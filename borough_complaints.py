import argparse
import pandas as pd
from datetime import datetime


def main():

    parser = argparse.ArgumentParser(description='Count complaints per borough for a given date range.')
    parser.add_argument('-i', '--input', required=True, help='Input CSV file')
    parser.add_argument('-s', '--start', required=True, help='Start date in MM/DD/YYYY format')
    parser.add_argument('-e', '--end', required=True, help='End date in MM/DD/YYYY format')
    parser.add_argument('-o', '--output', help='Optional output CSV file')
    args = parser.parse_args()
    
    df = pd.read_csv(args.input, header=None)
    df[1] = pd.to_datetime(df[1], format='%m/%d/%Y %I:%M:%S %p')
    start_date = pd.to_datetime(args.start, format='%m/%d/%Y')
    end_date = pd.to_datetime(args.end, format='%m/%d/%Y')
    filtered_df = df.loc[(df[1] >= start_date) & (df[1] <= end_date)]
    result_df = filtered_df.groupby([5, 25]).size().reset_index(name='count')

    
    result_df.columns = ['complaint type', 'borough', 'count']

    if args.output:
        result_df.to_csv(args.output, index=False)
    else:
        print(result_df.to_csv(index=False))

if __name__ == '__main__':
    main()
