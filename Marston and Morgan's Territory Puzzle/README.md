# Marston and Morgan's Territory Puzzle

## Description
After the successful train robbery, John Marston and Arthur Morgan stumble upon a map detailing the strategic locations of various gang supply caches and their connections. John and Arthur, after studying the map, realize that certain locations are crucial for controlling and monitoring the flow of resources and maintaining dominance in the region.
However, the challenge arises when they realize that some locations are heavily fortified or strategically positioned, making it difficult to control without risking exposure or spreading their resources too thin. To reduce the risk of getting caught together, they want to be separated on the map into two areas such that each area controls a set of locations that guarantee the control of the region. Your task is to help them identify the areas.

## Inputs
The first line of the input contains two integers n and m  — the number of locations and the number of roads, respectively.
Each of the next m lines contains a pair of integers ui and vi, denoting a road between ui and vi.

## Output
If John Marston and Arthur Morgan can't be separated on the map, print -1. Otherwise, for each area, two lines must be printed:
The first line contains a single integer k denoting the number of locations in the area
The second line contains k integers – locations numbers that belong to the area

## Constraints
- 2 ≤ n ≤ 1 000, 1 ≤ m ≤ 1 000
- 1 ≤ ui, vi ≤ n

## Examples

| Input     | Output |
|-----------|--------|
| 4 2       | 1      |
| 1 3       | 3      |
| 3 4       | 2      | 
|           | 1 4    |
|-----------|--------|
| 5 3       | -1     |
| 2 5       |        |
| 2 4       |        | 
| 3 4       |        |