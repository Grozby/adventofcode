import abc


class TypeObject(abc.ABC):

    def __init__(self, name: str, parent):
        self.name = name
        self.parent = parent

    @property
    @abc.abstractmethod
    def is_directory(self) -> bool:
        pass

    @property
    def full_name(self) -> str:
        if self.parent is not None:
            return f"{self.parent}/{self.name}"
        else:
            return self.name


class File(TypeObject):

    def __init__(self, name: str, size: int, parent):
        super().__init__(name=name, parent=parent)
        self.size = size

    @property
    def is_directory(self) -> bool:
        return False


class Directory(TypeObject):

    def __init__(self, name, parent):
        super().__init__(name=name, parent=parent)
        self.children = {}
        self._size = None

    @property
    def is_directory(self) -> bool:
        return True

    @property
    def size(self) -> int:
        if self._size is None:
            if len(self.children) == 0:
                self._size = 0
            else:
                self._size = sum([c.size for c in self.children.values()])
        return self._size

    def add_directory_child(self, name):
        self.children[name] = Directory(name, parent=self)

    def add_file_child(self, name, size):
        self.children[name] = File(
            name=name,
            size=size,
            parent=self,
        )

    def get_directory_children(self):
        return [x for x in self.children.values() if x.is_directory]


if __name__ == "__main__":

    root_directory = current_directory = Directory(name="/", parent=None)

    with open("./input", "r") as f:
        f.readline()
        line = f.readline().rstrip()
        while line:
            if line == "$ ls":
                while (line := f.readline().rstrip()) and line[0] != "$":
                    if line.startswith("dir"):
                        current_directory.add_directory_child(line[4:])
                    else:
                        file_size, file_name = line.split(" ")
                        current_directory.add_file_child(
                            name=file_name,
                            size=int(file_size),
                        )
            elif line.startswith("$ cd"):
                if line[5:] == "..":
                    current_directory = current_directory.parent
                else:
                    current_directory = current_directory.children[line[5:]]
                line = f.readline().rstrip()
            else:
                raise RuntimeError("Should not be here!")

    total_sum = 0
    checked_directories = set()
    to_search = root_directory.get_directory_children()

    while len(to_search) != 0:
        current_directory = to_search.pop()
        if current_directory.full_name not in checked_directories:
            checked_directories.add(current_directory.full_name)
            if current_directory.size <= 100000:
                total_sum += current_directory.size

            to_search.extend(current_directory.get_directory_children())

    print(total_sum)
