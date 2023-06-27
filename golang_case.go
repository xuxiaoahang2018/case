package main

import (
	"fmt"
	"strings"
)

func test(arr string) string {
	resultList := []string{}
	arrLen := len(arr)

	for i := 0; i < arrLen; i++ {
		if isDigit(arr[i]) {
			tempStr := string(arr[i])
			for k := i + 1; k < arrLen; k++ {
				if isDigit(arr[k]) {
					tempStr += string(arr[k])
				}
				if arr[k] == '.' {
					if !strings.Contains(tempStr, ".") {
						tempStr += string(arr[k])
					} else {
						resultList = append(resultList, tempStr)
						break
					}
				}
				if isLetter(arr[k]) || k == arrLen-1 {
					resultList = append(resultList, tempStr)
					break
				}
			}
		}
	}

	if len(resultList) == 0 {
		return ""
	}

	for i := 0; i < len(resultList); i++ {
		if resultList[i][len(resultList[i])-1] == '.' {
			resultList[i] = resultList[i][:len(resultList[i])-1]
		}
	}

	n := len(resultList)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if len(resultList[j]) > len(resultList[j+1]) {
				resultList[j], resultList[j+1] = resultList[j+1], resultList[j]
			}
		}
	}

	return resultList[len(resultList)-1]
}

func isDigit(char byte) bool {
	return char >= '0' && char <= '9'
}

func isLetter(char byte) bool {
	return (char >= 'a' && char <= 'z') || (char >= 'A' && char <= 'Z')
}

func testCase() {
	// 单元测试
	if test("1a1agf1234.52.344.8671.601.3921") != "601.3921" {
		fmt.Println("测试未通过")
		return
	}
	if test("fec74a32.a13t23.a21s6t66z16.a1.t42t3.a4a4a4c41b1") != "41" {
		fmt.Println("测试未通过")
		return
	}
	if test("12345.1.234.23") != "12345.1" {
		fmt.Println("测试未通过")
		return
	}
	if test("12345.1.234.23...") != "12345.1" {
		fmt.Println("测试未通过")
		return
	}
	if test("...12345.1.234.23...") != "12345.1" {
		fmt.Println("测试未通过")
		return
	}
	if test("aavvasdsad") != "" {
		fmt.Println("测试未通过")
		return
	}
	fmt.Println("测试通过")
}

func main() {
	testCase()
}
