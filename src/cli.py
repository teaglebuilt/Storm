from .http import entrypoint
import click


@click.command()
@click.option("--requests", "-r", default=500, help="Number of Requests")
@click.option("--concurrency", "-c", default=1, help="Number of Concurrent Requests")
@click.option("--json-file", "-j", default=None, help="Path to JSON File")
@click.argument("url")
def main(requests, concurrency, json_file, url):
    total_time = entrypoint(url, requests, concurrency)
    print(total_time)


if __name__ == "__main__":
    main()