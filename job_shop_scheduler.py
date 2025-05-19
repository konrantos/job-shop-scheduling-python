import matplotlib.pyplot as plt
import numpy as np

def read_file(file_path):
    # Open file for reading
    with open(file_path, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()

    # Convert first and second lines to integers
    num_jobs = int(lines[0].strip())
    num_machines = int(lines[1].strip())

    # Try to parse third line as the optimal makespan
    try:
        optimal_makespan = int(lines[2].strip())
        job_data_start_index = 3
    except ValueError:
        # If parsing fails, assume no optimal makespan is given
        optimal_makespan = None
        job_data_start_index = 2

    # Parse processing times for each job on each machine
    job_times = [list(map(int, lines[i].split())) for i in range(job_data_start_index, job_data_start_index + num_jobs)]

    # Parse machine sequence for each job
    job_sequences = [list(map(int, lines[i].split())) for i in range(job_data_start_index + num_jobs, job_data_start_index + 2 * num_jobs)]

    return num_jobs, num_machines, optimal_makespan, job_times, job_sequences


# Define list of file paths (relative)
file_paths = [
    './la01.txt',
    './la02.txt',
    './la03.txt',
    './la04.txt',
    './la05.txt',
    './mt06.txt',
    './mt10.txt',
    './mt20.txt'
]

# Initialize dictionary to store data for each file
data = {}
for file_path in file_paths:
    num_jobs, num_machines, optimal_makespan, job_times, job_sequences = read_file(file_path)
    data[file_path] = {
        'Number of jobs': num_jobs,
        'Number of machines': num_machines,
        'Optimal makespan': optimal_makespan,
        'Processing times': job_times,
        'Machine sequence': job_sequences
    }

# Print one parsed example
print(data['./la01.txt'])


def calculate_makespan_spt(num_jobs, num_machines, job_times, job_sequences):
    # Create machine availability and job completion trackers
    machine_schedule = [0] * num_machines
    job_completion = [0] * num_jobs

    # Sort jobs by total processing time (SPT rule)
    sorted_jobs = sorted(range(num_jobs), key=lambda x: sum(job_times[x]))

    for job in sorted_jobs:
        for step in range(num_machines):
            machine = job_sequences[job][step] - 1
            time = job_times[job][step]
            machine_schedule[machine] = max(machine_schedule[machine], job_completion[job]) + time
            job_completion[job] = machine_schedule[machine]

    return max(machine_schedule)


# Process one file at a time
def process_file(file_path):
    num_jobs, num_machines, optimal_makespan, job_times, job_sequences = read_file(file_path)
    makespan_spt = calculate_makespan_spt(num_jobs, num_machines, job_times, job_sequences)

    print(f'File: {file_path}')
    print(f'Calculated Makespan (SPT): {makespan_spt}')
    if optimal_makespan is not None:
        print(f'Optimal Makespan: {optimal_makespan}')
        print(f'Difference: {makespan_spt - optimal_makespan}')


if __name__ == '__main__':
    for file_path in file_paths:
        process_file(file_path)


def plot_gantt_chart(num_machines, num_jobs, start_times, end_times, makespan):
    # Create Gantt chart figure
    fig, ax = plt.subplots(figsize=(12, 6))
    colors = plt.cm.tab20.colors

    for job in range(num_jobs):
        for machine in range(num_machines):
            start = start_times[job][machine]
            end = end_times[job][machine]
            if start < end:
                ax.barh(machine, end - start, left=start, color=colors[job % len(colors)], edgecolor='black')

    ax.set_yticks(range(num_machines))
    ax.set_yticklabels([f'M{m+1}' for m in range(num_machines)])
    ax.invert_yaxis()
    ax.set_xlabel('Time')
    ax.set_ylabel('Machine')
    ax.set_title(f'SPT Gantt Chart (Makespan: {int(makespan)})')

    custom_lines = [plt.Line2D([0], [0], color=colors[job % len(colors)], lw=4) for job in range(num_jobs)]
    ax.legend(custom_lines, [f'Job {j+1}' for j in range(num_jobs)], loc='upper center', bbox_to_anchor=(0.5, -0.05), shadow=True, ncol=num_jobs)

    plt.tight_layout()
    plt.show()


# Read data from one file (e.g. la01)
file_path = './la01.txt'
parsed_num_jobs, parsed_num_machines, optimal_makespan, parsed_processing_times, parsed_machine_orders = read_file(file_path)

# Calculate makespan using SPT
makespan_spt_user = calculate_makespan_spt(parsed_num_jobs, parsed_num_machines, parsed_processing_times, parsed_machine_orders)

# Initialize start and end time matrices
start_times = np.zeros((parsed_num_jobs, parsed_num_machines))
end_times = np.zeros((parsed_num_jobs, parsed_num_machines))

# Initialize availability and completion trackers
machine_availability = [0] * parsed_num_machines
job_completion_times = [0] * parsed_num_jobs

# Sort jobs by total processing time (SPT)
sorted_jobs = sorted(range(parsed_num_jobs), key=lambda x: sum(parsed_processing_times[x]))

# Apply SPT logic
for job in sorted_jobs:
    for step in range(parsed_num_machines):
        machine = parsed_machine_orders[job][step] - 1
        proc_time = parsed_processing_times[job][step]
        start_time = max(machine_availability[machine], job_completion_times[job])
        end_time = start_time + proc_time
        start_times[job][machine] = start_time
        end_times[job][machine] = end_time
        machine_availability[machine] = end_time
        job_completion_times[job] = end_time

# Plot final Gantt chart
plot_gantt_chart(parsed_num_machines, parsed_num_jobs, start_times, end_times, makespan_spt_user)
