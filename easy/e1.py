class Solution {
    public int[] twoSum(int[] nums, int target) {
        
        
        HashMap<Integer,Integer> keys = new HashMap<Integer,Integer>();
        int num1=0, num2=0;
       
        for(int i = 0; i < nums.length; i++)
        {
         
            if(keys.containsKey(nums[i]))
            {
                num1 = i;
                num2 = keys.get(nums[i]);
            }

            else
            {
                int diff = target - nums[i];     
                keys.put(diff, i);
            }
        }
        
        return new int[] {num1, num2};

    }
}
