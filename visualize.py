import matplotlib.pyplot as plt
import pandas as pd
import pulp


def plot_runtime(results):
    tasks = [r["tasks"] for r in results]
    times = [r["time_sec"] for r in results]

    plt.figure()
    plt.plot(tasks, times, marker="o")
    plt.xlabel("Number of Tasks")
    plt.ylabel("Solver Time (seconds)")
    plt.title("Solver Runtime vs Problem Size")
    plt.grid(True)
    plt.show()


def plot_assignment_matrix(tasks, servers, x):
    data = []

    for task in tasks:
        row = []
        for server in servers:
            value = x[(task.id, server.id)].value()
            row.append(value)
        data.append(row)

    df = pd.DataFrame(
        data,
        index=[f"Task {t.id}" for t in tasks],
        columns=[f"Server {s.id}" for s in servers]
    )

    print("\nTask-to-Server Assignment Matrix:")
    print(df)


def plot_resource_utilization(tasks, servers, x):
    cpu_used = []
    mem_used = []

    for server in servers:
        cpu = sum(
            task.cpu * x[(task.id, server.id)].value()
            for task in tasks
        )
        mem = sum(
            task.memory * x[(task.id, server.id)].value()
            for task in tasks
        )
        cpu_used.append(cpu)
        mem_used.append(mem)

    server_ids = [s.id for s in servers]

    plt.figure()
    plt.bar(server_ids, cpu_used)
    plt.xlabel("Server ID")
    plt.ylabel("CPU Used")
    plt.title("CPU Utilization per Server")
    plt.show()

    plt.figure()
    plt.bar(server_ids, mem_used)
    plt.xlabel("Server ID")
    plt.ylabel("Memory Used")
    plt.title("Memory Utilization per Server")
    plt.show()
