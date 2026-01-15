# Task Scheduling with Linear Programming (ILP)

## Project Overview

This project implements a task-to-server scheduling system formulated as a Binary Integer Linear Programming (ILP) problem.
The goal is to assign computational tasks to servers while respecting CPU, memory, and deadline constraints, and minimizing total execution time.

The project demonstrates optimization modeling, constraint formulation, and solver-based decision making using Python.

---

## Problem Statement

Given:
- A set of tasks, each with CPU, memory, execution time, and optional deadline
- A set of servers, each with limited CPU and memory capacity

Determine an assignment of tasks to servers such that:
- Every task is assigned to exactly one server
- Server resource capacities are not exceeded
- Task deadlines (if defined) are satisfied
- Total execution time is minimized

---

## Mathematical Model

### Decision Variable

x(i,j) = 1 if task i is assigned to server j, otherwise 0

### Objective Function

Minimize total execution time:

Σ Σ time(i) × x(i,j)

---

### Constraints

Task assignment:

Σ x(i,j) = 1   for all tasks i

CPU capacity:

Σ cpu(i) × x(i,j) ≤ CPU(j)   for all servers j

Memory capacity:

Σ memory(i) × x(i,j) ≤ MEM(j)   for all servers j

Deadline (if defined):

Σ time(i) × x(i,j) ≤ deadline(i)

---

## Project Structure

├── data.py
├── solver.py
├── experiments.py
├── visualize.py
├── main.py
└── README.md


---

## File Descriptions

### data.py
Defines Task and Server data classes and generates random problem instances.

### solver.py
Builds and solves the Integer Linear Programming model using PuLP and the CBC solver.

### experiments.py
Runs scalability experiments and measures solver runtime for increasing problem sizes.

### visualize.py
Visualizes solver runtime, task assignments, and resource utilization.

### main.py
Main entry point that executes experiments, solves the model, and displays results.

---

## Installation

Install required dependencies:

pip install pulp matplotlib pandas


---

## Running the Project

Execute the program:


The program will:
- Run scalability experiments
- Solve a sample scheduling instance
- Print task-to-server assignments
- Plot CPU and memory utilization

---

## Experimental Evaluation

The project evaluates:
- Solver runtime as the number of tasks increases
- Feasibility and optimality of solutions
- Resource utilization efficiency per server

---

## Technologies Used

- Python 3
- PuLP (Integer Linear Programming)
- CBC Solver
- Matplotlib
- Pandas

---

## Possible Extensions

- Add task priorities
- Introduce time-based scheduling
- Multi-objective optimization
- Compare multiple ILP solvers
- Energy-aware server modeling

---

## Academic Relevance

This project demonstrates:
- Formal ILP modeling
- Constraint-based optimization
- Experimental performance analysis
- Clean software modularization

Suitable for university coursework, optimization classes, and technical portfolios.

---

## Author

Ogannes Mkrtchian  
Computer Science Student


