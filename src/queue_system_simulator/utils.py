def print_system_metrics(queue_metrics,system_cost):
    print("Average number waiting in system : ", queue_metrics.l)
    print("Average number waiting in line : ", queue_metrics.lq)
    print("Average number in service  : ", queue_metrics.ls)
    print("Average waiting time of passenger in system : ", queue_metrics.w)
    print("Average waiting time of passenger in line : ", queue_metrics.wq)
    print("Average waiting time of passenger in service : ", queue_metrics.ws)
    print("Total System cost : ", system_cost)
