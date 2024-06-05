from collections import deque
from typing import List, Tuple, Union


def bfs_with_path(
        grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]
) -> Union[int, Tuple[int, List[List[Union[int, str]]]]]:
    map_height_cells, map_width_cells = len(grid), len(grid[0])
    available_step_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    path_cells_queue = deque([(start[0], start[1], 0)])  # Инициализируем очередь с начальной позицией и расстоянием 0
    visited_cells = [[False] * map_width_cells for _ in range(map_height_cells)]  # Массив для отслеживания посещённых ячеек
    previous_cell = [[None] * map_width_cells for _ in range(map_height_cells)]  # Массив для отслеживания предыдущих ячеек
    visited_cells[start[0]][start[1]] = True  # Отмечаем начальную ячейку как посещённую

    while path_cells_queue:
        current_row, current_column, distance_cells = path_cells_queue.popleft()  # Извлекаем текущую ячейку из очереди

        if (current_row, current_column) == end:
            # Восстанавливаем путь
            path = []
            while (current_row, current_column) != start:
                path.append((current_row, current_column))
                current_row, current_column = previous_cell[current_row][current_column]
            path.append(start)
            path.reverse()

            # Отрисовываем путь
            for px, py in path:
                grid[px][py] = '*'

            return distance_cells, grid  # Возвращаем расстояние и карту с отмеченным путём

        for row_step, column_step in available_step_directions:
            new_row, new_column = current_row + row_step, current_column + column_step
            if 0 <= new_row < map_height_cells and 0 <= new_column < map_width_cells and not visited_cells[new_row][new_column] and grid[new_row][new_column] == 0:
                path_cells_queue.append((new_row, new_column, distance_cells + 1))  # Добавляем новую ячейку в очередь
                visited_cells[new_row][new_column] = True  # Отмечаем новую ячейку как посещённую
                previous_cell[new_row][new_column] = (current_row, current_column)  # Сохраняем текущую ячейку как предыдущую для новой ячейки

    return -1, grid  # Путь не найден, возвращаем -1 и исходную карту


# Пример использования
grid = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (0, 0)
end = (0, 4)

distance, path_grid = bfs_with_path(grid, start, end)

print(f"Кратчайшее расстояние: {distance}")

# Выводим карту с отмеченным путём
for row in path_grid:
    print(' '.join(str(cell) for cell in row))
