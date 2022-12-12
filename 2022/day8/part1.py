from dataclasses import dataclass


@dataclass
class Tree:
    height: int
    visible: bool


if __name__ == "__main__":
    tree_map = []
    with open("./input", "r") as f:
        while line := f.readline().rstrip():
            tree_map.append([Tree(int(x), False) for x in list(line)])

    for i in range(len(tree_map)):
        current_max_height = -1
        j = 0
        while j < len(tree_map[0]) and current_max_height < 9:
            if (tree := tree_map[i][j]).height > current_max_height:
                current_max_height = tree.height
                tree.visible = True
            j += 1

        current_max_height = -1
        j = len(tree_map[0]) - 1
        while j > 0 and current_max_height < 9:
            if (tree := tree_map[i][j]).height > current_max_height:
                current_max_height = tree.height
                tree.visible = True
            j -= 1

    for j in range(len(tree_map[0])):
        current_max_height = -1
        i = 0
        while i < len(tree_map) and current_max_height < 9:
            if (tree := tree_map[i][j]).height > current_max_height:
                current_max_height = tree.height
                tree.visible = True
            i += 1

        current_max_height = -1
        i = len(tree_map[0]) - 1
        while i > 0 and current_max_height < 9:
            if (tree := tree_map[i][j]).height > current_max_height:
                current_max_height = tree.height
                tree.visible = True
            i -= 1

    print(
        sum([
            sum([1
                 for t in tree_map[i]
                 if t.visible])
            for i in range(len(tree_map))
        ]))
