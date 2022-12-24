from queue import PriorityQueue
from utils import parse_input, manhattan_distance, Node, in_bounds

if __name__ == "__main__":

    height_map, s_pos, g_pos = parse_input()
    h, w = len(height_map), len(height_map[0])
    explored_nodes = set()
    frontier = PriorityQueue()
    to_goal = lambda x: manhattan_distance(x, g_pos)

    frontier.put(Node(
        position=s_pos,
        distance_to_goal=to_goal(s_pos),
        cost=0,
    ))

    while frontier.empty() is not True:
        current: Node = frontier.get()
        if tuple(current.position) in explored_nodes:
            continue
        if current.distance_to_goal == 0:
            break

        explored_nodes.add(tuple(current.position))

        for n in current.get_neighbors():
            if in_bounds(n, h_max=h, w_max=w) and (
                    height_map[n[0], n[1]] -
                    height_map[current.position[0], current.position[1]]) < 2:
                frontier.put(
                    Node(
                        position=n,
                        distance_to_goal=to_goal(n),
                        cost=current.cost + 1,
                    ))

    print(current.cost)
