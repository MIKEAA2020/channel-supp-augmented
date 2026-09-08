# GLM contributions (waves 1-6)

This folder collects this assistant's deliverables for the
`channel-supp-augmented` project. The original `manuscript uploads/` and
`wave 2 audits/` folders are untouched; wave 4 produced corrected new
versions of the manuscripts in `manuscript uploads v3/`; wave 5 applied the
flat-width attack as new versions (v4) in `manuscript uploads v4/`; wave 6
completed the attack as new versions (v5) in `manuscript uploads v5/`.

| Path | What it is |
|---|---|
| `WAVE6_FLAT_WIDTH_ATTACK_2.md` | **Wave 6 (this round).** The flat-width attack completed: switching from slot-counting to **coordinate**-counting (`nd_B` flags) yields the **coordinate dichotomy** — `δ_r = 1` iff `nd_B ≤ 2r+2`, proved for `d_B ∈ {1,2}` (complete classical and qubit dichotomies), with `δ_r ≥ 4/3` proved below the diagonal for every `d_B` (elementary median matching at `r = 1`, topological Tverberg at `r ≥ 2`), `δ₁(Δ₄) = 4/3` and `δ_r(2r+3) = 4/3` exactly, `δ_{n−1} = 2(1−1/d_B)` exactly for prime-power `d_B`, the qubit flat threshold improved to `r ≥ n−1`, the v4 refined conjecture refuted at `r ≥ 2`, the channel-level `n = 1` instance refuted for `d_B ≥ 5`, and the corrected statement posed as `con:coord-flat`. |
| `WAVE5_FLAT_WIDTH_ATTACK.md` | **Wave 5.** The flat-width conjecture `con:flat-d1` attacked via the simplex sub-case: **refuted** at the bottom index (`δ₁ ≥ 4/3` for `n ≥ 5`, every `d_B`, full elementary proof), flatness **proved** on the upper half of the subcritical range for classical outputs and from latent dimension `n` for qubit outputs, and the refined statement posed as `con:flat-refined`. Also records the 54-claims ledger reconciliation. |
| `WAVE3_ELEVATION_AND_CORRECTIONS.md` | **Wave 4.** All verified corrections from waves 1-3 applied to the two manuscripts as new versions (v3); every overclaim elevated (math strengthened to meet it) or demoted to an explicit conjecture. |
| `WAVE2_AUDIT_VERIFICATION_REPORT.md` | **Wave 3.** The four `wave 2 audits/` files sorted into 16 attributed audits, every substantive claim verified against the then-current manuscripts, jointly evaluated with the wave-1 report. |
| `sorted-wave2-audits/` | The 16 audits split into one file each, grouped by target paper (see its README). |
| `wave 1 report/` | **Wave 1.** Line-level review of both manuscripts (docx + pdf). Findings are folded into the wave-3 report's consolidated list. |
| `synthesis paper/` | **Wave 0 (earlier rounds).** Corrected synthesis paper (tex + compiled pdf); the tex is identical to `gpt round two/glm_CORRECTED_SYNTHESIS_PAPER2.tex` already in this repo. |

The current manuscripts live in `../manuscript uploads v5/`
(`instruments-paper-revised5.txt/.pdf`, `main-article-revised5.txt/.pdf`);
the previous corrected versions are in `../manuscript uploads v4/` and
`../manuscript uploads v3/`.
