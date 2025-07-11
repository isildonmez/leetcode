// https://leetcode.com/problems/two-sum/
package problems

func TwoSum(nums []int, target int) []int {
	numToIdx := make(map[int]int)
	for i, num := range nums {
		complement := target - num
		if idx, exists := numToIdx[complement]; exists {
			return []int{idx, i}
		}
		numToIdx[num] = i
	}
	return []int{}
}
