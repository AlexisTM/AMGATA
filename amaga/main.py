import argparse

from article_generator import ArticleGeneratorAI21, ArticleGeneratorOpenAI


def main(company, model, subject, refute_subject=False):
    if company == "ai21":
        ag = ArticleGeneratorAI21()

    elif company == "openai":
        ag = ArticleGeneratorOpenAI()

    print(ag.generate_article(model, subject, refute_subject))


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script to display stock ticker price on a Inky pHAT display"
    )
    parser.add_argument(
        "--company",
        "-c",
        type=str,
        help="Company",
        choices=["openai", "ai21"],
        default="openai",
    )
    parser.add_argument(
        "--model",
        "-m",
        type=str,
        help="Model",
    )
    parser.add_argument(
        "--subject",
        "-s",
        type=str,
        help="Subject to generate an article about",
    )
    parser.add_argument(
        "--refute-subject",
        "-r",
        action="store_true",
        help="If True, the article will try refute the 'subject' instead of confirming it",
    )

    args = parser.parse_args()

    main(**vars(args))
