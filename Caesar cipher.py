#There may still be some problems with this document, but I'm working on it------------2023/9/1
#Welcome to use it!

def change(code,key):
    code = code.lower()
    m = ord(code)
    if m >= 97 and m <= 122:
        m = 97 + ((m - 97) + key) % 26
        return chr(m)

def encrypt(code,key):
    code_new = ""
    for s in code:
        code_new += change(s,key)
    print(code_new)
    return code_new

def decrypt(code,key):
    code_new = ""
    for s in code:
        m = ord(s) - key
        if m < 97:
            m += 26
        code_new += chr(m)
    print(code_new)
    return code_new

def main():
    print("请选择数字1 or 2：")
    print("1： 加密码")
    print("2： 解密码")
    choice = input()
    if choice == "1":
        code = input("要加密码的内定：")
        key = int(input("请输入偏移位数："))
        encrypt(code,key)
    elif choice == "2":
        code = input("要解密码的内定：")
        key = int(input("输入偏移位数："))
        decrypt(code,key)
    else:
        print("这不是合法的选择\n请重试！！！！")

if __name__ == "__main__":
    main()
