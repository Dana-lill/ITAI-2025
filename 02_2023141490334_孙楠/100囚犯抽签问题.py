import numpy as np
import matplotlib.pyplot as plt
import time

def simulate_random(n, k, trials):
    """�������ģ��"""
    successes = 0
    for _ in range(trials):
        boxes = np.random.permutation(n)
        all_found = True
        for prisoner in range(n):
            found = False
            choices = np.random.choice(n, k, replace=False)
            for choice in choices:
                if boxes[choice] == prisoner:
                    found = True
                    break
            if not found:
                all_found = False
                break
        successes += 1 if all_found else 0
    return successes / trials

def simulate_loop(n, k, trials):
    """ѭ������ģ��"""
    successes = 0
    cycle_lengths = []
    for _ in range(trials):
        boxes = np.random.permutation(n)
        all_found = True
        for prisoner in range(n):
            found = False
            current = prisoner
            for step in range(k):
                if boxes[current] == prisoner:
                    found = True
                    cycle_lengths.append(step + 1)
                    break
                current = boxes[current]
            if not found:
                all_found = False
                break
        successes += 1 if all_found else 0
    return successes / trials, cycle_lengths

def main():
    """������"""
    n = 100
    k = 50
    trials = 10000
    
    print(f"ģ������: {n}����, ÿ��{k}�γ���, {trials}��ʵ��")
    
    # �������
    start = time.time()
    random_rate = simulate_random(n, k, trials)
    print(f"������Գɹ���: {random_rate:.4f} (��ʱ: {time.time()-start:.2f}��)")
    
    # ѭ������
    start = time.time()
    loop_rate, cycle_lengths = simulate_loop(n, k, trials)
    print(f"ѭ�����Գɹ���: {loop_rate:.4f} (��ʱ: {time.time()-start:.2f}��)")
    
    # ѭ�����ȷֲ�
    plt.hist(cycle_lengths, bins=50, alpha=0.7, color='blue')
    plt.axvline(x=50, color='red', linestyle='--', label='50�γ�������')
    plt.xlabel('ѭ������')
    plt.ylabel('Ƶ��')
    plt.title('ѭ�������µ�ѭ�����ȷֲ�')
    plt.legend()
    plt.show()
    
    # ��ͬ�����µĳɹ���
    sizes = [50, 100, 200]
    attempts = [25, 50, 75]
    results = []
    
    for size in sizes:
        for attempt in attempts:
            if attempt < size//2:
                _, lengths = simulate_loop(size, attempt, 1000)
                success_rate = sum(1 for l in lengths if l <= attempt) / len(lengths)
                results.append((size, attempt, success_rate))
    
    # ���չʾ
    print("\n��ͬ�����µĳɹ���:")
    for size, attempt, rate in results:
        print(f"N={size}, K={attempt}: {rate:.4f}")

if __name__ == "__main__":
    main()




