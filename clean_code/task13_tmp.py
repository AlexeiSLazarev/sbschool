from collections import deque
from typing import List, Tuple, Union


def bfs_with_path(
        grid: List[List[int]], start: Tuple[int, int], end: Tuple[int, int]
) -> Union[int, Tuple[int, List[List[Union[int, str]]]]]:
    rows, cols = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    queue = deque([(start[0], start[1], 0)])  # Инициализируем очередь с начальной позицией и расстоянием 0
    visited = [[False] * cols for _ in range(rows)]  # Массив для отслеживания посещённых ячеек
    prev = [[None] * cols for _ in range(rows)]  # Массив для отслеживания предыдущих ячеек
    visited[start[0]][start[1]] = True  # Отмечаем начальную ячейку как посещённую

    while queue:
        x, y, dist = queue.popleft()  # Извлекаем текущую ячейку из очереди

        if (x, y) == end:
            # Восстанавливаем путь
            path = []
            while (x, y) != start:
                path.append((x, y))
                x, y = prev[x][y]
            path.append(start)
            path.reverse()

            # Отрисовываем путь
            for px, py in path:
                grid[px][py] = '*'

            return dist, grid  # Возвращаем расстояние и карту с отмеченным путём

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny] and grid[nx][ny] == 0:
                queue.append((nx, ny, dist + 1))  # Добавляем новую ячейку в очередь
                visited[nx][ny] = True  # Отмечаем новую ячейку как посещённую
                prev[nx][ny] = (x, y)  # Сохраняем текущую ячейку как предыдущую для новой ячейки

    return -1, grid  # Путь не найден, возвращаем -1 и исходную карту


# Пример использования
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0]
]
start = (4, 0)
end = (0, 4)

distance, path_grid = bfs_with_path(grid, start, end)

print(f"Кратчайшее расстояние: {distance}")

# Выводим карту с отмеченным путём
for row in path_grid:
    print(' '.join(str(cell) for cell in row))

