import argparse
import json
import string


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

            query_preprocessed = preprocess_text(args.query)
            results = []
            for i in range(len(movies_dict["movies"])):
                movie = movies_dict["movies"][i]
                title_preprocessed = preprocess_text(movie["title"])
                if check_all_words_present(query_preprocessed, title_preprocessed):
                    results.append(movie)

            for position, movie in enumerate(results[:5], start=1):
                print(f"{position}. {movie['title']}")

        case _:
            parser.print_help()


def preprocess_text(text: str) -> str:
    text = text.lower()
    text = remove_punctuation(text)
    return text

def check_all_words_present(query: str, corpus: str) -> bool:
    query_words = set(query.split())
    corpus_words = set(corpus.split())
    return query_words.issubset(corpus_words)

def remove_punctuation(text: str) -> str:
    return text.translate(str.maketrans("", "", string.punctuation))


if __name__ == "__main__":
    main()
