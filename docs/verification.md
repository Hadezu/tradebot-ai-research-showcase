# Verification and evidence boundary

## Private engineering acceptance

The local acceptance snapshot dated **20 October 2026** contains **280 PASS / 0 FAIL / 2 SKIP** across selected regression and integration suites. For this presentation, those totals were recomputed from the saved test XML and the associated acceptance artifact hashes were checked locally. The private suite was not rerun solely to prepare this portfolio.

The two skips are opt-in orchestration-evidence placeholders. Separate saved orchestration and restart evidence exists; this does not turn skipped test cases into passes.

Coverage includes causal execution, accounting, model compatibility, unresolved outcomes, native signal generation, management actions, admission checks and recovery. It is not an exhaustive proof of correctness or a coverage percentage. Code existence alone is labelled IMPLEMENTED, not VERIFIED.

## What a visitor can reproduce

The standalone demo and its tests run from this repository using the Python standard library. Their results apply only to that educational example. They are separate from the private acceptance count.

## What remains private

Source implementation, full test logs, historical datasets, model files, trading rules and operational identifiers are intentionally excluded. Consequently, the private acceptance claims cannot be independently reproduced from this showcase. The owner can discuss methodology without disclosing protected implementation or sensitive records.

## Limits

- No claim of stable profitability, independent certification or production readiness.
- Repeatedly explored historical periods are not described as untouched holdouts.
- Modelled outcomes are not real account returns.
- A safe recovery path may require manual intervention when evidence is incomplete.
- Tested management execution interfaces do not imply that every action has a trained, approved selector.

Public-demo checks and release-file hashes are documented separately in the locally prepared review package. No private evidence needs to be published to run the demo.

## Scope of the presentation refresh

The 20 October 2026 refresh inspected the active local research branch, including uncommitted research changes, instead of relying on the default branch. Source, test definitions and saved acceptance were read; the private application, training and trading runtime were not started.

The 9-market / 21-strategy figures describe a documented research protocol, not profitable markets or production deployments. The overview diagram groups responsibilities; it does not imply six independently deployed services. Newly inspected code is not automatically covered by the saved acceptance. The historical research acceptance also does not close unrelated PAPER runtime accounting issues or establish live readiness.
