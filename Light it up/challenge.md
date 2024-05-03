# Light It Up (Easy)


## Description
In the vast expanse of the Wild West, John Marston find himself traversing a rugged terrain. He has a straight path stretching across the frontier, with `n` sections, where each section is either illuminated by the light of day or shrouded in the darkness of night.

Your task is to illuminate the entire path, turning every dark section into light. You can select a continuous segment of the path and light it up. Once lit, all the dark sections within this segment will be bathed in light, while the already illuminated sections will remain as they are.

What is the minimum number of operations needed to illuminate to ensure that every section of the trail is lit up?

## Inputs
- The first line `n` is the number of sections of the path
- The second line contains `n` numbers either `0` (dark section) or `1`(light section) 


## Output
- the minimum number of operations to illuminate all the path.

## Constraints
- 0 <= n <= 10^6

## Example 1
input:
5
1 0 0 1 0
output:
2

## Example 2
input:
2
1 1
output:
0
