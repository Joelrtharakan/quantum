# Case 16 – Grover's Search (marked |01>) – Viva Notes

Notation: states are |q[0] q[1]>. |01> means q[0]=0, q[1]=1.

**What does Grover's algorithm do?**
It finds a marked item in an unsorted list of N items using about √N oracle calls (classically about N/2 on average). Here N = 4, so 1 oracle call finds the item with certainty.

**Why do 2 qubits give 4 states?**
n qubits span 2^n basis states: |00>, |01>, |10>, |11>. Each state is one list item.

**Why Hadamard gates?**
H on |0> gives (|0>+|1>)/√2. H on both qubits gives an equal superposition of all 4 states, each with amplitude ½, so every item starts with probability ¼. H also appears in the diffusion operator, because it changes basis so that the reflection is about the uniform state.

**How does the |01> oracle work?**
X(q[0]) turns |01> into |11>. CZ(q[0], q[1]) puts a −1 phase on |11> only. The second X(q[0]) turns it back into |01>. So only |01> gets a −1 sign. Probabilities do not change yet, only the phase.

**What does CZ do?**
It applies Z to the target if the control is |1>. Its effect is |11> → −|11>, and it leaves the other three basis states alone.

**What does diffusion do?**
It reflects every amplitude about the average amplitude. After the oracle, the marked amplitude (−½) is below the average (¼). The reflection makes it larger, so it becomes +1 (up to a global sign), and the others become 0. It is built as H, X, CZ, X, H on both qubits.

**Why is 1 iteration optimal for N = 4?**
k = ⌊(π/4)√4⌋ = ⌊π/2⌋ = 1. Geometrically, sin θ = 1/√N = ½, so θ = 30°. Each iteration rotates the state by 2θ = 60°. After k iterations, P(marked) = sin²((2k+1)θ). With k = 1 this is sin²(90°) = 1.

**Why do 2 iterations reduce the probability?**
The second iteration rotates the state a further 60°, past the target, to 150°. P = sin²(150°) = ¼. This is overshoot. Grover's algorithm rotates the state; it does not keep increasing the amplitude.

**What does the histogram show?**
- Experiment A (1000 shots): |01> 1000 times. This is the target found with certainty, as predicted.
- Experiment B (1000 shots): |00> 240, |01> 272, |10> 247, |11> 241. All are roughly 25%, so the target has no advantage.

**Measurement and bit order**
Results are listed as q[0], q[1]. The result `[Zero, One]` means q[0]=0 and q[1]=1, which is |01>. This is the order the handout uses.

**Theory vs a finite-shot simulation**
Theory says the probabilities are exactly 100% and 25%. In a finite run, counts vary randomly. For 1000 shots at p = 0.25 the standard deviation is √(1000·0.25·0.75) ≈ 13.7 counts. So 240 to 272 are all consistent with 250. With 1 iteration the probability is exactly 1, so there is no spread.

**Operation by operation (the code)**
- `Main` – prints the register number(s) with `Message()`, sets `iterations`, and calls `Search`.
- `Search(iterations)` – allocates 2 qubits, applies H to both, repeats Oracle then Diffusion, and measures with `MResetEachZ` (which also resets the qubits before they are released).
- `Oracle` – X, CZ, X marks |01>.
- `Diffusion` – H, X, CZ, X, H on both qubits.

**Limitations of this demo**
- N = 4 is too small for a real speed-up.
- It is an ideal noise-free simulation, with no hardware errors.
- The oracle already knows the answer, so this only demonstrates the circuit.

**Possible follow-up questions**
- What would the oracle for |10> look like? (X on q[1] instead of q[0].)
- What happens with 3 iterations? (sin²(210°) = ¼ again.)
- How many iterations for N = 16? (⌊(π/4)·4⌋ = 3.)
- Does the oracle change the measurement probabilities? (No, only phases.)
- Is Grover's speed-up exponential? (No, quadratic.)
