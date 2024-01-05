class 行李:
    def __init__(self,ID,weight,出發機場,目的地機場,所屬旅客姓名):
        self._ID = ID
        self._weight = weight
        self._出發機場 = 出發機場
        self._目的地機場 = 目的地機場
        self._所屬旅客姓名 = 所屬旅客姓名

    #def 查詢行李資料():

def get_info(self):
        return f"行李 ID: {self._ID}, 重量: {self._weight} 公斤, 出發機場: {self._出發機場}, 目的地機場: {self._目的地機場}, 所屬旅客姓名: {self._所屬旅客姓名}"

# 辅助函数：根据行李 ID 查询行李信息
def query_luggage_info(總行李, luggage_id):
    for luggage in 總行李:
        if luggage._ID == luggage_id:
            return luggage.get_info()
    return f"Luggage with ID {luggage_id} not found."
 
def main():
   
    行李1 = 行李(123, 20, "A機場", "B機場", "小明")
    行李2 = 行李(256, 15, "C機場", "D機場", "小花")
    行李3 = 行李(389, 25, "E機場", "F機場", "小華")

    
    總行李 = [行李1, 行李2, 行李3]
  
    輸入行李ID = int(input("請輸入您的行李ID:"))
    
    result = query_luggage_info(總行李,輸入行李ID)

    # 输出查询结果
    print(result)

if __name__ == "__main__":
    main()



class 登機證:
    def __init__(self,旅客name,登機證編號,time,登機場編號,座位位子,行李件數,行李ID):
        self._旅客name = 旅客name
        self._登機證編號 = 登機證編號
        self._time = time
        self._登機場編號 = 登機場編號
        self._座位位子 = 座位位子
        self._行李件數 = 行李件數
        self._行李ID = 行李ID