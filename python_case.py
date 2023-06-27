#
#
#
# *   找出1个字符串中最长的数字字符串
#     数字字符串: 数字形式，包括小数，如00050，长度算5,1234.72长度为7，
#     说明: 如果两个数字子串长度一样，则输出最后1个，如果没有，则返回空字符串
#     比如: agf1234.52.344.8671.601.3921，最长数字字符串为601.3921
# *

def test(arr):
    result_list = []
    # 双指针法，当匹配中数字后，往该数字后继续进行匹配，直到遇到字母或者第二个小数点进行退出
    for i in range(len(arr)):
        if arr[i].isdigit():
            temp_str = arr[i]
            for k in range(i+1, len(arr)):
                # 如果是数字，进行字符串拼接
                if arr[k].isdigit():
                    temp_str += arr[k]
                if arr[k] == ".":
                    # 如果是小数点不在字符串中，添加
                    if "." not in temp_str:
                        temp_str += arr[k]
                    else:
                    # 遇到第二个小数点，退出循环，添加数字到list中
                        result_list.append(temp_str)
                        break
                # 如果是字符串，或者已经匹配到末尾，则退出
                if arr[k].isalpha() or k == len(arr) - 1:
                    result_list.append(temp_str)
                    break
    # 如果不包含数字，返回空字符串
    if len(result_list) == 0:
        return ""
    # 把列表中 以 "." 结尾的数字给清除
    lst = [i for i in result_list if i[-1] != "."]
    # 冒泡排序是稳定排序，所以使用冒泡排序对数组内值进行排序，并取出最后一个值，即为最大值
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if len(lst[j]) > len(lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst[-1]


def test_case():
    # 单元测试
    assert test("1a1agf1234.52.344.8671.601.3921") == "601.3921"
    assert test("fec74a32.a13t23.a21s6t66z16.a1.t42t3.a4a4a4c41b1") == "41"
    assert test("12345.1.234.23") == "12345.1"
    assert test("12345.1.234.23...") == "12345.1"
    assert test("...12345.1.234.23...") == "12345.1"
    assert test("aavvasdsad") == ""
    assert test("123456abcxdsx123457") == "123457"
    assert test("987654") == "987654"
    print("测试通过")

if __name__ == "__main__":
    test_case()





