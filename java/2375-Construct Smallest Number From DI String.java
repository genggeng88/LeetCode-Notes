class Solution {
    public String smallestNumber(String pattern) {
        int n = pattern.length();
        String result = "";
        Stack<Integer> store = new Stack<>();

        for(int i =0; i<n; i++){
            if(pattern.charAt(i)=='I' && store.empty()){
                result += Integer.toString(i+1);
                if (i==n-1){
                    result += Integer.toString(n+1);
                }
            }
            else if(i==n-1 && pattern.charAt(i)=='D'){
                store.add(i+1);
                store.add(i+2);
                while(!store.empty()){
                    result += Integer.toString(store.pop());
                }
            }
            else if(pattern.charAt(i)=='D'){
                store.add(i+1);
            }
            else{
                store.add(i+1);
                while(!store.empty()){
                    result += Integer.toString(store.pop());
                }
                if (i==n-1){
                    result += Integer.toString(n+1);
                }
            }
        }
        return result;
    }
}