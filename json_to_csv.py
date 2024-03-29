import pandas as pd
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Convert data from JSON format to CSV.',
    )
    parser.add_argument(
        'json_file',
        type=str,
        help='The json file to convert.',
    )
    args = parser.parse_args()

    json_file = args.json_file
    csv_file = '{0}.csv'.format(json_file.split('.json')[0])

    df = pd.read_json(json_file, lines=True)
    df.to_csv(csv_file, index=False, encoding='utf-8')