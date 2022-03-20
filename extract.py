"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    # TODO: Load NEO data from the given CSV file.

    #initializing a neo collection list

    neo_collection = []

    with open(neo_csv_path) as neo_file:
        all_neos = csv.DictReader(neo_file)
        for each_neo in all_neos:
            #if each_neo['name'] == 'Cerberus':
                #print(each_neo)
            neo_collection.append(NearEarthObject(**each_neo))
    return neo_collection


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param cad_json_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.

    #initializing a close approach list

    approach_collection = []

    with open(cad_json_path) as approach_file:
        all_approaches = json.load(approach_file)
        all_approaches_headers = all_approaches['fields']
        all_approaches_counts = int(all_approaches['count'])
        all_approaches_detail = all_approaches['data']

        for count in range(all_approaches_counts):
            approach_dict = {}
            for each_detail in range(11):
                approach_dict[all_approaches_headers[each_detail]] = all_approaches_detail[count][each_detail]
            #print(approach_dict)
            approach_collection.append(CloseApproach(**approach_dict))

    #print(approach_collection)
    return approach_collection

