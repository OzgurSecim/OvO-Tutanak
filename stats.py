from utils.stats import StatsCalculator


if __name__ == '__main__':
    calculator = StatsCalculator(load_csv=True)

    calculator(simple=True)