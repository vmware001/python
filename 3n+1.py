def main():
    maxstep=0
    for n in range(1,100000):
        step = 0  # 初始化步数

        while n != 1:
            if n % 2 == 0:
                n = n // 2  # 如果是偶数，除以 2
            else:
                n = 3 * n + 1  # 如果是奇数，执行 3n + 1
            print(n)  # 输出当前的 n
            step += 1  # 步数加 1
        print("step:", step)  # 输出总步数
        if(step>maxstep):
            maxstep=step
    print("maxstep:",maxstep)

if __name__ == "__main__":
    main()