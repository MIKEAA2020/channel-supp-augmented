# Sorted wave-2 audits (GLM wave 3)

The four files in `wave 2 audits/` contain **sixteen** separate audits (several files
concatenate multiple audits). They are split here into one file per audit, attributed
to the model named in the source, and grouped by target manuscript.

Verification of every substantive claim in these audits (against the current
`manuscript uploads/` texts) is in `../WAVE2_AUDIT_VERIFICATION_REPORT.md`.

## Instruments paper (`manuscript uploads/instruments-paper-revised2.txt`, 1615 lines)

| # | File | Model | Type | One-line verdict |
|---|------|-------|------|------------------|
| 1 | 01-gpt-terra_line-level-audit.txt | gpt terra | line-level, 17 findings | 14 of 17 verified valid (2 stale/soft, 1 rejected); highest yield |
| 2 | 02-qwen_consistency-verification.txt | qwen | verification | no flaws found; consistent with independent recomputation |
| 3 | 03-gpt-terra_physical-intuition.txt | gpt terra | recommendations | high-quality physical-narrative suggestions |
| 4 | 04-qwen_physical-intuition.txt | qwen | recommendations | pedagogy suggestions |
| 5 | 05-grok_verification-verdict.txt | grok | verification | 'all results follow'; 2 accurate minor notes |
| 6 | 06-gemini_line-level-audit.txt | gemini | line-level (mangled encoding) | ~9 findings, all located and verified valid |
| 7 | 07-gemini_executive-assessment.txt | gemini | assessment + verification | verifications consistent; insight suggestions |
| 8 | 08-max_deep-audit.txt | max | deep audit, 2 passes | no math errors; 4-5 precision items, all verified valid |

## Channel paper (`manuscript uploads/main-article-revised2.txt`, 3646 lines)

| # | File | Model | Type | One-line verdict |
|---|------|-------|------|------------------|
| 1 | 01-hy4_first-half-preliminary.txt | hy4 | preliminary (first half) | 5 accurate tracked items |
| 2 | 02-claude_line-level-audit.txt | claude | line-level (A/B/C) | highest precision of all audits; every sub-claim verified |
| 3 | 03-ai-model_line-level-and-intuition.txt | 'ai model' | line-level + intuition | 1 false positive (\rhodep), 1 self-retracted alarm; rest valid |
| 4 | 04-qwen_full-audit.txt | qwen | full audit | verdict 'sound'; 4 polish items (1 overlap misses a real imprecision) |
| 5 | 05-gemini_first-half-verification.txt | gemini | verification | consistent |
| 6 | 06-grok_cross-companion-consistency.txt | grok | cross-paper check | 3 accurate notes (join d_B>=3, C_n, conjugate bars) |
| 7 | 07-gemini_second-half-assessment.txt | gemini | assessment + verification | verifications consistent with independent recomputation |
| 8 | 08-max_deep-audit.txt | max | deep audit | 2 false positives (escape artifacts), 1 valid big catch (d_B=3 join) |
