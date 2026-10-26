# 25DC2012 IA3 – Case 16: Grover's Search Algorithm (marked item |01>)

Quantum Computing and Cryptography, Karunya Institute of Technology and Sciences.
Student: Joel R Tharakan, URK23AI1047 (one-person team). Algorithm: Grover's search on 2 qubits (N = 4). Marked state |01>, written |q[0] q[1]>. Language: Q#.

Related files: **COMMANDS.md** (every terminal command) and **Case16_Viva_Notes.md** (viva preparation).

## 1. Project status

| Item | Status |
|---|---|
| Q# program `URK23AI1047_Case16.qs` | Done, with `iterations = 1` |
| Five screenshots in `screenshots/` | Done (names in section 3) |
| Circuit drawing `report_tools/circuit.png` | Done |
| Report | To be written by you (guide in section 4) |
| IBM badge (Part C, 10 marks) | Individual and separate. Complete it yourself. |

## 2. Folder contents

```
Quantum/
├── URK23AI1047_Case16.qs              Q# program                      (SUBMIT)
├── README.md                          this file
├── COMMANDS.md                        all run / output commands
├── Case16_Viva_Notes.md               viva answers (do not submit)
├── screenshots/
│   ├── 1_code.png                     Q# code in VS Code
│   ├── 2_output.png                   terminal run: register number + result
│   ├── 3_histogram_1_iteration.png    VS Code histogram, 1 iteration
│   ├── 4_histogram_2_iterations.png   VS Code histogram, 2 iterations
│   └── 5_terminal_counts.png          terminal run: 1000-shot counts
├── report_tools/
│   └── circuit.png                    circuit diagram
└── .venv/                             Python environment (qsharp)
```

Do not add `qsharp.json`, a `src/` folder, or the VS Code extension's sample or learning files. A `qsharp.json` turns the folder into a Q# project, and a root-level `.qs` file may then be ignored. The single-file setup here needs none of them.

## 3. Exact file names and where each goes in the report

| Report section (handout section 5) | What goes there | File |
|---|---|---|
| 1. Cover page | Name, register number, case 16, algorithm | (text only) |
| 2. Aim and circuit | Circuit drawing | `report_tools/circuit.png` |
| 3. Code | Full Q# program pasted **as text** | `URK23AI1047_Case16.qs` (open it and copy the text) |
| 4. Output, screenshot 1 | Code in the editor | `screenshots/1_code.png` |
| 4. Output, screenshot 2 | Program output with register number (terminal) | `screenshots/2_output.png` |
| 4. Output, screenshot 3 | Histogram, 1 iteration, 1000 shots | `screenshots/3_histogram_1_iteration.png` |
| 4. Output, screenshot 4 | Histogram, 2 iterations, 1000 shots | `screenshots/4_histogram_2_iterations.png` |
| 4. Output, screenshot 5 | Terminal 1000-shot counts (source of the tables) | `screenshots/5_terminal_counts.png` |
| 5. Answers | Q1 and Q2 | Write in your own words (guide: `Case16_Viva_Notes.md`) |
| 6. Conclusion and references | 3 to 5 line conclusion, reference list | Write yourself (see section 4, steps 6 and 7) |

Result tables for section 4, taken from `screenshots/5_terminal_counts.png` (1000 shots each):

| State | 1 iteration | 2 iterations |
|---|---|---|
| \|00> | 0 | 240 |
| \|01> (marked) | 1000 | 272 |
| \|10> | 0 | 247 |
| \|11> | 0 | 241 |

Notes on the screenshots:
- Screenshots 3 and 4 come from the VS Code **Histogram** feature. Screenshots 2 and 5 come from the terminal. Say so in the report captions.
- The VS Code histogram (screenshot 4) is a different random run from the terminal counts, so its bar heights differ slightly. That is normal shot noise.
- VS Code's **Circuit** view is not used, because it collapses the loop into one box and hides the gates. `circuit.png` shows every gate.

## 4. Making the report (Word or Google Docs)

1. Create a new document and add the six headings, in this order: Cover page; Aim and Circuit; Code; Output; Answers; Conclusion and References.
2. **Cover page:** Karunya Institute of Technology and Sciences, Division of Data Science and Cyber Security, 25DC2012 – Quantum Computing and Cryptography, IA3, Case 16, Grover's Search Algorithm, Joel R Tharakan, URK23AI1047.
3. **Aim and circuit:** write the aim in your own words, then insert `report_tools/circuit.png`.
4. **Code:** paste the text of `URK23AI1047_Case16.qs` in a monospace font (Courier or Consolas). Do not use a screenshot for this.
5. **Output:** insert `screenshots/1_code.png`, `2_output.png`, `3_histogram_1_iteration.png`, `4_histogram_2_iterations.png` and `5_terminal_counts.png` in that order, each with a one-line caption. Add the result table from section 3.
6. **Answers:**
   - Q1: show k = ⌊(π/4)√4⌋ = ⌊π/2⌋ = 1, why one iteration is best for N = 4, and what two iterations did and why (see the viva notes).
   - Q2: what the oracle does and what the diffusion operator does, in your own words.
7. **Conclusion and references:** 3 to 5 lines on what you learned, then every source used. Suggested: the 25DC2012 IA3 handout; L. K. Grover, "A fast quantum mechanical algorithm for database search", STOC 1996; Nielsen & Chuang, *Quantum Computation and Quantum Information*, Chapter 6; Microsoft Q# and Quantum Development Kit documentation (learn.microsoft.com/azure/quantum).
8. Export to PDF and save it as `URK23AI1047_Case16_Report.pdf` in this folder.

## 5. Final checks (rubric)
- **Implementation (12):** the circuit matches the recipe, it runs, and the register number prints first (`Message("URK23AI1047")`).
- **Output (8):** the output matches the expected result, with screenshots shown.
- **Questions (5):** Q1 includes k = ⌊(π/4)√4⌋ = ⌊π/2⌋ = 1. Q2 explains the oracle and the diffusion.
- **Write-up (5):** all six sections in order, circuit drawing and code as text, clear writing, sources cited.
- Before submitting, confirm `let iterations = 1;` in the `.qs` file.
- You must be able to explain the code in the viva (read `Case16_Viva_Notes.md`).

## 6. Submission (Google Classroom, IA3)

| File | Who |
|---|---|
| `URK23AI1047_Case16_Report.pdf` (the report you make in section 4) | One per team |
| `URK23AI1047_Case16.qs` | One per team |
| `URK23AI1047_Cert.pdf` + public Credly link | Every student, individually |

## 7. Troubleshooting

- **Run opens a terminal / no Histogram link:** click inside the `.qs` file, check that the status bar (bottom right) says **Q#**, make sure the Quantum Development Kit extension is enabled, and reload the window (Cmd+Shift+P → "Developer: Reload Window"). The links appear above `operation Main`.
- **The histogram doesn't show the register number:** that is normal. The register number appears in the code (screenshot 1) and in the program output (screenshot 2).
- **Screenshot file names have odd spaces:** macOS puts a special space before "PM". Rename from the terminal with a pattern, for example `mv screenshots/*9.05.45*.png screenshots/1_code.png`.
- **Changing the code later:** if you edit the `.qs` file, retake `1_code.png` so they match.
