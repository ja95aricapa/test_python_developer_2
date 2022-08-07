from typing import Tuple


def search_path_list(
    grid: int, start_point: Tuple[int, int], end_point: Tuple[int, int]
):
    """
    Search for a path from start_point to end_point in a grid of size n x n.

    Args:
        grid (int): Indicates the size of the grid.
        start_point (tuple(int, int)): Coordinate of the start point.
        end_point (tuple(int, int)): Coordinate of the end point.

    Algorithm:
        1. step over start_point and add it to the path
        2. move about the x-axis until the x-coordinate of my current position is the same as the x-coordinate of the end point
            2.1 if x-cordinate is diferrent, move to the next nearest x-coordinate and add it to the path
        3. move about the y-axis until the y-coordinate of my current position is the same as the y-coordinate of the end point
            3.1 if y-cordinate is diferrent, move to the next nearest y-coordinate and add it to the path
        4. if the current position is the same as the end point, add it and to the path
        5. remove start and end point from the path
        6. calculate the distance of the path
        7. return the path and the cost distance
    """
    if grid <= 2:
        raise ValueError("Grid size must be greater than 2")
    grid = grid - 1
    check_grid = [
        grid < start_point[0],
        grid < start_point[1],
        grid < end_point[0],
        grid < end_point[1],
    ]
    if True in check_grid:
        raise ValueError("Invalid start or end point, it must be within the grid")
    # Initialize the queue
    current_x = start_point[0]
    current_y = start_point[1]
    list_pos = [(current_x, current_y)]
    # move over x axis
    while current_x != end_point[0]:
        if current_x < end_point[0]:
            current_x = current_x + 1
        if current_x > end_point[0]:
            current_x = current_x - 1
        list_pos.append((current_x, current_y))
    # move over y axis
    while current_y != end_point[1]:
        if current_y < end_point[1]:
            current_y = current_y + 1
        if current_y > end_point[1]:
            current_y = current_y - 1
        list_pos.append((current_x, current_y))
    # remove the start point and end point
    list_pos = list_pos[1:-1]
    # calculate the path cost
    cost = len(list_pos)
    return cost, list_pos


if __name__ == "__main__":
    try:
        grid_size = 5
        start = (0, 0)
        end = (4, 5)
        cost, list_pos = search_path_list(
            grid=grid_size, start_point=start, end_point=end
        )
        print(cost)
        print(list_pos)
    except ValueError as e:
        print(e)
