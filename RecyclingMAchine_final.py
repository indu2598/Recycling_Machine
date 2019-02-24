class RecyclableItems:
    def __init__(self):
            self.product_item = {'Can':0.10, 'Bottle':0.54, 'Paper':0.32}
            self.typeOfItem = "unknown"
    
    def is_valid_product(self,product):
        return (product.title() in self.product_item.keys())
           

class RecyclingMachine(RecyclableItems):

    def __init__(self):
        super().__init__()
        self.name = "Recycling Machine"
        self.type = "Crusher"
        self.list_of_items = []

    def select_product(self):
        product = input(f"Please select a product: {set(self.product_item.keys())} and Stop to finish:")
        return product
    
    def accept_product(self,product,count):
        c = 0
        print(f"Please place {count} {product} into machine.")
        for i in range(count):
            (self.list_of_items).append(product)
            print(f"{product} Accepted")
            c+= 1
        return c

    def payout(self,product,c):
        final_dict[product] = {c:c*(self.product_item[product])}
        print(f"You have added {c} {product}\'s for Rs.{list(final_dict[product].values())}")
        

    def print_receipt(self):
        print("--------FINAL RECEIPT--------")
        total_item = 0
        total_price=0
        for x,y in final_dict.items():
            for i, j in y.items():
                print(f"{i}{x}\'s ----> {j}")
                total_item+=i
                total_price+=j
        print(f"Total Items : {total_item}")
        print(f"Amount Paid : {total_price}")
        print("Thank you for recycling...!")


final_dict = {}
def run():
    vm = RecyclingMachine()
    next_customer = True
    while next_customer:
        pro_name = vm.select_product()
        pro_valid =vm.is_valid_product(pro_name)
        
        if pro_valid == True:
            count = int(input(f"How many {pro_name}\'(s) do you have?:"))
            c = vm.accept_product(pro_name,count)
            vm.payout(pro_name,c)
        elif pro_name.title() == 'Stop':
            vm.print_receipt()
            final_dict.clear()
            while True:
                answer = input("(N)ext customer, or (Q)uit?")
                answer = answer.upper()
                if answer == "N":
                    break
                elif answer == "Q":
                    exit()
                else:
                    print("Invalid Response")
        else:
            print("You are putting Wrong Item..!")

run()