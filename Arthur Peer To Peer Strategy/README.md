
# Arthur’s peer-to-peer strategy

### Submission Constraints
- Time limit per test: **0.2 seconds**
- Memory limit per test: **Default(65 MB)**

## Description
A showdown is approaching between the Van der Linde gang and Arthur and Dutch's allies. Arthur and the Dutch allies geared up to spread across the map to fight across multiple fronts, in which they needed to establish communication to exchange data and critical information. They aimed to set up a peer-to-peer network, ensuring messages could pass securely without relying on a single messenger who might turn into a traitor.

Their plan was for every soldier to act as a point in this network, allowing messages to travel through several soldiers to reach their target. But the risk lay in soldiers getting cut off—due to death or other reasons—which could break parts of the network. Communication is considered established if a message is communicated between any two soldiers a and b

Arthur and Dutch needed to find the Safety Factor of this peer-to-peer setup before attempting to use it. It meant figuring out the minimum number of soldiers whose disconnection would cause the network to not be established. Your task is to help them find out this safety factor!

## Inputs
You will be given the first line that starts with two integers n and m–the number of soldiers and the number of connections between them respectively. Followed by m lines, each line contains input in the format of (u, v) designating a communication line between soldiers u and m

## Output
The safety factor of the peer-to-peer setup

## Constraints
- 0 <= n <=60
- The communication between two soldiers is bidirectional
- locations number is incremental, starting from zero.

## Examples
| Input     | Output |
|-----------|--------|
|8 11       | 2      |
|(0,1)      |        |
|(0,3)      |        |
|(0,2)      |        |
|(1,2)      |        |
|(2,3)      |        |
|(2,4)      |        |
|(3,4)      |        |
|(3,5)      |        |
|(5,6)      |        |
|(4,7)      |        |
|(6,7)      |        |


