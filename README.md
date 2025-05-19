# Job Shop Scheduling (SPT Rule) — Python Implementation

> Course project for **Algorithms & Complexity** (5th semester) — Department of Informatics and Telecommunications of the University of Ioannina.

## Problem Statement
Given a list of jobs and machines, each job consists of a sequence of operations that must be processed in a specific order. The goal is to schedule these operations to minimize the **makespan** (total time to complete all jobs), using the **Shortest Processing Time (SPT)** rule.

## Approach
1. **Input Parsing**  
   Read `.txt` files containing the number of jobs, number of machines, operation durations, and job routes.

2. **Scheduling Using SPT**  
   - Jobs are sorted by total processing time (ascending).
   - Each operation is scheduled based on machine availability and job order.
   - Both job precedence and machine availability are respected.

3. **Gantt Chart Visualization**  
   The final schedule is visualized using a Gantt chart (via matplotlib) to show the timing and sequence of operations on each machine.

## Complexity
- The SPT rule is greedy: efficient for small to medium inputs.
- Naive worst-case time complexity: **O(n²)**

## Input Format (`*.txt` files)
```
n
m
T (optional optimal makespan)

<processing times>     # n lines of m integers
<machine sequences>    # n lines of m integers (machine indices)
```

## Example Files
- `la01.txt`, `la02.txt`, `la03.txt`, `la04.txt`, `la05.txt`
- `mt06.txt`, `mt10.txt`, `mt20.txt`

## Results (SPT vs Optimal)

| Instance | SPT Makespan | Optimal | Δ     |
|----------|--------------|---------|-------|
| la01     | 688          | 666     | +22   |
| la02     | 737          | 655     | +82   |
| la03     | 1110         | 597     | +513  |
| la04     | 938          | 590     | +348  |
| la05     | 1211         | 593     | +618  |
| mt06     | 1578         | 55      | +1523 |
| mt10     | 1616         | 930     | +686  |
| mt20     | 1852         | 1165    | +687  |

## How to Run
```bash
git clone https://github.com/konrantos/job-shop-scheduling-python.git
cd job-shop-scheduling-python
python job_shop_scheduler.py la01.txt
```

## Report

A full technical report (in English) is available here:  
📄 [docs/report_en.pdf](./docs/report_en.pdf)

It includes a detailed description of the problem, SPT rule implementation, results, and a Gantt chart visualization.

## License

This project is licensed under the MIT License.

## Acknowledgements

- University of Ioannina — course project for *Algorithms & Complexity*
- SPT (Shortest Processing Time) is a classic greedy rule in scheduling theory
