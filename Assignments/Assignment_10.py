import argparse
import logging


parserTool = argparse.ArgumentParser()
parserTool.add_argument("number", help="This will give the sigma notation of the number")
args = parserTool.parse_args()

def sigmaFunction(number):
    logging.info("%s", number)
    total = 0
    for counter in range (0, number + 1, 1):
        total = total + counter
    logging.warning("The total is: %s", total)
    return total


print(sigmaFunction(int(args.number)))

    
