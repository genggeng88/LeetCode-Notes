class Solution {
    public int[][] allCellsDistOrder(int rows, int cols, int rCenter, int cCenter) {
        int[][] result = new int[rows*cols][2];
        int idx = 0;
        result[idx][0]=rCenter;
        result[idx][1]=cCenter;
        
        Queue<Node> queue = new LinkedList<>();
        int[] checked = new int[rows*cols];
        queue.add(new Node(rCenter, cCenter));
        checked[rCenter*cols + cCenter] = 1;
       
        while(!queue.isEmpty()){
            Node top = queue.remove();
            if(top.x+1 < rows){
                Node test = new Node(top.x + 1, top.y);
                int index = (top.x+1)*cols + top.y;
                if (checked[index] != 1){
                    queue.add(test);
                    checked[index] = 1;
                    idx++;
                    result[idx][0]=top.x + 1;
                    result[idx][1]=top.y;
                } 
            }
            if(top.x-1 >= 0){
                Node test = new Node(top.x - 1, top.y);
                int index = (top.x-1)*cols + top.y;
                if (checked[index] != 1){
                    queue.add(test);
                    checked[index] = 1;
                    idx++;
                    result[idx][0]=top.x - 1;
                    result[idx][1]=top.y;
                }
            }
            if(top.y-1 >= 0){
                Node test = new Node(top.x, top.y-1);
                int index = (top.x)*cols + top.y-1;
                if (checked[index] != 1){
                    queue.add(test);
                    checked[index] = 1;
                    idx++;
                    result[idx][0]=top.x;
                    result[idx][1]=top.y-1;
                }
            }
            if(top.y+1 < cols){
                Node test = new Node(top.x, top.y+1);
                int index = (top.x)*cols + top.y+1;
                if (checked[index] != 1){
                    queue.add(test);
                    checked[index] = 1;
                    idx++;
                    result[idx][0]=top.x;
                    result[idx][1]=top.y+1;
                }
            }
            
        }
        return result;
    }

    class Node{
        public int x;
        public int y;
        public Node(int x, int y){
            this.x = x;
            this.y = y;
        }
    }
}