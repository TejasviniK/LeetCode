class StockSpanner:

    def __init__(self):
        self.index = 0
        self.stack = []

    def next(self, price: int) -> int:
        
        if len(self.stack) == 0 :
            self.stack.append([self.index,price])
            print("stack : ", self.stack)
            self.index += 1
            return 1
        
        while len(self.stack) > 0 and self.stack[-1][1] <= price:
            self.stack.pop()
        print("Stack after pop :", self.stack)

        self.stack.append([self.index,price])
        print("stack : ", self.stack)
        self.index += 1
        
        if(len(self.stack) == 1) :
            return self.stack[0][0] + 1
        
        return (self.stack[-1][0] - self.stack[-2][0])

# Your StockSpanner object will be instantiated and called as such:
obj = StockSpanner()
print(obj.next(31))
print(obj.next(41))
print(obj.next(48))
print(obj.next(59))
print(obj.next(79))
print(obj.next(75))
# print(obj.next(85))



#[100, 80, 60, 70, 60, 75, 85], then the stock spans would be [1, 1, 1, 2, 1, 4, 6]
