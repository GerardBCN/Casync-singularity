import argparse
import subprocess


if __name__ == '__main__':

    # parser
    parser = argparse.ArgumentParser(description='Chunks and syncs squashfs images efficiently using Casync')
    parser.add_argument('-chunk', dest='chunk', action='store', help='img to chunk')
    parser.add_argument('-sync', dest='sync', action='store', help='.caibx to sync')
    parser.add_argument('-seed', dest='seed', action='store', help='image to use as seed')
    parser.add_argument('-new', dest='new', action='store', help='name of new image to create')
    args = parser.parse_args()
    args = vars(args)

    print(args)

    # chunk an image to be served
    if args["chunk"]:
        subprocess.call(["casync", "make", "app.caibx", args["chunk"]])

    # sync existing seed image using chunks from sync url
    elif args["sync"] and args["seed"] and args["new"]:
        subprocess.call(["casync", "-v", "extract", args["sync"], "--seed", args["seed"], args["new"]])

    else:
        # do nothing
        pass
