import sys
import argparse
from common.logger import log
from core.configuration import Configuration


def init_args_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--env", help="set environment for app")
    args = parser.parse_args()

    if args.env is None:
        log.error("Error: Please enter your ENV")
        sys.exit(1)
    return args


def run():
    log.info("=== Singularity ===")
    args = init_args_parser()
    log.info(f'Current environment: {args.env}')
    config = Configuration(args.env)
    log.info("=== Spark project is running... ===")
    log.info("== Configurations ==")

    log.info(f'app_name: {config.app_name}')
    log.info(f'input_mongodb_uri: {config.input_mongodb_uri}')
    log.info(f'output_mongodb_uri: {config.output_mongodb_uri}')
    log.info(f'jars_dir: {config.jars_dir}')


if __name__ == '__main__':
    run()
