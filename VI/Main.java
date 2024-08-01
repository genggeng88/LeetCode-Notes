// Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
//  
// Example 1:
// Input: nums = [1,1,1,2,2,3], k = 2
// Output: [1,2]
// Example 2:
// Input: nums = [1], k = 1
// Output: [1]
import java.util.*;

class Solution {
    public List<Integer> frequent(int[] nums, int k) {
        
        HashMap<Integer, Integer> map = new HashMap<>();
        for (int num : nums) {
            if (map.containsKey(num)) {
                map.put(num, map.get(num)+1);
            }
            else {
                map.put(num, 1);
            }
        }

        List<Integer> result = new ArrayList<>();
        
        for (int i=0; i<k; i++) {
            // System.out.println("map for each iteration: " + map.keySet());
            int maxTimes = 0, maxValue = 0;
            for (Integer ele: map.keySet()) {
                if (maxTimes < map.get(ele)) {
                    maxTimes = map.get(ele);
                    maxValue = ele;
                }
            }
            System.out.println("map: " + map.keySet());
            result.add(maxValue);
            map.remove(maxValue);
            System.out.println("map after remove: " + map.keySet());
        }

        return result;
    }
}


public class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        
        // Define test cases
        int[] test1 = {1,1,1,2,2,3};
        int k1 = 2;
        int[] test2 = {1};
        int k2 = 1;
        
        // Test canJump method
        System.out.println("Test case 1: " + solution.frequent(test1, k1));
        System.out.println("Test case 2: " + solution.frequent(test2, k2));
    }
}
