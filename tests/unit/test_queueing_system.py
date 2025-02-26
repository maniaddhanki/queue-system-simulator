import mock

from queue_system_simulator.queueing_system import QueueingSystem


@mock.patch("queue_system_simulator.queueing_system.QueueMetrics")
def test_should_calculate_queue_metrics(queue_metrics_mock):
    queueing_system = QueueingSystem(8, 16)
    queueing_system.calculate_metrics()

    queue_metrics_mock.assert_called_once_with(
        1.0, 0.5, 0.5, 0.125, 0.0625, 0.0625
    )
