#!/usr/bin/env python3
"""WAVE 29: the v10 manuscript build -- the machine-free derivation
integrated. Generates instruments-paper-revised10.txt and
main-article-revised10.txt from the v9 sources via anchored replacements,
each asserted to match exactly once."""

import sys

INS = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v9/"
       "instruments-paper-revised9.txt")
MAIN = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v9/"
        "main-article-revised9.txt")
INS10 = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v10/"
         "instruments-paper-revised10.txt")
MAIN10 = ("/home/z/my-project/channel-supp-augmented/manuscript uploads v10/"
          "main-article-revised10.txt")

src = open(INS).read()
edits = []  # (name, old, new, count)


# ---------------------------------------------------------------- Hunk 1
# Insert the new Proposition (the hand derivation) before the lemma.
PROP = r"""% ---- Second-index widths: the certified qutrit core ----

\begin{proposition}[The cup square on the flag quotient: a hand derivation]
\label{prop:cupsquare}
Keep the notation of the proof of Theorem~\ref{thm:equal-basis}: in
particular $B=\mathrm{Fl}/\langle c\rangle$ is the qutrit flag quotient,
$\kappa\colon B\to B(\mathbb Z/3)$ classifies the regular cover, and
$x=c_1(L)=\kappa^*(u)\in H^2(B;\mathbb Z)$, where $u$ generates
$H^2(B(\mathbb Z/3);\mathbb Z)\cong\mathbb Z/3$. Then
\[
x^2\ \ne\ 0\qquad\text{in }H^4(B;\mathbb Z),
\]
and, more precisely,
\[
H^k(B;\mathbb Z)\ =\ \bigl(\mathbb Z,\ 0,\ \mathbb Z/3,\ \mathbb Z/3,\
\mathbb Z/3,\ \mathbb Z/3,\ \mathbb Z\bigr)\qquad(k=0,\dots,6),
\]
with $x$ generating $H^2$, $x^2$ generating $H^4$, and a discriminant class
generating $H^6$.
\end{proposition}

\begin{proof}
The proof runs the Serre spectral sequence of the Borel fibration
$U(3)\to B\to B\bigl(T^3\rtimes\langle\sigma\rangle\bigr)$ with integral
coefficients, in the spirit of the transgression computations used for the
unordered flag quotients in Ref.~\cite{GuerraJana2025} but lifted to the
integral layer. It is self-contained apart from three classical inputs,
each cited at the point of use: the cohomology of the flag manifold and of
$BU(3)$, Borel's transgression computation, and the cyclic cohomology of
finite modules.

\emph{Step 0 (the homogeneous-space model).} Realise
$\mathrm{Fl}=U(3)/T^3$, where $T^3\subset U(3)$ is the diagonal torus: a
flag is the ordered triple of lines spanned by the columns of a unitary
matrix $g$, and two matrices span the same triple iff they differ by right
multiplication by an element of $T^3$. Under this identification the deck
transformation $c$ is right multiplication by the permutation matrix
$\sigma$ of the cycle $(123)$, which normalises $T^3$; hence the orbits of
$\langle c\rangle$ are exactly the right cosets of the subgroup
$K:=T^3\rtimes\langle\sigma\rangle\subset U(3)$ of cyclic monomial
matrices, and $B=U(3)/K$.

\emph{Step 1 (the fibration and its transgressions).} Let $EU(3)$ be the
contractible free right $U(3)$-space. Left multiplication makes $U(3)$ a
free left $K$-space, and
\[
U(3)\ \longrightarrow\ EU(3)\times_K U(3)\ \overset{\rho}{\longrightarrow}\
BK:=EU(3)/K
\]
is a fibre bundle with fibre $U(3)$ whose total space is homotopy equivalent
to $K\backslash U(3)\cong B$ (the quotient of a free $K$-space is a model
for the associated bundle; the projection $(e,g)\mapsto g$ onto the second
factor has contractible fibres). The map $[e,g]\mapsto eg$ exhibits the
bundle as the pullback of the universal fibration $U(3)\to EU(3)\to BU(3)$
along the map $B\iota\colon BK\to BU(3)$ induced by the inclusion
$\iota\colon K\hookrightarrow U(3)$: indeed $[eg]_{U(3)}=B\iota([e]_K)$, and
on the fibres the induced map is the identity under the canonical
identifications with $U(3)$. By naturality of the Serre spectral sequence,
\[
E_2^{p,q}\ =\ H^p\bigl(BK;\ H^q(U(3);\mathbb Z)\bigr),
\]
the $K$-action on $H^*(U(3);\mathbb Z)=\Lambda(z_1,z_3,z_5)$ (one generator
$z_{2i-1}$ in each degree $2i-1$) being homotopically trivial because $U(3)$
is connected, and the differentials are the pullbacks of the universal
differentials. In the universal fibration the transgression of the primitive
class $z_{2i-1}$ is the universal Chern class $c_i$
\cite{MilnorStasheff1974,HatcherSS}; hence, extended to the exterior part by
the Leibniz rule,
\[
d_2(z_1)=\iota^*c_1,\qquad d_4(z_3)=\iota^*c_2,\qquad d_6(z_5)=\iota^*c_3,
\]
and $d_r=0$ for $r\notin\{2,4,6\}$ by bidegree ($r$ even forces an odd
$q$-degree in the target, where $H^{\mathrm{odd}}(U(3))=0$).

\emph{Step 2 (the cohomology of $BK$).} The semidirect structure splits, so
$BK$ is the Borel construction $EC_3\times_{C_3}BT^3$ and sits in the
fibration $BT^3\to BK\to BC_3$, whose spectral sequence has
$E_2^{p,q}=H^p\bigl(C_3;H^q(BT^3;\mathbb Z)\bigr)$ with
$H^*(BT^3;\mathbb Z)=\mathbb Z[\chi_1,\chi_2,\chi_3]$ (the tautological
characters) and $C_3$ acting by cyclic permutation of the $\chi_i$. The
monomials of each degree $d$ form free $C_3$-orbits of size three, except
the fixed monomials $(\chi_1\chi_2\chi_3)^a$ with $3a=d$; as
$\mathbb Z[C_3]$-modules the degree-$d$ part is a sum of permutation modules
--- which are acyclic for $C_3$ --- plus, when $3\mid d$, one trivial
summand. Now $H^q(BT^3)=0$ for $q$ odd, and in odd $p$-degree the entries
vanish: $H^{\mathrm{odd}}(C_3;\mathbb Z)=0$, permutation modules are
acyclic, and for the trivial summands $H^{\mathrm{odd}}(C_3;\mathbb Z
\text{-trivial})=0$. Consequently every differential lands in a zero group
--- if $r$ is even the target has odd $q$-degree, and if $r$ is odd the
target has odd, positive $p$-degree --- and the sequence collapses. The
invariant theory of the cyclic permutation group gives the free part
\cite{MilnorStasheff1974}
\[
H^*(BK;\mathbb Z)_{\mathrm{free}}\ =\ \mathbb Z[\sigma_1,\sigma_2,\sigma_3]\
\oplus\ \Delta\cdot\mathbb Z[\sigma_1,\sigma_2,\sigma_3],
\]
where $\sigma_i=\sigma_i(\chi)$ are the elementary symmetric functions and
$\Delta=\prod_{i<j}(\chi_i-\chi_j)$ is the discriminant, invariant under the
cyclic group, with $\Delta^2$ equal to the classical discriminant polynomial
in the $\sigma_i$; the module statement follows because in each degree $d$
the orbit sums span the invariant lattice, of rank equal to the number of
orbits, which the monomial count of the displayed module reproduces. The
torsion is one $\mathbb Z/3$ in each bidegree $(2k,6a)$ with $k\ge1$; write
$\tau\in H^2(BK;\mathbb Z)\cong\mathbb Z\sigma_1\oplus\mathbb Z/3\cdot\tau$
for the class of the $(2,0)$-slot, the pullback of $u$ along
$BK\to BC_3$.

\emph{Step 3 (the torsion product rule).} Multiplication with $\tau$ is the
cup product with the generator of $H^2(C_3;\mathbb Z)$, which on the cyclic
cohomology of each module $M$ acts as the standard periodicity map
$H^0(C_3;M)\to H^2(C_3;M)$, $[f]\mapsto[f]$ \cite{Brown1982}. For the
degree-$d$ part $M=\operatorname{Sym}^d$ of $\mathbb Z[\chi]$, one has
$H^2(C_3;M)=M^{C_3}/NM$ with $N$ the norm: the invariant lattice is spanned
by the orbit sums together with the fixed monomial
$(\chi_1\chi_2\chi_3)^{d/3}$, and the norm image by the orbit sums together
with three times that monomial. Hence, for a free class $f$ of degree $d$,
\[
\tau\cdot f\ =\ \bigl[\text{coefficient of }(\chi_1\chi_2\chi_3)^{d/3}
\text{ in }f\ \bmod 3\bigr]\cdot(\text{torsion generator}),
\]
and $\tau\cdot f=0$ when $3\nmid d$. In particular $\tau\sigma_1=
\tau\sigma_2=0$ (degree not divisible by $3$), $\tau\Delta=0$ (the
alternating polynomial $\Delta$ contains no monomial
$\chi_1\chi_2\chi_3$), and $\tau\sigma_1^3=0$ (the coefficient of
$\chi_1\chi_2\chi_3$ in $\sigma_1^3$ is $6$), while $\tau\sigma_3$ is the
generator of the $(2,6)$-slot. Also $\tau^k\cdot\tau^{k'}=\tau^{k+k'}\ne0$;
so $\tau^2$ is a class of order $3$ in
\[
H^4(BK;\mathbb Z)\ \cong\ \mathbb Z\sigma_1^2\ \oplus\ \mathbb Z\sigma_2\
\oplus\ \mathbb Z/3\cdot\tau^2,
\qquad
H^6(BK;\mathbb Z)\ \cong\ \mathbb Z\{\sigma_1^3,\sigma_1\sigma_2,\sigma_3,
\Delta\}\oplus\mathbb Z/3\cdot\tau^3,
\]
and $H^{\mathrm{odd}}(BK;\mathbb Z)=0$.

\emph{Step 4 (the transgression values).} The restrictions to the fibre
$BT^3\subset BK$ are the classical Chern-root identifications
$c_i\mapsto\sigma_i(\chi)$ \cite{MilnorStasheff1974}; hence
$\iota^*c_1=\sigma_1$ (the unique class of the $(0,2)$-slot restricting to
$\sigma_1(\chi)$, up to torsion), $\iota^*c_2=\sigma_2+\varepsilon\tau^2$
and $\iota^*c_3=\sigma_3+\varepsilon'\tau^3$ with
$\varepsilon,\varepsilon'\in\mathbb Z/3$. The constants are pinned by the
splitting $s\colon BC_3\to BK$ of the projection $BK\to BC_3$ (the
semidirect product splits through $\sigma\mapsto(1;\sigma)$): the composite
$BC_3\to BK\overset{B\iota}{\to}BU(3)$ classifies the $K$-representation
$\sigma\mapsto$ the permutation matrix, that is, the regular representation
$1\oplus\omega\oplus\omega^2$ of $C_3$, whose Chern classes in
$H^*(BC_3;\mathbb Z)=\mathbb Z[u]/(3u)$ are $c_1=3u=0$, $c_2=2u^2$,
$c_3=0$. On the other hand $s^*$ annihilates every class of positive fibre
degree --- restricting the fibration $BT^3\to BK\to BC_3$ along $s$ gives
the fibration with fibre a point over $BC_3$, and on the $E_2$ pages the
$q>0$ slots map to zero --- while $s^*(\tau^2)=u^2$ and
$s^*(\tau^3)=u^3$. Hence $2u^2=s^*(\iota^*c_2)=\varepsilon u^2$ and
$0=\varepsilon'u^3$, so
\[
d_2(z_1)=\sigma_1,\qquad d_4(z_3)=\sigma_2+2\tau^2,\qquad
d_6(z_5)=\sigma_3 .
\]

\emph{Step 5 (the run, total degree four).} On
$E_2=H^*(BK;\mathbb Z)\otimes\Lambda(z_1,z_3,z_5)$ the three
transgressions, extended by the Leibniz rule, determine the whole
differential. In total degree four the terms are
$E_2^{4,0}=\mathbb Z\sigma_1^2\oplus\mathbb Z\sigma_2\oplus\mathbb
Z/3\cdot\tau^2$, $E_2^{3,1}=E_2^{1,3}=0$ (odd cohomology of $BK$), and
$E_2^{0,4}=\mathbb Z\cdot z_1z_3$. The incoming images into the $(4,0)$
slot are $d_2(\sigma_1z_1)=\sigma_1^2$ and $d_4(z_3)=\sigma_2+2\tau^2$,
while $d_2(z_1z_3)=\sigma_1z_3\ne0$ kills the $z_1z_3$ class. The class
$\tau^2$ has order three; both $\sigma_1^2$ and $\sigma_2+2\tau^2$ generate
infinite cyclic subgroups --- the latter because its free component
$\sigma_2$ is nonzero --- and a finite-order element never lies in a
subgroup generated by an infinite-order element. Consequently the class of
$\tau^2$ is nonzero in
\[
E_\infty^{4,0}\ =\ \bigl(\mathbb Z\sigma_2\oplus\mathbb Z/3\cdot\tau^2\bigr)
\big/\langle\sigma_2+2\tau^2\rangle\ \cong\ \mathbb Z/3,
\]
and, no other term of total degree four contributing,
$H^4(B;\mathbb Z)\cong\mathbb Z/3$.

\emph{Step 6 (the edge).} The edge homomorphism of the Serre spectral
sequence of a fibration, from the base cohomology to the total-space
cohomology, is the pullback along the projection
\cite{Brown1982,HatcherSS}. Under the identification of the total space
$EU(3)\times_KU(3)$ with $B$, the projection $\rho([e,g])=[e]$ is the
classifying map $\gamma\colon B\to BK$ of the principal $K$-bundle
$U(3)\to U(3)/K=B$. The intermediate cover $\mathrm{Fl}=U(3)/T^3\to B$ is
the quotient of that bundle by the normal subgroup $T^3$, hence is
classified by the composite $\pi\circ\gamma$, where $\pi\colon BK\to BC_3$
is the quotient; since that cover is the regular cover classified by
$\kappa$, we have $\kappa=\pi\circ\gamma$, and therefore
\[
x\ =\ \kappa^*(u)\ =\ \gamma^*(\tau),
\qquad
x^2\ =\ \gamma^*(\tau^2)\ =\ \bigl[\tau^2\bigr]\ \ne\ 0,
\]
the last equality being the surviving class of Step 5. This proves the first
assertion.

\emph{Step 7 (the remaining degrees).} Total degree two: the incoming image
into $(2,0)$ is $d_2(z_1)=\sigma_1$, so
$H^2(B)\cong(\mathbb Z\sigma_1\oplus\mathbb Z/3\cdot\tau)/\langle\sigma_1
\rangle\cong\mathbb Z/3$, generated by the edge image
$\gamma^*(\tau)=x$. Total degree three: on
$E_2^{2,1}=\mathbb Z\sigma_1z_1\oplus\mathbb Z/3\cdot\tau z_1$ one has
$d_2(\sigma_1z_1)=\sigma_1^2\ne0$ while $d_2(\tau z_1)=\tau\sigma_1=0$, and
$E_2^{0,3}=\mathbb Z\cdot z_3$ is killed by $d_4(z_3)\ne0$; hence
$H^3(B)\cong\mathbb Z/3\cdot\langle\tau z_1\rangle$. Total degree five: on
$E_2^{4,1}=\mathbb Z\sigma_2z_1\oplus\mathbb Z\sigma_1^2z_1\oplus\mathbb
Z/3\cdot\tau^2z_1$ the free classes die under $d_2$
($\sigma_1\sigma_2$, $\sigma_1^3$) while $d_2(\tau^2z_1)=\tau^2\sigma_1=0$;
the class $\tau z_3\in E_2^{2,3}$ dies under $d_4(\tau z_3)=
\tau(\sigma_2+2\tau^2)=2\tau^3\ne0$ (Step 3), and $z_5$ dies under
$d_6(z_5)=\sigma_3$; hence $H^5(B)\cong\mathbb Z/3\cdot\langle\tau^2z_1
\rangle$. Total degree six: the incoming images into $(6,0)$ are
$\sigma_1\sigma_2$ and $\sigma_1^3$ (from $d_2$), $2\tau^3$ (from $d_4$),
and $\sigma_3$ (from $d_6$), so
\[
H^6(B;\mathbb Z)\ \cong\ \bigl(\mathbb Z\{\sigma_1^3,\sigma_1\sigma_2,
\sigma_3,\Delta\}\oplus\mathbb Z/3\cdot\tau^3\bigr)\big/\langle\sigma_1^3,\
\sigma_1\sigma_2,\ 2\tau^3,\ \sigma_3\rangle\ \cong\ \mathbb Z\cdot
\langle\Delta\rangle,
\]
the top class being the discriminant, consistently with the rational
cohomology $H^*(B;\mathbb Q)=\mathbb Q\oplus\mathbb Q\cdot\bar\Delta$ read
off from the invariant theory of Step 2. The mixed exterior terms die
transversally ($d_2(z_1z_3)=\sigma_1z_3$, $d_2(z_1z_5)=\sigma_1z_5$,
$d_4(\tau z_1z_3)=2\tau^3z_1$), completing the tuple.
\end{proof}

"""
edits.append(("insert-proposition",
              "% ---- Second-index widths: the machine-certified qutrit core "
              "----\n\n\\begin{lemma}[Cohomology of the qutrit flag quotient "
              "in degrees three and four]",
              PROP + "\\begin{lemma}[Cohomology of the qutrit flag quotient "
              "in degrees three and four]", 1))

# ---------------------------------------------------------------- Hunk 2
# Replace the machine-decision paragraph in the lemma's proof.
OLD2 = r"""The page alone does not decide $d_3^{1,2}$: both the zero map and the
isomorphism of $\mathbb Z/3$ are consistent with every entry derived so far,
including the degree-two and top-degree identifications used in the proof of
Theorem~\ref{thm:equal-basis}. The decision between the two worlds is supplied
by the machine computation recorded in
Remark~\ref{rem:machine-certificate}, certified by its battery and reproduced
by an independent re-implementation: the integral homology of $B$ is
\[
H_k(B;\mathbb Z)\ =\ \bigl(\mathbb Z,\ \mathbb Z/3,\ \mathbb Z/3,\ \mathbb Z/3,\
\mathbb Z/3,\ 0,\ \mathbb Z\bigr)
\qquad(k=0,\dots,6),
\]
whence, by the universal coefficient theorem,
$H^3(B;\mathbb Z)\cong\operatorname{Ext}\bigl(H_2(B),\mathbb Z\bigr)
\cong\mathbb Z/3$ and
$H^4(B;\mathbb Z)\cong\operatorname{Ext}\bigl(H_3(B),\mathbb Z\bigr)
\cong\mathbb Z/3$. A homomorphism $\mathbb Z/3\to\mathbb Z/3$ with nonzero
kernel is zero, so $d_3^{1,2}=0$; then
$\operatorname{coker}d_3^{1,2}=\mathbb Z/3=H^4(B;\mathbb Z)$, consistently.
With $d_3^{1,2}=0$ the class $u^2$ survives to $E_\infty^{4,0}$, and the edge
homomorphism $H^4(\mathbb Z/3;\mathbb Z)\to H^4(B;\mathbb Z)$ --- which is
$\kappa^*$, exactly as in degree two in the proof of
Theorem~\ref{thm:equal-basis} \cite{Brown1982} --- carries it to
$\kappa^*(u^2)=x^2$. Since $H^4(B;\mathbb Z)\cong E_\infty^{4,0}\cong
\mathbb Z/3$, the class $x^2$ generates $H^4(B;\mathbb Z)$."""
NEW2 = r"""The page alone does not decide $d_3^{1,2}$: both the zero map and the
isomorphism of $\mathbb Z/3$ are consistent with every entry derived so far,
including the degree-two and top-degree identifications used in the proof of
Theorem~\ref{thm:equal-basis}. The decision between the two worlds is now
supplied by hand. Proposition~\ref{prop:cupsquare} proves $x^2\ne0$ by an
integral transgression computation, independent of the Cartan--Leray page in
front of us; and $x^2=\kappa^*(u^2)$ is, exactly as in degree two in the
proof of Theorem~\ref{thm:equal-basis} \cite{Brown1982}, the image of $u^2$
under the edge homomorphism $H^4(\mathbb Z/3;\mathbb Z)\to H^4(B;\mathbb Z)$,
which factors as $H^4(\mathbb Z/3;\mathbb Z)\to E_\infty^{4,0}=
\operatorname{coker}d_3^{1,2}\hookrightarrow H^4(B;\mathbb Z)$. A nonzero
image forces a nonzero cokernel, and a homomorphism
$\mathbb Z/3\to\mathbb Z/3$ with nonzero cokernel is zero: $d_3^{1,2}=0$.
Then $H^3(B;\mathbb Z)=\ker d_3^{1,2}\cong\mathbb Z/3$ and
$H^4(B;\mathbb Z)=\operatorname{coker}d_3^{1,2}\cong\mathbb Z/3$, the class
$u^2$ survives to $E_\infty^{4,0}$, and $\kappa^*(u^2)=x^2$ generates
$H^4(B;\mathbb Z)$. The machine computation recorded in
Remark~\ref{rem:machine-certificate} independently certifies the same
conclusion and agrees with the full cohomology tuple of
Proposition~\ref{prop:cupsquare}."""
edits.append(("lemma-proof-decision", OLD2, NEW2, 1))

# ---------------------------------------------------------------- Hunk 3
# Rewrite rem:machine-certificate.
OLD3 = r"""\begin{remark}[The machine certificate behind Lemma~\ref{lem:flag-cohomology}]
\label{rem:machine-certificate}
Lemma~\ref{lem:flag-cohomology} is the one premise of this paper's
second-index results that is not derived by hand; its provenance is recorded
precisely. The integral homology of $B$ was computed from a free
$\mathbb Z/3$-equivariant finite cellulation of $\mathrm{Fl}$ with"""
NEW3 = r"""\begin{remark}[The machine certificate behind Lemma~\ref{lem:flag-cohomology}]
\label{rem:machine-certificate}
Lemma~\ref{lem:flag-cohomology} is derived by hand: the decision input
$x^2\ne0$ is Proposition~\ref{prop:cupsquare}, whose transgression
computation uses only cited classical results (the cohomology of
$U(3)$ and $BU(3)$, Borel's transgression, the cyclic cohomology of finite
modules \cite{MilnorStasheff1974,HatcherSS,Brown1982}) plus a self-contained
invariant-theory step. The machine computation described below is retained
as an independent computational cross-check, and the two routes agree on the
full cohomology tuple. The integral homology of $B$ was computed from a free
$\mathbb Z/3$-equivariant finite cellulation of $\mathrm{Fl}$ with"""
edits.append(("remark-machine-head", OLD3, NEW3, 1))

# the residuals paragraph inside rem:machine-certificate:
OLD3b = r"""Residuals, stated plainly: the cellulation began as one
implementation and has since been independently re-implemented from the
design specification with fresh algorithms at every layer (phase measurement
by column ratios rather than a joint gauge solve, Newton inversions, sign
derivation by constraint propagation from $\partial T=T\partial$, direct
$\mathbb Z/12$ elimination rather than the Chinese-remainder route, and an
incremental subgroup-order computation of the $\mathbb Z/9$ ladder); the two
implementations agree on every input datum, on the full battery, and on the
homology tuple, and the convention data of the construction is forced by the
battery (each falsified variant breaks either the equivariance certificate
or the orbit homology); the geometric identification with the flag quotient
remains warranted by the construction lineage and the battery, not by an
explicit diffeomorphism; and the prime scan is finite, covering $p\le 31$
across the two implementations."""
NEW3b = r"""Residuals, stated plainly. On the hand side, the derivation of
Proposition~\ref{prop:cupsquare} rests on three cited classical inputs ---
Borel's transgression computation for the universal bundle, the Chern-root
restriction, and the cyclic cohomology of finite modules --- and its
arithmetic (the orbit counts, the invariant lattice, the torsion product
rule, the Chern classes of the regular representation, and the
Leibniz-signed page bookkeeping, including the $D^2=0$ coherence check) has
been verified by an exact-integer script whose transcript is part of the
companion repository; the decision logic was moreover validated on the lens
model case $SU(2)\to SU(2)/C_3\to BC_3$, where the same transgression
mechanism ($d_4(z_3)=2u^2$, the second Chern class of the regular
representation) reproduces the classical $H^*(L(3;1);\mathbb Z)=
(\mathbb Z,0,\mathbb Z/3,\mathbb Z)$ with the transfer edge
$\pi^*[L]^*=3[S^3]^*$, and on the two model cases of the earlier audit
(the lens $L(3;1,1,1)$ and $\mathbb{RP}^2\times S^2$, which pin both
directions of the $d_3$-versus-cup-square pattern). On the machine side, the
cellulation began as one
implementation and has since been independently re-implemented from the
design specification with fresh algorithms at every layer (phase measurement
by column ratios rather than a joint gauge solve, Newton inversions, sign
derivation by constraint propagation from $\partial T=T\partial$, direct
$\mathbb Z/12$ elimination rather than the Chinese-remainder route, and an
incremental subgroup-order computation of the $\mathbb Z/9$ ladder); the two
implementations agree on every input datum, on the full battery, and on the
homology tuple, and the convention data of the construction is forced by the
battery (each falsified variant breaks either the equivariance certificate
or the orbit homology); the geometric identification with the flag quotient
remains warranted by the construction lineage and the battery, not by an
explicit diffeomorphism; and the prime scan is finite, covering $p\le 31$
across the two implementations. The premise of
Lemma~\ref{lem:flag-cohomology} is thus carried by three mutually
independent routes --- the hand derivation, the cellulation, and its
re-implementation --- which agree on the tuple; the hand derivation is the
one a reader can check line by line."""
edits.append(("remark-machine-residuals", OLD3b, NEW3b, 1))

# ---------------------------------------------------------------- Hunk 4
# rem:flag-literature: the two closing sentences.
OLD4 = r"""The algorithmic procedure of
Ref.~\cite{GuerraJana2025} is accordingly a natural candidate route for the
hand derivation posed as open problem (vi) below; and the machine certificate
of Remark~\ref{rem:machine-certificate}, now doubly implemented, is complementary
to, not subsumed by, that programme --- the integral $3$-torsion of the cyclic quotient, with the
exponents fixed, is precisely the layer not addressed by field-coefficient
algorithms."""
NEW4 = r"""The hand derivation of Proposition~\ref{prop:cupsquare} is the
integral lift of the transgression route that the algorithmic procedure of
Ref.~\cite{GuerraJana2025} inspires: the same fibration comparison and
Chern-class transgressions, with the invariant-theoretic input replacing the
field-coefficient module algebra, and the torsion-survival argument of
Step~5 handling the integral $3$-torsion layer that the field-coefficient
algorithms of that programme do not address. The machine certificate of
Remark~\ref{rem:machine-certificate}, now doubly implemented, remains
complementary to, not subsumed by, that programme."""
edits.append(("remark-literature-close", OLD4, NEW4, 1))

# ---------------------------------------------------------------- Hunk 5
# Open problem (vi): discharged.
OLD5 = """(vi) close the last computational premise of Theorem~\\ref{thm:state-d2}: give a hand derivation of the degree-three and degree-four cohomology of the flag quotient $B$ (Lemma~\\ref{lem:flag-cohomology}) --- the premise now rests on two independent implementations (Remark~\\ref{rem:machine-certificate}), so the hand derivation is the remaining route, and the algorithmic procedure of Ref.~\\cite{GuerraJana2025} for the unstable additive cohomology of the unordered quotients is a natural candidate (Remark~\\ref{rem:flag-literature});"""
NEW5 = """(vi) [closed in this version] the hand derivation of the cohomology of the flag quotient $B$ posed as an open problem in earlier versions is supplied by Proposition~\\ref{prop:cupsquare}, whose transgression computation removes the last computational premise of Theorem~\\ref{thm:state-d2}; the machine certificate (Remark~\\ref{rem:machine-certificate}) is retained as an independent cross-check, and the remaining research direction in its neighbourhood is the unstable integral cohomology of the symmetric-group quotients themselves, where the field-coefficient algorithms of Ref.~\\cite{GuerraJana2025} leave the torsion layers open;"""
edits.append(("open-problem-vi", OLD5, NEW5, 1))

# ---------------------------------------------------------------- Hunk 6
# Abstract phrase.
OLD6 = """the latter through a machine computation of the integral cohomology of the cyclic flag quotient, certified by an exact-integer equivariant battery and reproduced by an independent re-implementation"""
NEW6 = """the latter through a hand derivation of the integral cohomology of the cyclic flag quotient by a Chern-transgression computation, cross-checked by an exact-integer equivariant battery and an independent re-implementation"""
edits.append(("abstract-phrase", OLD6, NEW6, 1))

# ---------------------------------------------------------------- Hunk 7
# Intro contributions (1358).
OLD7 = """(Theorem~\\ref{thm:equal-basis-plane}, proved through the cohomology of the flag quotient, machine-certified and independently re-implemented, Lemma~\\ref{lem:flag-cohomology})"""
NEW7 = """(Theorem~\\ref{thm:equal-basis-plane}, proved through the cohomology of the flag quotient --- hand-derived, machine-certified, and independently re-implemented; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})"""
edits.append(("intro-contrib", OLD7, NEW7, 1))

# ---------------------------------------------------------------- Hunk 8
# Conclusion phrase (2427).
OLD8 = """(Theorem~\\ref{thm:state-d2}, proved through the cohomology of the flag quotient, machine-certified and independently re-implemented, Lemma~\\ref{lem:flag-cohomology})"""
NEW8 = """(Theorem~\\ref{thm:state-d2}, proved through the cohomology of the flag quotient --- hand-derived, machine-certified, and independently re-implemented; Lemma~\\ref{lem:flag-cohomology} and Proposition~\\ref{prop:cupsquare})"""
edits.append(("conclusion-phrase", OLD8, NEW8, 1))

# ---------------------------------------------------------------- Hunk 11
# Bibliography: insert HatcherSS after Fulton1997 (citation order).
OLD11 = """\\bibitem{GuerraJana2025}"""
NEW11 = """\\bibitem{HatcherSS}
A. Hatcher, \\emph{Spectral Sequences in Algebraic Topology}, book project,
available at the author's webpage (unpublished draft).

\\bibitem{GuerraJana2025}"""
edits.append(("bib-hatcher", OLD11, NEW11, 1))

# ---------------------------------------------------------------- apply
n_ok = 0
for (name, old, new, cnt) in edits:
    c = src.count(old)
    if c != cnt:
        print(f"ANCHOR FAIL [{name}]: found {c} occurrences (expected {cnt})")
        sys.exit(1)
    src = src.replace(old, new)
    n_ok += 1
    print(f"  ok [{name}]")

import os
os.makedirs(os.path.dirname(INS10), exist_ok=True)
open(INS10, "w").write(src)
print(f"instruments v10 written with {n_ok} hunks "
      f"({len(src.splitlines())} lines)")

# ================================================================ main
msrc = open(MAIN).read()
medits = [
    ("main-abstract",
     "through a flag-quotient computation that is machine-certified and independently re-implemented",
     "through a flag-quotient computation that is hand-derived, machine-certified, and independently re-implemented", 1),
    ("main-body",
     "whose homological premise is machine-certified and independently re-implemented",
     "whose homological premise is hand-derived, machine-certified, and independently re-implemented", 1),
]
m_ok = 0
for (name, old, new, cnt) in medits:
    c = msrc.count(old)
    if c != cnt:
        print(f"MAIN ANCHOR FAIL [{name}]: found {c} (expected {cnt})")
        sys.exit(1)
    msrc = msrc.replace(old, new)
    m_ok += 1
    print(f"  ok [main:{name}]")
os.makedirs(os.path.dirname(MAIN10), exist_ok=True)
open(MAIN10, "w").write(msrc)
print(f"main v10 written with {m_ok} hunks "
      f"({len(msrc.splitlines())} lines)")
