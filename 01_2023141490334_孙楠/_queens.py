import time
import matplotlib.pyplot as plt

def is_safe(board, row, col):
    """��鵱ǰλ���Ƿ�ȫ"""
    # �����
    for i in range(row):
        if board[i] == col:
            return False
        # ���Խ���
        if abs(board[i] - col) == abs(i - row):
            return False
    return True

def solve_n_queens(n, find_all=True):
    """ʹ�û��ݷ����N�ʺ�����"""
    solutions = []
    board = [-1] * n
    
    def backtrack(row):
        if row == n:
            solutions.append(board[:])
            return
        
        for col in range(n):
            if is_safe(board, row, col):
                board[row] = col
                backtrack(row + 1)
                if solutions and not find_all:
                    return
    
    backtrack(0)
    return solutions

def print_solution(board):
    """��ӡ���̲���"""
    n = len(board)
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if board[row] == col else ". "
        print(line)
    print()

def main():
    """������"""
    n = 0
    while n < 4:
        try:
            n = int(input("���������̴�СN (N��4): "))
            if n < 4:
                print("�������N������ڻ����4")
        except ValueError:
            print("��������Ч������")
    
    find_all = input("������н⣿(y/n): ").lower() == 'y'
    
    start_time = time.time()
    solutions = solve_n_queens(n, find_all)
    end_time = time.time()
    
    print(f"\n�ҵ� {len(solutions)} ����:")
    if n <= 8:  # ����С��ģʱ��ӡ���н�
        for i, sol in enumerate(solutions):
            print(f"�� {i+1}:")
            print_solution(sol)
    else:
        print("����N�ϴ󣬽���ӡ��һ����:")
        print_solution(solutions[0])
    
    print(f"�����ʱ: {end_time - start_time:.4f}��")
    
    # ʵ�������N=4��N=12������ʱ��
    if input("\n�Ƿ�����ʵ�������(y/n): ").lower() == 'y':
        times = []
        sizes = list(range(4, 13))
        for size in sizes:
            start = time.time()
            solve_n_queens(size)
            elapsed = time.time() - start
            times.append(elapsed)
            print(f"N={size}: {elapsed:.4f}��")
        
        plt.plot(sizes, times, 'o-')
        plt.xlabel('Board Size (N)')
        plt.ylabel('Time (seconds)')
        plt.title('N-Queens Problem Time Complexity')
        plt.grid(True)
        plt.show()

if __name__ == "__main__":
    main()
    




