## Ch 08.06 Towers of Hanoi
# In the classic problem of the Towers of Hanoi, you have 3 towers and N disks of different sizes
# which can slide onto any tower. The puzzle starts with disks sorted in ascending order of size
# from top to bottom (Le., each disk sits on top of an even larger one). You have the following
# constraints:
#    (1) Only one disk can be moved at a time.
#    (2) A disk is slid off the top of one tower onto another tower.
#    (3) A disk cannot be placed on top of a smaller disk.
# Write a program to move the disks from the first tower to the last using stacks.
##


## Dynamic Programming
# reference : https://github.com/w-hat/ctci-solutions/blob/master/ch-08-recursion-and-dynamic-programming/06-towers-of-hanoi.py
class Tower:
    def __init__(self, name, discs=None):
        self.name = name
        if discs:
            self.discs = discs
        else:
            self.discs = []

    def __str__(self):
        return self.name


def towersOfHanoi(n, ori, buff, dest):
    if n is None:
        n = len(ori.discs)
    if n == 0:
        return

    towersOfHanoi(n-1, ori, dest, buff)
    disc = ori.discs.pop()
    # print("Moving disc {} from {} to {}.".format(disc, ori, dest))
    dest.discs.append(disc)
    towersOfHanoi(n-1, buff, ori, dest)



import unittest

class Test(unittest.TestCase):
    def test_towers_of_hanoi(self):

        tower1 = Tower("Tower1", ["6", "5", "4", "3", "2", "1"])
        tower2 = Tower("Tower2")
        tower3 = Tower("Tower3")

        self.assertEqual(tower1.discs, ["6", "5", "4", "3", "2", "1"])
        self.assertEqual(tower2.discs, [])
        self.assertEqual(tower3.discs, [])

        towersOfHanoi(None, tower1, tower2, tower3)

        self.assertEqual(tower1.discs, [])
        self.assertEqual(tower2.discs, [])
        self.assertEqual(tower3.discs, ["6", "5", "4", "3", "2", "1"])


if __name__ == "__main__":
    unittest.main()

