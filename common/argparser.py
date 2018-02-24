# coding : utf-8
import argparse

app_name = ["xigua"]


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("app_name", choices=app_name,
                        help="The app you are playing")
    args = parser.parse_args()
    return args.app_name
