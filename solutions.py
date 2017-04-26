import unittest
from collections import Counter


def question1(s, t):
    return not Counter(t) - Counter(s)


def question2(a):
    palindrome = ''
    for x in range(len(a)):
        for y in range(len(a)):
            word = a[x:y+1]
            if is_palindrome(word) and (len(word) > len(palindrome)):
                palindrome = word
    return palindrome

def is_palindrome(a):
    if len(a) > 1:
       return a==a[::-1]
    return False


def question3(G):

    if type(G) != dict or len(G) < 2:
        return 'Invalid Input'

    mst = {}
    visited_vertices = []
    best_edge = None

    visited_vertices.append(G.keys()[0])

    for vertex in G.keys():
        mst[vertex] = []

    while len(visited_vertices) < len(G):
        for vertex in visited_vertices:
            for edge in G[vertex]:
                if not best_edge or edge[1] < best_edge[1]:
                    if edge[0] not in visited_vertices:
                        best_edge = edge
                        vertex_from = vertex
                        vertex_to = edge[0]

        if not best_edge:
            return 'Disconnected Tree'

        mst[vertex_from].append(best_edge)
        mst[vertex_to].append((vertex_from, best_edge[1]))

        visited_vertices.append(vertex_to)

        best_edge = None
        vertex_from = None
        vertex_to = None

    return mst


def question4(T, r, n1, n2):
    ancestor_n1 = n1
    ancestor_n2 = n2

    if len(T) - 1 < n1 or len(T) - 1 < n2:
        return None

    for i, node in enumerate(T):

        if node[ancestor_n1] == 1:
            ancestor_n1 = i

        if node[ancestor_n2] == 1:
            ancestor_n2 = i

        if ancestor_n1 == ancestor_n2:
            return ancestor_n1

    return r


class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def question5(ll, m):
    if ll == None or m == None:
        return None
    count = 0
    finished = False
    current_node = ll
    mth_node = ll

    while not finished:
        if count + 1 > m:
            mth_node = mth_node.next

        if not current_node.next:
            if not (count - m + 1) in range(0, count + 1):
                return 'm is out of list range'
            return mth_node.data

        count += 1
        current_node = current_node.next


Node1 = Node('dog')
Node2 = Node('cat')
Node3 = Node('bear')
Node4 = Node('wolf')
Node5 = Node('eagle')
Node6 = Node('mouse')
Node7 = Node('penguin')
Node8 = Node('lion')
Node1.next = Node2
Node2.next = Node3
Node3.next = Node4
Node4.next = Node5
Node5.next = Node6
Node6.next = Node7
Node7.next = Node8

Node9 = Node('wolf')

class Tests(unittest.TestCase):
    def test_question1(self):
        self.assertTrue(question1('udacity', 'ad'))
        self.assertFalse(question1('racecar', 'catch'))
        self.assertTrue(question1('doodle', 'dolod'))
        self.assertFalse(question1('e', 'elephants'))


    def test_question2(self):
        self.assertEqual(question2('finnif'), 'finnif')
        self.assertEqual(question2('yessir'), 'ss')
        self.assertEqual(question2('iceman'), '')
        self.assertEqual(question2('oillied'), 'illi')


    def test_question3(self):
        self.assertEqual(
            question3({
                'A': [('B', 2)],
                'B': [('A', 2), ('C', 5)],
                'C': [('B', 5)]
            }),
            {
                'A': [('B', 2)],
                'B': [('A', 2), ('C', 5)],
                'C': [('B', 5)]
            }
        )
        self.assertEqual(
            question3({
                'A': [('B', 1)],
                'B': [('A', 1)],
            }),
            {
                'A': [('B', 1)],
                'B': [('A', 1)],
            }
        )
        self.assertEqual(
            question3({
                'A': [('B', 1), ('E', 2)],
                'B': [('A', 1), ('C', 1), ('D', 3)],
                'C': [('B', 1), ('D', 4)],
                'D': [('B', 3), ('C', 4), ('E', 6)],
                'E': [('A', 2), ('D', 6)]
            }),
            {
                'A': [('B', 1), ('E', 2)],
                'C': [('B', 1)],
                'B': [('A', 1), ('C', 1), ('D', 3)],
                'E': [('A', 2)],
                'D': [('B', 3)]
            }
        )


    def test_question4(self):
        self.assertEqual(
            question4([[0, 1, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0]],
                      3,
                      1,
                      4
                     ),
            3
        )
        self.assertEqual(
            question4([[0, 1, 0, 1, 0],
                       [0, 0, 0, 0, 0],
                       [1, 0, 0, 0, 0],
                       [0, 0, 0, 0, 1],
                       [0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0]],
                      1,
                      2,
                      7
                     ),
            None
        )
        self.assertEqual(
            question4([[0, 0, 0, 0, 0, 0],
                       [0, 0, 1, 0, 0, 1],
                       [0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0],
                       [0, 1, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0]],
                      4,
                      5,
                      2
                     ),
            1
        )


    def test_question5(self):
        self.assertEqual(question5(Node1, 3), 'mouse')
        self.assertEqual(question5(Node1, 1), 'lion')
        self.assertEqual(question5(Node1, 0), 'm is out of list range')
        self.assertEqual(question5(Node1, 9), 'm is out of list range')
        self.assertEqual(question5(Node1, 8), 'dog')
        self.assertEqual(question5(Node1, 18), 'm is out of list range')
        self.assertEqual(question5(Node1, -20), 'm is out of list range')
        self.assertEqual(question5(Node1, 5), 'wolf')
        self.assertEqual(question5(None, None), None)
        self.assertEqual(question5(Node9, 1), 'wolf')


if __name__ == '__main__':
    unittest.main()
