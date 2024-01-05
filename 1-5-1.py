class food:

        #建構子是重要的，才能建立屬性參數。self則是目前的，將之前建立的屬性參數設置為一開始的狀態。設定參數可以在之後的一些計算或操作時，更加方便。
    def __init__(self,name,price,保存期限):
        self._name = name
        self._price = price
        self._保存期限 = 保存期限

    def 顯示食物名稱(self):
        return self._name

    def 顯示食物價錢(self):
        return self._price
    
    def 顯示食物保存期限(self):
        return self._保存期限

    
        
food1 = food("牛肉",100,5)
food2 = food("魚",80,30)
food3 = food("羊肉",95,10)
        
print(f"food1的名稱為：{food1.顯示食物名稱()}")
print(f"food1的價錢為：{food1.顯示食物價錢()}")
print(f"food1的保存期限為：{food1.顯示食物保存期限()}")
print(f"food2的名稱為：{food2.顯示食物名稱()}")
print(f"food2的價錢為：{food2.顯示食物價錢()}")
print(f"food2的保存期限為：{food2.顯示食物保存期限()}")
print(f"food3的名稱為：{food3.顯示食物名稱()}")
print(f"food3的價錢為：{food3.顯示食物價錢()}")
print(f"food3的保存期限為：{food3.顯示食物保存期限()}")

   
