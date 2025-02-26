from dataclasses import dataclass


@dataclass
class QueueMetrics:
    l: float
    lq: float
    ls: float
    w: float
    wq: float
    ws: float
