class MinStack {

    class Node {
        private int val;
        private int min;
        private Node next;

        private Node(int val) {
            this.val = val;
            this.next = null;
            this.min = Integer.MAX_VALUE;
        }
    }

    private Node dummy;

    public MinStack() {
        this.dummy = new Node(0);
    }
    
    public void push(int val) {
        if (dummy.next == null) {
            Node curr = new Node(val);
            curr.min = Math.min(dummy.min, val);
            dummy.next = curr;
        }
        else {
            Node tmp = dummy.next;
            Node curr = new Node(val);
            dummy.next = curr;
            curr.next = tmp;
            curr.min = Math.min(tmp.min, val);
        }
    }
    
    public void pop() {
        dummy.next = dummy.next.next;
    }
    
    public int top() {
        return dummy.next.val;
    }
    
    public int getMin() {
        return dummy.next.min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */