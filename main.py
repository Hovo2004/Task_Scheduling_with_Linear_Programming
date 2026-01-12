from experiments import run_scalability_experiments
from data import generate_tasks, generate_servers
from solver import solve_task_scheduling
from visualize import (
    plot_runtime,
    plot_assignment_matrix,
    plot_resource_utilization
)
import pulp


def main():
    results = run_scalability_experiments()

    for r in results:
        print(
            f"Tasks: {r['tasks']}, "
            f"Servers: {r['servers']}, "
            f"Status: {pulp.LpStatus[r['status']]}, "
            f"Time: {r['time_sec']:.4f}s"
        )

    plot_runtime(results)

    tasks = generate_tasks(10)
    servers = generate_servers(5)
    model, x, status = solve_task_scheduling(tasks, servers)

    if pulp.LpStatus[status] == "Optimal":
        print(f"\nOptimal solution found with total time: {pulp.value(model.objective):.2f}")
        plot_assignment_matrix(tasks, servers, x)
        plot_resource_utilization(tasks, servers, x)
    else:
        print(f"\nNo optimal solution found. Status: {pulp.LpStatus[status]}")


if __name__ == "__main__":
    main()
