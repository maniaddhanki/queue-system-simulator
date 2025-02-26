import mock

from queue_system_simulator.main import run_queue_simulation


@mock.patch("builtins.open")
@mock.patch("queue_system_simulator.main.json")
@mock.patch("queue_system_simulator.main.print_queue_metrics")
@mock.patch("queue_system_simulator.main.QueueingSystem")
def test_should_run_simulatior(
    queue_system_mock, printer_mock, json_mock, open_mock
):

    test_data = {"arrival_rate": 3.26, "service_rate": 4.119}
    json_mock.load.return_value = test_data
    metrics = mock.MagicMock("Metrics")
    queue_mock = mock.MagicMock("queue mock")
    calculate_metrics_mock = mock.MagicMock("calculate metrics")
    metrics_mock = mock.MagicMock("metrics")

    queue_mock.calculate_metrics = calculate_metrics_mock
    queue_mock.calculate_metrics.return_value = metrics_mock
    queue_system_mock.return_value = queue_mock

    run_queue_simulation("test_data_path")
    open_mock.assert_called_once_with("test_data_path", "r")
    queue_system_mock.assert_called_once_with(3.26, 4.119)
    queue_mock.calculate_metrics.assert_called_once_with()
    printer_mock.assert_called_once_with(metrics_mock)


@mock.patch("builtins.print")
@mock.patch("builtins.open")
@mock.patch("queue_system_simulator.main.json")
@mock.patch("queue_system_simulator.main.print_queue_metrics")
@mock.patch("queue_system_simulator.main.QueueingSystem")
def test_should_print_message_when_arrival_rate_is_greater_than_service_rate(
    queue_system_mock, printer_mock, json_mock, open_mock, sys_print_mock
):

    test_data = {"arrival_rate": 5.26, "service_rate": 4.119}
    json_mock.load.return_value = test_data
    metrics = mock.MagicMock("Metrics")
    queue_mock = mock.MagicMock("queue mock")
    calculate_metrics_mock = mock.MagicMock("calculate metrics")
    metrics_mock = mock.MagicMock("metrics")

    queue_mock.calculate_metrics = calculate_metrics_mock
    queue_mock.calculate_metrics.return_value = metrics_mock
    queue_system_mock.return_value = queue_mock

    run_queue_simulation("test_data_path")

    sys_print_mock.assert_called_once_with(
        "arrival rate is greater than service rate. Then the state of system will grow without end. Given are: 5.26 4.119"
    )
    open_mock.assert_called_once_with("test_data_path", "r")
    queue_system_mock.assert_called_once_with(5.26, 4.119)
    queue_mock.calculate_metrics.assert_called_once_with()
    printer_mock.assert_called_once_with(metrics_mock)
