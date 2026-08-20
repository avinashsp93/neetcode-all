class Solution:
    def isPathCrossing(self, path: str) -> bool:
        coordinates = (0,0)
        visited = set()
        visited.add(coordinates)
        for dir in path:
            calcCoordinates = (0,0)
            if dir == "N":
                calcCoordinates = (coordinates[0], coordinates[1] + 1)
            elif dir == "S":
                calcCoordinates = (coordinates[0], coordinates[1] - 1)
            elif dir == "E":
                calcCoordinates = (coordinates[0] + 1, coordinates[1])
            elif dir == "W":
                calcCoordinates = (coordinates[0] - 1, coordinates[1])
            coordinates = calcCoordinates
            if coordinates in visited:
                return True
            else:
                visited.add(coordinates)
        return False