from .http import entrypoint
from .stats import Results
import click


@click.command()
@click.option("--requests", "-r", default=500, help="Number of Requests")
@click.option("--concurrency", "-c", default=1, help="Number of Concurrent Requests")
@click.option("--json-file", "-j", default=None, help="Path to JSON File")
@click.argument("url")
def main(requests, concurrency, json_file, url):
    print(f"Requests: {requests}")
    print(f"Concurrency: {concurrency}")
    print(f"JSON File: {json_file}")
    print(f"URL: {url}")
    total_time, request_dict = entrypoint(url, requests, concurrency)
    print(request_dict)
    results = Results(total_time, request_dict)


# def display_results(results):
#      # Print to screen
#         print(".... Done!")
#         print("--- Results ---")
#         print(f"Slowest            \t{results.slowest()}s")
#         print(f"Fastest            \t{results.fastest()}s")