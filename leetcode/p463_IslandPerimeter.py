# SUBMITTED

class Solution:
	def islandPerimeter(self, grid):
		"""
		:type grid: List[List[int]]
		:rtype: int
		"""
		
		total = 0
		for y in range(len(grid)):
			for x in range(len(grid[y])):
				# Skip if not on island
				if grid[y][x] != 1:
					continue

				# Check if each of the four side is either empty or edge
				if x != len(grid[y]) - 1:
					total += 1 - grid[y][x + 1]
				else:
					total += 1

				if x != 0:
					total += 1 - grid[y][x - 1]
				else:
					total += 1

				if y != len(grid) - 1:
					total += 1 - grid[y + 1][x]
				else:
					total += 1

				if y != 0:
					total += 1 - grid[y - 1][x]
				else:
					total += 1

		return total