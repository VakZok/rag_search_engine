import argparse
import json


def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using keywords")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            # print the search query here
            print(f"Searching for: {args.query}")

            with open("data/movies.json") as file:
                movies_dict = json.load(file)

            results = []
            for i in range(len(movies_dict["movies"])):
                movie = movies_dict["movies"][i]
                if args.query in movie["title"]:
                    results.append(movie)

            for position, movie in enumerate(results[:5], start=1):
                if position >= len(results):
                    break
                print(f"{position}. {movie['title']}")

        case _:
            parser.print_help()


if __name__ == "__main__":
    main()
