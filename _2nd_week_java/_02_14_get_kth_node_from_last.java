package _2nd_week_java;

/*
 * Q. 링크드 리스트의 끝에서 K번째 값을 반환하시오.
 */
public class _02_14_get_kth_node_from_last {
    public static class Node {
        int data;
        Node next;
        public Node(int data) {
            this.data = data;
        }
    }

    public static class LinkedList {
        Node head;

        public LinkedList(int value) {
            head = new Node(value);
        }

        public void add(int value) {
            Node curr = head;
            while (curr.next != null) {
                curr = curr.next;
            }
            curr.next = new Node(value);
        }

        public Node get_kth_node_from_last(int k) {
            Node slow = this.head;
            Node fast = this.head;
            for (int i=0; i<k; i++) {
                fast = fast.next;
            }
            while (fast != null) {
                slow = slow.next;
                fast = fast.next;
            }
            return slow;
        }
    }

    public static void main(String[] args) {
        LinkedList linkedList = new LinkedList(6);
        linkedList.add(7);
        linkedList.add(8);
        System.out.println(linkedList.get_kth_node_from_last(2).data); // 7이 나와야 합니다!
    }
}
