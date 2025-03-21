int subarraySum(vector<int>& nums, int k) {
  int ans = 0;
  int curSum = 0; 
  unordered_map<int, int> map;      
  map[0] = 1;

  for (int num : nums) {
    curSum += num;
    if (map[curSum - k] > 0)
      ans += map[curSum - k];
            
      map[curSum]++;    
  } 

  return ans;
}
