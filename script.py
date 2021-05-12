from collections import OrderedDict
from pathlib import Path
from os import listdir
import json


gitaggregate_dated_files = [
    'activities',
    'activity_files',
    'file_size_bins',
    'file_size',
    'invalidxml',
    'nonstandardroots',
    'organisation_files',
    'publisher_has_org_file',
    'publishers_per_version',
    'publishers',
    'publishers_validation',
    'unique_identifiers',
    'validation',
    'versions',
]

gitaggregate_publisher_dated_files = [
    'activities',
    'activity_files',
    'file_size',
    'invalidxml',
    'most_recent_transaction_date',
    'nonstandardroots',
    'organisation_files',
    'publisher_unique_identifiers',
    'validation',
    'versions',
]

blacklist_gitaggregate_publisher_dated_files = [
    'activities_with_future_transactions',
]


def merge_json(output_path, paths):
    current = {}
    for path in paths:
        try:
            with open(path) as f:
                j = json.load(f)
        except FileNotFoundError:
            j = {}
        if str(path).endswith('activities_with_future_transactions.json'):
            j = {k: len(v) for k, v in j.items()}
        current.update(j)
    with open(output_path, 'w') as f:
        json.dump(OrderedDict(sorted(current.items())), f, indent=2)


paths = [
    Path('publishingstats', 'gitaggregate-dated'),
    Path('dashboard', 'gitaggregate-dated')]
output_root = Path('gitaggregate-dated')
output_root.mkdir(parents=True, exist_ok=True)
for file in gitaggregate_dated_files:
    gad_paths = [Path(path, file + '.json') for path in paths]
    output_path = Path(output_root, file + '.json')
    merge_json(output_path, gad_paths)

paths = [
    Path('publishingstats', 'gitaggregate-publisher-dated'),
    Path('dashboard', 'gitaggregate-publisher-dated')]
blacklist_paths = [
    Path('publishingstats-blacklist', 'gitaggregate-publisher-dated'),
    Path('dashboard-blacklist', 'gitaggregate-publisher-dated')]
publishers = sorted(set([
    publisher
    for path in paths
    for publisher in listdir(path)]))
for publisher in publishers:
    print(publisher)
    output_root = Path('gitaggregate-publisher-dated', publisher)
    output_root.mkdir(parents=True, exist_ok=True)
    for file in gitaggregate_publisher_dated_files:
        gapd_paths = [Path(path, publisher, file + '.json') for path in paths]
        output_path = Path(output_root, file + '.json')
        merge_json(output_path, gapd_paths)

    for file in blacklist_gitaggregate_publisher_dated_files:
        gapd_paths = [Path(path, publisher, file + '.json') for path in blacklist_paths]
        output_path = Path(output_root, file + '.json')
        merge_json(output_path, gapd_paths)
