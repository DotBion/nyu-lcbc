class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> freq = new HashMap<>();
        for(int num: nums) {
            freq.put(num, freq.getOrDefault(num, 0) + 1);
        }
        Queue<Integer> pq = new PriorityQueue<>((n1, n2) -> freq.get(n1) - freq.get(n2));
        freq.keySet().forEach((key) -> {
            pq.add(key);

            if (pq.size() > k) pq.poll();
        });
        int[] ans = new int[k];
        int i = 0;
        while(!pq.isEmpty()){
            ans[i++] = pq.remove();
        }
        return ans;
    }
}
