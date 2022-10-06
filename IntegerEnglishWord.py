class Solution:
    num_dict = {1: "One", 2: "Two", 3: "Three", 4: "Four",
                5: "Five", 6: "Six", 7: "Seven", 8: "Eight", 9: "Nine"}
    ten_dict = {1: "Ten", 2: "Twenty", 3: "Thirty", 4: "Fourty",
                5: "Fifty", 6: "Sixty", 7: "Seventy", 8: "Eighty", 9: "Ninty"}
    ten_ones = {1: "Eleven", 2: "Twelve", 3: "Thirteen", 4: "Fourteen", 5: "Fifteen",
                6: "Sixteen", 7: "Seventeen", 8: "Eighteen", 9: "Nineteen", 0: "Ten"}
    mid_nam = {1: "Hundred", 2: "Thousand", 3: "Million", 4: "Billion"}

    def numberToWords(self, num: int) -> str:
        num = str(num)
        number_holder = []
        num_str_holder = ""
        if len(num) > 3:
            for i in num[::-1]:
                num_str_holder += i
                if len(num_str_holder) == 3:
                    number_holder.append(num_str_holder)
                    num_str_holder = ""
            if num_str_holder != number_holder[-1]:
                number_holder.append(num_str_holder)
        else:
            number_holder.append(str(num))
        print(number_holder)
        return self.num_nam(number_holder)

    def num_sep(self, num):
        num = str(num)
        if len(num) == 1:
            return self.num_dict[int(num)]
        else:
            if len(num) == 3:
                return self.num_dict[int(num)//10**(2)]+" "+self.mid_nam[1]+" "+self.num_sep(int(num) % 10**(2))
            elif len(num) == 2 and int(num)//10 != 1:
                return self.ten_dict[int(num)//10]+" "+self.num_dict[int(num) % 10]
            elif len(num) == 2 and int(num)//10 == 1:
                return self.ten_ones[int(num) % 10]

    def num_nam(self, num_list):
        fullname = ""
        if len(num_list) == 3:
            for item in num_list:
                fullname += self.num_sep(item)
                if item == num_list[0]:
                    fullname += " "+self.mid_nam[3]+" "
                if item == num_list[1]:
                    fullname += " "+self.mid_nam[2]+" "
        if len(num_list) == 2:
            for item in num_list:
                fullname += self.num_sep(item)
                if item == num_list[0]:
                    fullname += " "+self.mid_nam[2]+" "
        if len(num_list) == 1:
            fullname += self.num_sep(num_list[0])
        return fullname
