from pyOpenBCI import OpenBCICyton
from pylsl import StreamInlet, resolve_stream
from matplotlib import pyplot as plt
from matplotlib import animation


def get_data():
    streams = resolve_stream('type', 'EEG')
    Inlet = StreamInlet(streams[0])
    while True:
        yield Inlet.pull_sample()[0]
