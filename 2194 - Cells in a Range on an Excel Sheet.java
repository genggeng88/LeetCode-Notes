class Solution {
    public List<String> cellsInRange(String s) {
        char sr = s.charAt(0), er = s.charAt(3);
        int a = Integer.parseInt(s.charAt(1)+"");
        int b = Integer.parseInt(s.charAt(4)+"");

        List<String> result = new ArrayList<>();

        while(sr<=er){
            int spare = a;
            while(spare<=b){
                result.add(sr+Integer.toString(spare));
                spare++;
            }
            sr++;
        }
        return result;
    }
}