from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.platypus import *
import os, glob
HERE=os.path.dirname(os.path.abspath(__file__)); ROOT=os.path.dirname(HERE)
# ---- EDIT THIS: real team members (name, register number). Max 3 rows. ----
TEAM=[("Joel R Tharakan","URK23AI1047")]
# ---------------------------------------------------------------------------
QS=sorted(glob.glob(os.path.join(ROOT,'*_Case16.qs')))[0]
code=open(QS).read()
OUT=QS.replace('.qs','_Report.pdf')
SHOTS=['1_code','2_output','3_histogram_1_iteration','4_histogram_2_iterations','5_terminal_counts']
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
pdfmetrics.registerFont(TTFont('AU','/System/Library/Fonts/Supplemental/Arial Unicode.ttf'))
pdfmetrics.registerFontFamily('AU',normal='AU',bold='AU',italic='AU',boldItalic='AU')
ss=getSampleStyleSheet()
for k in ss.byName: ss[k].fontName='AU'
B=ParagraphStyle('B',parent=ss['BodyText'],fontSize=10.5,leading=14.5)
H1=ParagraphStyle('H1',parent=ss['Heading1'],fontSize=16,spaceBefore=4)
H2=ParagraphStyle('H2',parent=ss['Heading2'],fontSize=12.5)
C=ParagraphStyle('C',fontName='Courier',fontSize=8.3,leading=10.2)
T=ParagraphStyle('T',parent=B,alignment=1,fontSize=22,leading=28)
CT=ParagraphStyle('CT',parent=B,alignment=1,fontSize=13,leading=19)
def P(t,s=B): return Paragraph(t,s)
def shot(i,t,h):
    for ext in ('png','jpg','jpeg','PNG','JPG'):
        f=os.path.join(ROOT,'screenshots',SHOTS[i]+'.'+ext)
        if os.path.exists(f):
            from reportlab.lib.utils import ImageReader
            w,hh=ImageReader(f).getSize(); W=15*cm; H=min(W*hh/w,(15.5*cm if i==0 else 7.2*cm)); W=H*w/hh
            return KeepTogether([P("Screenshot %d: %s"%(i+1,t.split(': ',1)[-1]),B),Image(f,width=W,height=H)])
    return ph(t,h)
def ph(t,h=5*cm):
    t=Table([[P("<b>[PLACEHOLDER – NOT YET CAPTURED]</b><br/>"+t,B)]],colWidths=[16*cm],rowHeights=[h])
    t.setStyle(TableStyle([('BOX',(0,0),(-1,-1),1,colors.red),('BACKGROUND',(0,0),(-1,-1),colors.HexColor('#fff4f4')),('VALIGN',(0,0),(-1,-1),'MIDDLE'),('ALIGN',(0,0),(-1,-1),'CENTER')]))
    return t
def tbl(rows,w):
    t=Table(rows,colWidths=w); t.setStyle(TableStyle([('FONTNAME',(0,0),(-1,-1),'AU'),('GRID',(0,0),(-1,-1),.6,colors.black),('BACKGROUND',(0,0),(-1,0),colors.HexColor('#e6e6e6')),('FONTSIZE',(0,0),(-1,-1),10),('ALIGN',(1,0),(-1,-1),'CENTER')])); return t
s=[]
# 1 cover
s+=[Spacer(1,2*cm),P("<b>Karunya Institute of Technology and Sciences</b>",CT),P("Division of Data Science and Cyber Security",CT),Spacer(1,.6*cm),
P("25DC2012 – Quantum Computing and Cryptography",CT),P("Internal Assessment III – Quantum Algorithm Project",CT),Spacer(1,1.5*cm),
P("<b>Grover's Search Algorithm</b>",T),P("Case 16 – Marked item |01>",CT),Spacer(1,1.5*cm),
tbl([["Team member name","Register number"]]+[list(m) for m in TEAM],[9*cm,6*cm]),
Spacer(1,.8*cm),P("Case number: 16 &nbsp;|&nbsp; Algorithm: Grover's Search (2 qubits, N = 4) &nbsp;|&nbsp; Language: Q# (Microsoft QDK)",CT),PageBreak()]
# 2 aim
s+=[P("1. Aim and Circuit",H1),
P("<b>Aim.</b> To search an unsorted list of four items (represented by two qubits) with Grover's algorithm and find the marked item |01>, where the state is written |q[0] q[1]>. The program is written in Q#. I run it with one Grover iteration, which is the optimal number for N = 4, and with two iterations, to see how the success probability changes."),
P("<b>Circuit</b> (exactly as specified in the handout): H on both qubits → oracle → diffusion → measure both. The oracle is X(q[0]) → CZ(q[0], q[1]) → X(q[0]). The diffusion operator is H on both → X on both → CZ → X on both → H on both. The grey box is repeated k times: k = 1 for Experiment A and k = 2 for Experiment B."),
Spacer(1,.3*cm),Image(os.path.join(HERE,'circuit.png'),width=16*cm,height=16*cm*0.30),Spacer(1,.2*cm),
P("<i>Figure 1 – Grover circuit for Case 16 (drawn for this report).</i>"),PageBreak()]
# 3 code
s+=[P("2. Q# Source Code",H1),P("File: RegNo_Case16.qs (shown with the iteration count set to 1). To run Experiment B, only the line <font name='Courier'>let iterations = 1;</font> was changed to 2."),Spacer(1,.2*cm),Preformatted(code,C),PageBreak()]
# 4 output
s+=[P("3. Output",H1),
P("<b>Verified simulation results.</b> The program was simulated for 1,000 shots per experiment using the Q# simulator (Python <font name='Courier'>qsharp</font> package) in a terminal. These are the actual counts obtained (Screenshot 5). The probability column is count/1000. Bit order is q[0] q[1]."),
P("Experiment A – 1 Grover iteration (1000 shots)",H2),
tbl([["State","Count","Probability"],["|00>","0","0.0 %"],["|01> (marked)","1000","100.0 %"],["|10>","0","0.0 %"],["|11>","0","0.0 %"]],[5*cm,4*cm,4*cm]),
Spacer(1,.3*cm),P("Experiment B – 2 Grover iterations (1000 shots)",H2),
tbl([["State","Count","Probability"],["|00>","240","24.0 %"],["|01> (marked)","272","27.2 %"],["|10>","247","24.7 %"],["|11>","241","24.1 %"]],[5*cm,4*cm,4*cm]),
Spacer(1,.3*cm),
P("<b>Exact amplitudes</b> (from the simulator's state dump): after 1 iteration the state is −|01> (amplitude −1 on |01>; the global sign has no effect). After 2 iterations the amplitudes are −½ on |00>, +½ on |01>, −½ on |10> and −½ on |11>, so each outcome has probability ¼."),
PageBreak(),
P("<b>Screenshots</b>",H2),
shot(0,"Screenshot 1: Q# source code in VS Code showing Oracle, Diffusion and Search.",4.5*cm),Spacer(1,.2*cm),
shot(1,"Screenshot 2: Program output showing the register number on the first line (terminal run).",4.5*cm),Spacer(1,.2*cm),
shot(2,"Screenshot 3: Histogram, 1 iteration (at least 100 shots).",4.5*cm),Spacer(1,.2*cm),
shot(3,"Screenshot 4: Histogram, 2 iterations (at least 100 shots).",4.5*cm),Spacer(1,.2*cm),
shot(4,"Screenshot 5: Terminal run, 1000 shots each (source of the two result tables above).",4.5*cm),PageBreak()]
# 5 answers
s+=[P("4. Answers to Questions",H1),
P("Q1. Why is 1 iteration best for N = 4, and what happens with 2?",H2),
P("The optimal number of iterations is k = ⌊(π/4)√N⌋. For N = 4: k = ⌊(π/4)·√4⌋ = ⌊π/2⌋ = ⌊1.571⌋ = <b>1</b>."),
P("Geometric view. Let the marked state be |m> and let |s> be the uniform superposition. Then sin θ = 1/√N = 1/2, so θ = 30°. Each Grover iteration (oracle followed by diffusion) rotates the state by 2θ = 60° towards |m>. After k iterations the success probability is sin²((2k+1)θ):"),
tbl([["k","Angle (2k+1)θ","P(marked)"],["0","30°","0.25"],["1","90°","1.00"],["2","150°","0.25"]],[3*cm,5*cm,4*cm]),Spacer(1,.2*cm),
P("With k = 1 the state has rotated exactly onto |01>, so the marked item is measured with certainty. The simulation agrees: 1000 out of 1000 shots gave |01>. A second iteration rotates the state another 60° past |01> (to 150°), so the amplitude of |01> falls back to sin 150° = ½ and its probability to ¼. This is overshoot: amplitude amplification is a rotation, not a monotonic increase, so extra iterations beyond the optimum reduce the success probability. After two iterations the amplitudes are ±½ on all four states, so the state is again uniform in probability. In the experiment the counts were 240, 272, 247 and 241 out of 1000. All of these are close to the ideal 250. The remaining differences are statistical shot noise, since the standard deviation for 1000 shots at p = 0.25 is about 13.7 counts. That is why |01> shows no advantage over the others."),
P("Q2. Role of the oracle and the diffusion operator",H2),
P("<b>Oracle.</b> The oracle recognises the marked state and flips its sign (phase) without changing any probabilities. Here X(q[0]) turns |01> into |11>, CZ gives −1 only to |11>, and the second X(q[0]) turns it back. The result is that |01> has amplitude −½ while the other three have +½. A measurement at this point would still give a uniform distribution, because the sign is not visible in the measurement."),
P("<b>Diffusion operator.</b> Diffusion reflects every amplitude about the average amplitude (inversion about the mean). Because the marked amplitude is below the mean after the oracle, the reflection makes it larger, while the others become smaller. Here it is built as H·X·CZ·X·H, which flips the sign of all states except |00> in the Hadamard basis. After the first iteration the marked amplitude is 1 and the others are 0."),
P("<b>Measurement.</b> After the iterations, measuring both qubits gives the marked item with probability sin²((2k+1)θ), which is 100% after one iteration for N = 4."),PageBreak()]
# 6 conclusion
s+=[P("5. Conclusion and References",H1),
P("<b>Conclusion.</b> I implemented Grover's algorithm for N = 4 in Q# exactly as the handout's recipe and found the marked state |01> with 1000/1000 successes after one iteration. With two iterations the distribution became essentially uniform (about 25% each), which confirms that the algorithm rotates the state and overshoots when run too long. The result shows that the number of iterations must be chosen carefully, k = ⌊(π/4)√N⌋. For a list of only four items this gives no practical speed-up over classical search; the point is to demonstrate amplitude amplification."),
P("<b>References</b>",H2),
P("1. 25DC2012 IA3 Student Handout, Karunya Institute of Technology and Sciences (Case 16)."),
P("2. L. K. Grover, 'A fast quantum mechanical algorithm for database search', Proceedings of the 28th ACM Symposium on Theory of Computing (STOC), 1996, pp. 212–219."),
P("3. M. A. Nielsen and I. L. Chuang, <i>Quantum Computation and Quantum Information</i>, Cambridge University Press, Chapter 6."),
P("4. Microsoft Quantum Development Kit and Q# documentation, https://learn.microsoft.com/azure/quantum/ and https://github.com/microsoft/qdk ."),
P("5. Course lectures 40–41 (Grover's algorithm), 25DC2012.")]
doc=SimpleDocTemplate(OUT,pagesize=A4,leftMargin=2.5*cm,rightMargin=2.5*cm,topMargin=2*cm,bottomMargin=2*cm,title="Case 16 – Grover's Search")
doc.build(s)
