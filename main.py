import random
import threading
import time
import json
import os
import traceback
import argparse

from configs import Configs
from generator_pub_sub import GeneratorPubSub
from utils import generate_field_freq, generate_operator_freq

def load_configs():
    parser = argparse.ArgumentParser(
        description='Generator de publicații și subscripții')

    parser.add_argument('--config-path', type=str, default='config.json', help='The path to the configuration JSoN file')
    args = parser.parse_args()

    return Configs(config_path=args.config_path)


def main(iteration):
    configs = load_configs()

    if configs.error:
        return

    generator = GeneratorPubSub(configs=configs)

    for thread in configs.threads:
        generator.generate(iteration, thread)


if __name__ == "__main__":
    for index in range(1, 50001):
        main(index)
