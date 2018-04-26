# https://leetcode.com/problems/merge-two-binary-trees/description/

# Definition for a binary tree node.
# class TreeNode
#     attr_accessor :val, :left, :right
#     def initialize(val)
#         @val = val
#         @left, @right = nil, nil
#     end
# end

# @param {TreeNode} t1
# @param {TreeNode} t2
# @return {TreeNode}
def merge(t1, t2)
  if t1 && t2
    TreeNode.new(t1.val + t2.val)
  elsif t1 || t2
    t1 ? TreeNode.new(t1.val) : TreeNode.new(t2.val)
  else
    nil
  end
end

def merge_trees(t1, t2)
  t3 = merge(t1,t2)
  if t1 && t2
    t3.left = merge_trees(t1.left, t2.left)
    t3.right = merge_trees(t1.right, t2.right)
  elsif t1 || t2
    if t1
      t3.left = merge_trees(t1.left, t2)
      t3.right = merge_trees(t1.right, t2)
    else
      t3.left = merge_trees(t1, t2.left)
      t3.right = merge_trees(t1, t2.right)
    end
  end
  t3
end

def merge_trees2(t1, t2)
  return t1 if !t2
  return t2 if !t1
  root = TreeNode.new(nil)
  root.val = t1.val + t2.val
  root.left = merge_trees(t1.left, t2.left)
  root.right = merge_trees(t1.right, t2.right)
  root
end