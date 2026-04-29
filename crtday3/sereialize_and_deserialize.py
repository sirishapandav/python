class Codec:
    def serialize(self, root):
        res = []
        def preorder(root):
            if root is None:
                res.append("N")
                return
            res.append(str(root.val))
            preorder(root.left)
            preorder(root.right)
        preorder(root)
        return ",".join(res)
    def deserialize(self, data):
        data = data.split(",")
        self.i = 0
        def preorder():
            if data[self.i] == "N":
                self.i+=1
                return None
            root = TreeNode(int(data[self.i]))
            self.i+=1
            root.left = preorder()
            root.right = preorder()
            return root
        return preorder()
