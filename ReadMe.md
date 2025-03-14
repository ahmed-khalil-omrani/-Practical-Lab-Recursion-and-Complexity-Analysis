# 📚 Recursion Exercises README


## 📝 Exercises Overview
1. **💰 The Recursive Cashier (Direct Recursion)**
   - **Problem**: Given an amount \( N \) and coin denominations {1, 5, 10, 25, 50, 100}, compute the minimum number of coins needed.
   - **Tasks**: 
     - Implement `minCoins(N, coins)`.
     - Analyze time complexity and discuss limitations of recursion.
     - Optimize with memoization.

2. **🦠 Virus Spread (Head Recursion)**
   - **Problem**: Calculate the number of infected computers after \( N \) hours, starting with \( P \) infected computers.
   - **Tasks**:
     - Implement `virusSpread(N, P)`.
     - Determine time complexity.
     - Convert to an iterative approach and compare efficiency.

3. **🔢 The Tail-Recursive Factorial (Tail Recursion)**
   - **Problem**: Optimize factorial calculation using tail recursion.
   - **Tasks**:
     - Implement a tail-recursive factorial function.
     - Compare with a non-tail-recursive version.
     - Analyze complexity and memory efficiency of tail recursion.

4. **🧮 Pascal’s Triangle (Nested Recursion)**
   - **Problem**: Compute values of Pascal's Triangle using nested recursion.
   - **Tasks**:
     - Implement `pascal(n, k)`.
     - Analyze complexity and propose an iterative solution.
     - Print Pascal’s Triangle up to \( n = 5 \).

5. **📁 File System Depth (Tree Recursion)**
   - **Problem**: Compute the maximum depth of a nested directory structure.
   - **Tasks**:
     - Implement `maxDepth(fs)`.
     - Analyze complexity and compare with an iterative BFS approach.

6. **📞 Two-Way Communication (Indirect Recursion)**
   - **Problem**: Simulate a conversation between a caller and receiver using indirect recursion.
   - **Tasks**:
     - Implement mutually recursive functions `callerNo` and `receiverNo`.
     - Print the conversation simulation.

## 🎁 Bonus Challenge
- **🏰 The Towers of Hanoi (Optimization & Complexity)**
  - **Problem**: Move \( N \) disks from peg A to peg C using peg B, minimizing moves.
  - **Tasks**:
    - Implement `hanoi(N, A, B, C)`.
    - Prove the minimum number of moves is \( O(2^N - 1) \).
    - Implement a memoized version and analyze performance.


## 🔑 Key Takeaways
- Recursion is a powerful technique but requires optimization to avoid inefficiencies.
- Tail recursion improves space complexity and can prevent stack overflow.
- Tree recursion can effectively model hierarchical structures like file systems.
- Memoization can significantly enhance performance by storing computed results.
- Indirect recursion can model real-world interactions, such as phone conversations.

