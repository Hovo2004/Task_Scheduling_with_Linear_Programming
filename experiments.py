import time
from data import generate_tasks, generate_servers
from solver import solve_task_scheduling


def run_scalability_experiments():
    results = []

    for n_tasks in [10, 20, 30, 40, 50]:
        tasks = generate_tasks(n_tasks)
        servers = generate_servers(5)

        start = time.time()
        model, x, status = solve_task_scheduling(tasks, servers)
        end = time.time()

        results.append({
            "tasks": n_tasks,
            "servers": 5,
            "status": status,
            "time_sec": end - start
        })

    return results
