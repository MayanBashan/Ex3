class NodeData:

    def __init__(self, key: int, info: str = None, tag: float = 0, pos: tuple = None):
        self.info = info
        self.tag = tag
        self.key = key
        self.edges_from_node = {}
        self.edges_to_node = {}
        self.pos = pos

    def add_edge_from_node(self, ni_key: int, weight: float):
        self.edges_from_node[ni_key] = weight

    def add_edge_to_node(self, ni_key: int, weight: float):
        self.edges_to_node[ni_key] = weight

    def get_edges_from_node(self):
        return self.edges_from_node

    def get_edges_to_node(self):
        return self.edges_to_node

    def get_edge_weight(self, ni_key: int):
        return self.edges_from_node.get(ni_key)

    def get_key(self):
        return self.key

    def get_info(self):
        return self.info

    def get_tag(self):
        return self.tag

    def get_pos(self):
        return self.pos

    def set_pos(self, pos: tuple):
        self.pos = pos

    def set_tag(self, tag: float):
        self.tag = tag

