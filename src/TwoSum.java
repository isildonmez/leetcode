import java.util.HashMap;
import java.util.Map;

public class TwoSum{
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            if (!map.containsKey(nums[i])){
                map.put(nums[i], i);
            }
            if (map.containsKey(target - nums[i]) && i != map.get(target - nums[i])) {
                return new int[]{map.get(target - nums[i]), i};
            }
        }
        return null;
    }

    public static void main(String[] args) {
        TwoSum testing = new TwoSum();
        int[] hums = new int[] {3, 3};
        int target = 6;
        int[] result = testing.twoSum(hums, target);
        System.out.println(result[0] + " " + result[1]);
    }
}

