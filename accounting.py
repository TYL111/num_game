import json

#檔案位置

class file:
    def __init__(self,file_address = "./accounting.json"):
        self.file_address = file_address
        self.account_record = []
    #新增紀錄
    def add_record(self,date,item,cost,category):
        record = {
            "date":f"{date}",
            "item":f"{item}",
            "cost":f"{cost}",
            "category":f"{category}"
        }
        self.account_record.append(record)

    #寫入json
    def save_to_json(self,index):
        with open(self.file_address,"w") as f:
            json.dump(index,f,indent=4)

    #讀取json
    def load_record(self):
        try:
            with open(self.file_address,"r") as f:
                self.account_record = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            self.account_record = []

class fun():
    def __init__(self,file_manager):
        self.file_manager = file_manager

    #輸入新資料
    def input_new_accounting(self):
        run = True
        while run:
            date = input("DATE(YYYY-MM-DD):")
            item = input("ITEM:")
            cost = input("COST:")
            category = input("CATEGORY:")
            if not date or not item or not cost or not category:
                print("error:input error")
            else:
                self.file_manager.load_record()
                self.file_manager.add_record(date,item,cost,category)
                self.file_manager.save_to_json(self.file_manager.account_record)
            exit_or_not = input("Do you want to exit?(y/n)")
            while not exit_or_not in ["y","n"]:
                print("please enter y or n")
            if exit_or_not == "y":
                run = False

    #搜尋功能
    def search(self):
        sum = 0
        self.file_manager.load_record()
        search_type = input("date / category/all:")
        if search_type == "date":
            search_by_date = input("Search by month(YYYY-MM) or date(YYYY-MM-DD):")
            print("\n\n")
            for x in self.file_manager.account_record:
                if search_by_date in x["date"]:
                    print(x["date"],x["item"],x["category"],"$"+x["cost"])
                    sum += int(x["cost"])
        elif search_type == "category":
            search_by_category = input("Search by category:")
            print("\n\n")
            for x in self.file_manager.account_record:
                if x["category"] == search_by_category:
                    print(x["date"],x["item"],x["category"],"$"+x["cost"])
                    sum += int(x["cost"])
        elif search_type == "all":
            print("\n\n")
            for x in self.file_manager.account_record:
                print(x["date"],x["item"],x["category"],"$"+x["cost"])
                sum += int(x["cost"])

        else:
            print("error:input error")
            return
        print(f"\ntotle cost: ${sum}\n")

    #刪除功能
    def delete_record(self):
        new_record = []
        self.file_manager.load_record()
        delete_target = input("The target you want to del(YYYY-MM-DD ITEM):")
        if not delete_target:
            print("error:missing input")
            return
        delete_target = delete_target.split()
        if len(delete_target) != 2:
            print("error:please provide both date and item")
            return
        new_record = [record for record in self.file_manager.account_record if not (record["date"] == delete_target[0] and record["item"] == delete_target[1])]
        if len(new_record) == len(self.file_manager.account_record):
            print("error:not found")
            return
        else:
            self.file_manager.account_record = new_record
            self.file_manager.save_to_json(self.file_manager.account_record)

# main function
file_manager = file()
app = fun(file_manager)
while True:
    fun_select = input("(add/search/remove/exit):")
    if fun_select == "add":
        app.input_new_accounting()
    elif fun_select == "search":
        app.search()
    elif fun_select == "remove":
        app.delete_record()
        print("removed!")
    elif fun_select == "exit":
        break
    else:
        print("error")