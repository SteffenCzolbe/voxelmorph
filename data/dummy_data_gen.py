"""
Generates random data samples

The samples are of the size defined in the arguments (Default size as in the Papers)
Values are sampled uniformly from 0..1
"""
import argparse
import numpy as np
from tqdm import tqdm
import os

if __name__ == '__main__':

    parser = argparse.ArgumentParser()

    # data organization parameters
    parser.add_argument('datadir', help='directory to save the data in')
    parser.add_argument('--size', type=int, nargs='+', help='Dimensionality of the data (default: 160 192 224)')
    parser.add_argument('--sample_count', type=int, default=200, help='Amount of Samples to create (default: 200)')

    args = parser.parse_args()
    
    # prepare size
    size = args.size if args.size else [160, 192, 224]

    # prepare output folder
    os.makedirs(args.datadir, exist_ok=True)

    # create samples
    for i in tqdm(range(args.sample_count), desc='Creating Samples...'):
        a = np.random.uniform(size=size)
        np.savez(os.path.join(args.datadir, f'{i}.npz'), vol=a)
