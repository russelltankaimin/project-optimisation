import unittest
from node import TreeNode
from mcts import MonteCarlo

class TestPolicyValue(unittest.TestCase):

	def test_choice_is_correct(self):
		montecarlo = MonteCarlo(TreeNode(0))
		montecarlo.child_finder = self.child_finder

		montecarlo.simulate(1, 1, 50)

		chosen_node = montecarlo.make_choice()
		self.assertIs(chosen_node.state, 1)

		# exploratory_node = montecarlo.make_exploratory_choice()
		# self.assertTrue(exploratory_node != None)

	def child_finder(self, node, montecarlo):
		node.add_children(self.build_children(node))
		node.update_win_value(node.state)

	def build_children(self, node):
		children = []

		for i in range(2):
			child = TreeNode(node.state or (1 if i == 1 else -1))
			child.policy_value = .90 if i == 1 else 0.10
			children.append(child)

		node.update_win_value(0)

		return children
