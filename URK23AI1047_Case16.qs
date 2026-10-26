// 25DC2012 - IA3 - Case 16: Grover's Search Algorithm, marked item |01>
// Qubit order follows the handout: |q[0] q[1]>, so |01> means q[0]=0, q[1]=1.

operation Main() : Result[] {
    // >>> REPLACE with the real register numbers of ALL team members <<<
    Message("URK23AI1047");
    // Number of Grover iterations: 1 for Experiment A, change to 2 for Experiment B.
    let iterations = 1;

    return Search(iterations);
}

// Full circuit: H on both -> (oracle -> diffusion) x iterations -> measure both.
operation Search(iterations : Int) : Result[] {
    use q = Qubit[2];

    // Uniform superposition over |00>, |01>, |10>, |11>.
    H(q[0]);
    H(q[1]);

    for _ in 1..iterations {
        Oracle(q);
        Diffusion(q);
    }

    // Measure q[0], q[1] (printed in that order) and reset both qubits to |0>.
    return MResetEachZ(q);
}

// Oracle marking |01>: flips the sign (phase) of that state only.
operation Oracle(q : Qubit[]) : Unit {
    X(q[0]);              // turn |01> into |11>
    CZ(q[0], q[1]);       // CZ gives -1 phase to |11> only
    X(q[0]);              // undo the first X
}

// Diffusion operator (inversion about the mean).
operation Diffusion(q : Qubit[]) : Unit {
    H(q[0]);
    H(q[1]);
    X(q[0]);
    X(q[1]);
    CZ(q[0], q[1]);       // phase flip on |11> (which is |00> in the original frame)
    X(q[0]);
    X(q[1]);
    H(q[0]);
    H(q[1]);
}
