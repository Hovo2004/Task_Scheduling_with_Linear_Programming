from dataclasses import dataclass
import random

@dataclass
class Task:
    id: int
    cpu: float
    memory: float
    time: float
    deadline: float | None = None

@dataclass
class Server:
    id: int
    cpu_capacity: float
    memory_capacity: float


def generate_tasks(n, seed=0):
    random.seed(seed)
    tasks = []
    for i in range(n):
        cpu = random.uniform(1, 4)
        memory = random.uniform(1, 4)
        time = random.uniform(1, 5)
        deadline = time + random.uniform(1, 5)
        tasks.append(Task(i, cpu, memory, time, deadline))
    return tasks


def generate_servers(m, seed=0):
    random.seed(seed + 100)
    servers = []
    for j in range(m):
        cpu_capacity = random.uniform(10, 20)
        memory_capacity = random.uniform(10, 20)
        servers.append(Server(j, cpu_capacity, memory_capacity))
    return servers
