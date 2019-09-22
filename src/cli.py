from typing import TextIO
import json
import sys
import click

from .http import entrypoint
from .stats import Results


@click.command()
@click.option("--requests", "-r", default=500, help="Number of Requests")
@click.option("--concurrency", "-c", default=1, help="Number of Concurrent Requests")
@click.option("--json-file", "-j", default=None, help="Path to JSON File")
@click.argument("url")
def main(requests, concurrency, json_file, url):
    print(".... Running!")
    print(f"Requests: {requests}")
    print(f"Concurrency: {concurrency}")
    print(f"JSON File: {json_file}")
    print(f"URL: {url}")
    output_file = None
    if json_file:
        try: 
            output_file = open(json_file, 'w')
        except:
            print(f"Unable to open file {json_file}")
            sys.exit(1)
    total_time, request_dict = entrypoint(url, requests, concurrency)
    results = Results(total_time, request_dict)
    display_results(results, output_file)


def display_results(results: Results, json_file: TextIO):
    if json_file:
        json.dump(
            {
                "successful_requests": results.successful_requests(),
                "slowest": results.slowest(),
                "fastest": results.fastest(),
                "total_time": results.total_time,
                "requests_per_minute": results.requests_per_minute(),
                "requests_per_second": results.requests_per_second(),
            },
            json_file,
        )
        json_file.close()
    else:
        print(".... Done!")
        print("--- Results ---")
        print(f"Slowest            \t{results.slowest()}s")
        print(f"Fastest            \t{results.fastest()}s")
        print(f"Average            \t{results.average_time()}s")
        print(f"Total Time         \t{results.total_time}s")
        print(f"Requests Per Min   \t{results.requests_per_min()}s")
        print(f"Requests Per Sec   \t{results.requests_per_sec()}s")