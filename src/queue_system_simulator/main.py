import json
from typing import Annotated

from typer import Option, Typer

from .queueing_system import QueueingSystem
from .utils import print_system_metrics

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
    duration = queue_data["duration"]
    operator_cost = queue_data["operator_cost"]
    machine_installation_cost = queue_data["machine_installation_cost"]
    machine_operation_cost = queue_data["machine_operation_cost"]

    if arrival_rate > service_rate:
        print(
            f"arrival rate is greater than service rate. Then the state of system will grow without end. Given are: {arrival_rate} {service_rate}"
        )

    queue_system = QueueingSystem(
        arrival_rate,
        service_rate,
        duration,
        operator_cost,
        machine_installation_cost,
        machine_operation_cost,
    )

    queue_metrics = queue_system.calculate_metrics()
    total_cost = queue_system.calculate_cost()
    print_system_metrics(queue_metrics,total_cost)
