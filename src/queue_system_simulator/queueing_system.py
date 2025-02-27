from .queue_metrics import QueueMetrics


class QueueingSystem:
    def __init__(
        self,
        arrival_rate,
        service_rate,
        duration,
        operator_cost,
        machine_installation_cost,
        machine_operation_cost,
    ):
        self.arrival_rate = arrival_rate
        self.service_rate = service_rate
        self.duration = duration
        self.operator_cost = operator_cost
        self.machine_installation_cost = machine_installation_cost
        self.machine_operation_cost = machine_operation_cost

    def calculate_cost(self):
        total_operator_cost = self.operator_cost * self.duration
        machine_operation_cost = self.machine_operation_cost * self.duration
        return (
            total_operator_cost
            + self.machine_installation_cost
            + machine_operation_cost
        )

    def calculate_metrics(self):
        utilization_factor = self.arrival_rate / self.service_rate
        waiting_in_line = (utilization_factor**2) / (1 - utilization_factor)
        waiting_in_system = utilization_factor + waiting_in_line

        service_time = 1 / self.service_rate
        line_time = waiting_in_line / self.arrival_rate
        total_time = service_time + line_time

        return QueueMetrics(
            waiting_in_system,
            waiting_in_line,
            utilization_factor,
            total_time,
            line_time,
            service_time,
        )
