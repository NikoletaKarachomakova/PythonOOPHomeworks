from datetime import datetime, timedelta
from time import sleep
from pyspectator.processor import Cpu


def generate_report(duration):
    cpu = Cpu(monitoring_latency=1)
    measurements = []

    with cpu:
        begin_time = datetime.now()
        end_time = begin_time + duration
        now = datetime.now()
        while now < end_time:
            measurements.append((now, cpu.load))
            now = datetime.now()
            sleep(1.1)

    return now

generate_report(timedelta(seconds=3))

