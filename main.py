import argparse

from configs import Configs
from generator_pub_sub import GeneratorPubSub

def load_configs():
    parser = argparse.ArgumentParser(
        description='Generator de publicații și subscripții')

    parser.add_argument('--config-path', type=str, default='config.json', help='The path to the configuration JSON file')
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
    for index in range(1, 10001):
        main(index)
