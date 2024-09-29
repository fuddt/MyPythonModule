import time
def codetimer(code,sleep=1):
    start = time.perf_counter()
    time.sleep(sleep)
    
    if callable(code):
        code
    elif type(code) == str:
        exec(code)
    else:
        raise ValueError('関数かコードのテキストを渡してください。')
        
    end = time.perf_counter()
    result = end - start

    print(result)
