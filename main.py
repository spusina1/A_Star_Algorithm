
class Node():

    def __init__(self, parent=None, index=None, distance_from_start=None):
        self.parent = parent
        self.index = index
        self.distance_from_start = distance_from_start
        self.heuristic_distance = 0
        self.total_distance = 0


def a_star(start, end, w , h):
    start_node = Node(None, start, 0)
    start_node.heuristic_distance = h[0]
    start_node.total_distance = h[0]
    end_node = Node(None, end, None)

    open_list = []
    visited_list = []

    open_list.append(start_node)

    while len(open_list) > 0:
        current_node = open_list[0]
        current_index = 0
        for index, item in enumerate(open_list):
            if item.total_distance < current_node.total_distance:
                current_node = item
                current_index = index

        open_list.pop(current_index)
        visited_list.append(current_node)

        if current_node.index == end_node.index:
            path = []
            current = current_node
            while current is not None:
                path.append(current.index)
                current = current.parent
            print ("Duzina najkraceg puta je: ", current_node.distance_from_start)
            return path[::-1]  # Return reversed path

        i = current_node.index - 1
        for j in range (0,len(w)):
            if w[i][j] > 0:
                logic_visited = False
                for index, item in enumerate(visited_list):
                    if item.index == j + 1:
                        logic_visited = True
                        break
                if logic_visited:
                    continue

                g = current_node.distance_from_start + w[i][j]
                logic_open = False
                logic_child = False
                for index, item in enumerate(open_list):
                    if item.index == j + 1:
                        logic_open = True
                        if g < item.distance_from_start:
                            item.distance_from_start = g
                            item.total_distance = item.distance_from_start + item.heuristic_distance
                            item.parent = current_node

                if logic_open == False:
                    new_node = Node(current_node, j+1, g)
                    new_node.heuristic_distance = h[j] #heuristike cu izracunati prije pokretanja algoritma
                    new_node.total_distance = new_node.distance_from_start + new_node.heuristic_distance
                    open_list.append(new_node)

    return []




if __name__ == '__main__':
    w = [[0,4,3,0,0,0,0,0],
         [0,0,0,0,12,5,0],
         [0,0,0,7,10,0,0],
         [0,0,0,0,2,0,0],
         [0,0,0,0,0,0,5],
         [0,0,0,0,0,0,10],
         [0,0,0,0,0,0,0]]

    w2 =[[0, 9, 4, 7, 0, 0, 0, 0],
         [0, 0, 0, 0, 11, 0, 0],
         [0, 0, 0, 0, 17, 12, 0],
         [0, 0, 0, 0, 0, 14, 0],
         [0, 0, 0, 0, 0, 0, 5],
         [0, 0, 0, 0, 0, 0, 9],
         [0, 0, 0, 0, 0, 0, 0]]

    w3 = [[0,6,0,0,0,3,0,0,0,0],
          [0,0,3,2,0,0,0,0,0,0],
          [0,0,0,1,5,0,0,0,0,0],
          [0,0,0,0,8,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,5,5],
          [0,0,0,0,0,0,1,7,0,0],
          [0,0,0,0,0,0,0,0,3,0],
          [0,0,0,0,0,0,0,0,2,0],
          [0,0,0,0,0,0,0,0,0,3],
          [0,0,0,0,0,0,0,0,0,0]]

    h = [14,12,11,6,4,11,0]
    h2 = [21,14,18,18,5,8,0]
    h3 = [10,8,5,7,3,6,5,3,1,0]

    start = 1
    end = 7

    print("Najkraci put cine cvorovi: ", a_star(start,end,w,h))


