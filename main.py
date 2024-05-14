import sys

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

def fcfs(requests, initial_head_position):
    total_movement = 0
    current_position = initial_head_position
    
    for request in requests:
        total_movement += abs(current_position - request)
        current_position = request
    
    return total_movement

def scan(requests, initial_head_position, max_cylinder):
    total_movement = 0
    current_position = initial_head_position
    direction = 1  # 1 for moving towards the end, -1 for moving towards the start
    
    requests.sort()
    
    # Move in the current direction until we reach the end
    if direction == 1:
        for request in requests:
            if request >= current_position:
                total_movement += abs(current_position - request)
                current_position = request
        
        # Reverse direction at the end
        total_movement += abs(current_position - max_cylinder)
        current_position = max_cylinder
        direction = -1

    # Now move in the opposite direction
    for request in reversed(requests):
        if request <= current_position:
            total_movement += abs(current_position - request)
            current_position = request

    return total_movement

def c_scan(requests, initial_head_position, max_cylinder):
    total_movement = 0
    current_position = initial_head_position
    
    requests.sort()
    
    # Move towards the end
    for request in requests:
        if request >= current_position:
            total_movement += abs(current_position - request)
            current_position = request
    
    # Jump to the beginning
    total_movement += abs(current_position - max_cylinder)
    current_position = 0

    # Continue moving towards the end again
    for request in requests:
        if request < initial_head_position:
            total_movement += abs(current_position - request)
            current_position = request
    
    return total_movement

def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_head_position> <requests_file>")
        sys.exit(1)

    initial_head_position = int(sys.argv[1])
    requests_file = sys.argv[2]
    max_cylinder = 4999

    requests = read_requests(requests_file)

    fcfs_movement = fcfs(requests, initial_head_position)
    scan_movement = scan(requests, initial_head_position, max_cylinder)
    c_scan_movement = c_scan(requests, initial_head_position, max_cylinder)

    print(f"FCFS total movement: {fcfs_movement}")
    print(f"SCAN total movement: {scan_movement}")
    print(f"C-SCAN total movement: {c_scan_movement}")

if __name__ == "__main__":
    main()
