import os.path

DATADIR = os.path.abspath(os.path.dirname(__file__))

DATAFILES = {
        'AOT': 'MOD04_3K.A2017001.1155.006.2017009173648.hdf',
        'PWV': 'MOD05_L2.A2017001.1155.006.2017009173340.hdf',
        'ozone': 'MOD07_L2.A2017001.1155.006.2017004142736.hdf'}

DATAFILES = {key: os.path.join(DATADIR, DATAFILES[key]) for key in DATAFILES}

EXTENT = dict(xmin=10, xmax=13, ymin=55, ymax=56)
