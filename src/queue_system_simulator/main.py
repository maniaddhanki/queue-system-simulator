import json
from typing import Annotated

from typer import Option, Typer

from .queueing_system import QueueingSystem
from .utils import print_queue_metrics

app = Typer()


@app.command(help="Simulate Queue and give metrics")
def run_queue_simulation(
    passenger_data_file: Annotated[
        str, Option(help="Path to the file containing the data")
    ] = None,
):

    with open(passenger_data_file, "r") as fp:
        queue_data = json.load(fp)

    arrival_rate = queue_data["arrival_rate"]
    service_rate = queue_data["service_rate"]
    if arrival_rate > service_rate:
        print(
            f"arrival rate is greater than service rate. Then the state of system will grow without end. Given are: {arrival_rate} {service_rate}"
        )

    queue_system = QueueingSystem(arrival_rate, service_rate)
    queue_metrics = queue_system.calculate_metrics()
    print_queue_metrics(queue_metrics)
