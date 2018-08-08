# https://leetcode.com/problems/maximum-depth-of-binary-tree/description/

def max_depth(root)
	return 0 unless root

	depth_right = max_depth(root.right)
	depth_left = max_depth(root.left)

	[depth_left, depth_right].max + 1
end
