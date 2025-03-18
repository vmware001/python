import time

while True:
    startTime = time.time()
    time.sleep(1)
    endTime = time.time()
    diff = endTime - startTime - 1
    print(f"{diff:.8f}")  # 使用 f-string 格式化输出，保留 8 位小数
