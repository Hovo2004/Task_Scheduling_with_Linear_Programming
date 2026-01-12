import pulp


def solve_task_scheduling(tasks, servers):
    model = pulp.LpProblem("Task_Scheduling", pulp.LpMinimize)

    x = {}
    for task in tasks:
        for server in servers:
            x[(task.id, server.id)] = pulp.LpVariable(
                f"x_{task.id}_{server.id}",
                cat="Binary"
            )

    model += pulp.lpSum(
        task.time * x[(task.id, server.id)]
        for task in tasks
        for server in servers
    )

    for task in tasks:
        model += pulp.lpSum(
            x[(task.id, server.id)]
            for server in servers
        ) == 1

        if task.deadline is not None:
            model += pulp.lpSum(
                task.time * x[(task.id, server.id)]
                for server in servers
            ) <= task.deadline

    for server in servers:
        model += pulp.lpSum(
            task.cpu * x[(task.id, server.id)]
            for task in tasks
        ) <= server.cpu_capacity

        model += pulp.lpSum(
            task.memory * x[(task.id, server.id)]
            for task in tasks
        ) <= server.memory_capacity

    status = model.solve(pulp.PULP_CBC_CMD(msg=False))
    return model, x, status
