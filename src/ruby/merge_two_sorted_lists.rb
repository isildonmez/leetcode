class ListNode
  attr_accessor :val, :next
  def initialize(val)
      @val = val
      @next = nil
  end
end

def merge_two_lists(l1, l2)
  return l2 if l1.nil?
  return l1 if l2.nil?
  return nil if l1.nil? && l2.nil?
  current1 = l1
  current2 = l2
  result = ListNode.new(nil)
  head = result
  until current1.nil? || current2.nil?
    unless head.val.nil?
      head.next = ListNode.new(nil)
      head = head.next
    end
    min_val = [current1.val, current2.val].min
    head.val = min_val
    current1.val < current2.val ? current1 = current1.next : current2 = current2.next
  end
  list = current1.nil? ? current2 : current1
  until list.nil?
    head.next = ListNode.new(list.val)
    list = list.next
    head = head.next
  end
  result
end

def merge_two_lists2(l1, l2)
  headNode = ListNode.new(nil)
  tail = headNode
  while (l1 && l2)
    if (l1.val < l2.val)
      tail.next = l1
      l1 = l1.next
    else
      tail.next = l2
      l2 = l2.next
    end
    tail = tail.next
  end

  tail.next = l1 ? l1 : l2
    headNode = headNode.next
  return headNode
end