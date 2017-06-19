i = 0

class Header:
	def __init__(self, weight, content=""):
		self.weight = weight
		self.content = content

class Node:
	def __init__(self, header, children=[]):
		assert(isinstance(header, Header))
		self.header = header
		self.children = children

	def append(self, child):
		assert(isinstance(child, Node))
		self.children.append(child)

	def to_str(self):
		s = self.header.content
		for child in self.children:
			s += "\n" + ("\t"*child.header.weight) + child.to_str()

		return s

# def treeify(headers):
# 	def treeify_rec(headers, weight, parent):
# 		global i

# 		while (i < len(headers) and
# 			headers[i].weight == weight):

# 			child = Node(headers[i])
# 			i += 1
# 			treeify_rec(headers=headers, weight=weight+1, parent=child)
# 			parent.append(child=child)

# 	header = Header(0)
# 	root = Node(header)
# 	treeify_rec(headers=headers, weight=1, parent=root)

# 	return root

def treeify(headers):
	def treeify_rec(headers, weight):
		global i

		children = []

		while (i < len(headers) and
			headers[i].weight == weight):

			i += 1

			child = Node(headers[i-1],
				treeify_rec(headers=headers, weight=weight+1))

			children.append(child)

		return children

	return Node(Header(0), treeify_rec(headers=headers, weight=1))

def main():
	headers = [Header(1, "a"),
		Header(2, "b"),
		Header(3, "c"),
		Header(4, "d"),
		Header(4, "d"),
		Header(5, "e"),
		Header(3, "C"),
		Header(3, "C"),
		Header(4, "D"),
		Header(5, "E")]

	root = treeify(headers=headers)

	print root.to_str()

	return root

if __name__ == "__main__":
	main()
