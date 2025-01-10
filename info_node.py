# -----------------------------------------------------------------------------------
# Copyright (c) [takayama-76] [2025]
# This software is provided "as is", without any warranty of any kind, express or implied, including but not limited to the warranties of merchantability, fitness for a particular purpose, and noninfringement.
# In no event shall the authors or copyright holders be liable for any claim, damages, or other liability, whether in an action of contract, tort, or otherwise, arising from, out of, or in connection with the software or the use or other dealings in the software.
# -----------------------------------------------------------------------------------

class info_node:
    def __init__(self):
        self.name = "Unknown"  # Member variable name
        self.value = 0  # Member variable value
        self.child_node = []  # Member variable child_node (Reference to child info_node class objects)

    # set_name function: Set the input_name to the name
    def set_name(self, input_name):
        self.name = input_name

    # get_name function: Get the name
    def get_name(self):
        return self.name

    # set_value function: Set the input_value to the value
    def set_value(self, input_value):
        self.value = input_value

    # get_value function: Get the value
    def get_value(self):
        return self.value

    # add_value function: Add the input_value to the value
    def add_value(self, input_value):
        self.value += input_value

    # make_child function: Append a newly created info_node to child_node
    def make_child(self, target_name):
        new_child = info_node()  # Create a new info_node object
        new_child.set_name(target_name)  # Set the name
        self.child_node.append(new_child)  # Add to child node

    # get_name_children function: Return a list of all names in child_node
    def get_name_children(self):
        return [child.get_name() for child in self.child_node]

    # get_sum_value_children function: Return the sum of all values in child_node
    def get_sum_value_children(self):
        return sum(child.get_value() for child in self.child_node)

    # make_descendant function: Add new info_nodes in a parent-child-grandchild hierarchy based on target_name_list
    def make_descendant(self, target_name_list):
        current = self
        for target_name in target_name_list:
            # Check if a child with the given name already exists
            child = next((child for child in current.child_node if child.get_name() == target_name), None)
            if child is None:  # Only create a new child if it does not exist
                current.make_child(target_name)
            # Move to the created or existing child
            current = next(child for child in current.child_node if child.get_name() == target_name)

    # get_name_descendant function: Return a list of all names in child_node, separated by "/" (recursive)
    def get_name_descendant(self):
        result = []

        def dfs(node, prefix):
            result.append(prefix + node.get_name())
            for child in node.child_node:
                dfs(child, prefix + node.get_name() + "/")

        dfs(self, "")
        return result

    # get_sum_value_descendant function: Return the sum of all values in child_node (recursive)
    def get_sum_value_descendant(self):
        total = self.get_value()  # Add the value of the current node

        # Recursively add the sum of values from child nodes
        for child in self.child_node:
            total += child.get_sum_value_descendant()

        return total
        
