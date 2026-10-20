# Engineering case studies

These three cases describe the private engineering acceptance of 20 October 2026. They explain requirements, decisions and verification without exposing trading rules or internal artifacts. [Evidence boundaries](verification.md) apply throughout: private tests are not publicly reproducible from this repository.

## 1. When an unchanged action no longer has a compatible label

### Problem and consequence

A research label describes the outcome of an action under a particular execution model. It is not an intrinsic property of the action name. If the executor changes, an old outcome may no longer answer the question that the current model is learning to predict.

This can produce a misleading experiment even when the learning code runs successfully: training targets represent one set of assumptions, while evaluation applies another. A file loading without an error is therefore insufficient evidence of compatibility.

### Requirement and engineering decision

The requirement was to restore compatible historical targets while preserving old evidence. The solution extended the existing data preparation and execution path rather than introducing another simulator.

Compatibility binds observations, action identity and execution assumptions. Reuse requires equivalent economic inputs and a validated execution context. A matching name or unchanged feature vector does not establish that equivalence. Where equivalence cannot be demonstrated, the existing executor must calculate a new result.

The approach deliberately separates two questions:

- Is this an available action at decision time?
- Is its eventual outcome sufficiently determined and mature to become a training answer?

An unresolved future outcome must not retrospectively remove an action from the choices the model originally faced. Conversely, an available action does not automatically provide a valid supervised label.

### Verification

The private acceptance checked source identities, feature timing, contract compatibility and financial records. Recorded cash, charges and position accounting were reconciled; control replays checked the corresponding outcomes. Repeat processing checked that verified parts could be reused without duplicating financial receipts.

| Condition | Expected behavior |
|---|---|
| Compatible inputs and execution identity | Process under the bound contract |
| Changed or unverified execution semantics | Reject reuse or recalculate |
| Outcome still unresolved | Preserve uncertainty; exclude it as a definite training answer |
| Outcome not yet mature at training time | Keep it unavailable to that training run |
| Restart after a verified part completed | Reuse verified work without duplicate records |

### Result and limits

The selected corpus was made compatible with the tested execution version. This is a data-integrity achievement, not evidence of improved prediction. Financial reconciliation establishes consistency with a model; it cannot establish that every historical fill was observable or that a future strategy will be profitable.

**Transferable lesson:** dataset lineage includes the meaning of a target, not just the bytes of its features. This applies to any ML system whose labels depend on a changing business process.

## 2. A saved model is not necessarily a completed job

### Failure scenario

Training can finish and write an artifact before the workflow records completion. After interruption, the next run sees a file but lacks a complete account of how it was produced.

Two shortcuts are unsafe. Retraining silently creates a different execution history and may produce a different model. Accepting any existing file risks loading a partial artifact or one belonging to another job.

### Requirement and engineering decision

The owner required recovery without repeating a completed fit, with explicit rejection when provenance could not be established. The implementation extended the existing durable artifact workflow.

The job is bound to its inputs and compatibility context. Artifact verification and completion confirmation are separate steps. A verified preparation record supports finishing an interrupted confirmation; an unproven save does not.

This is intentionally conservative: an ambiguous operation stops for investigation instead of manufacturing certainty from the existence of a file. A content hash detects a mismatch only when compared with a trusted expected identity; hashing arbitrary bytes alone does not establish provenance.

### Recovery behavior checked

| Interruption point | Verified behavior |
|---|---|
| Before fit starts | Resume and perform one fit |
| During saving, without verified preparation | Stop for manual recovery; do not silently refit |
| After verified save, before completion confirmation | Complete confirmation without another fit |
| After confirmation, before checkpoint completion | Finish the missing checkpoint |
| After checkpoint | Finish the job record |
| After job completion | Load the same verified artifact |

Small real-fit tests injected these interruptions. Assertions counted fit calls, compared loaded predictions, checked artifact identity and verified that financial evidence was not modified. Additional checks rejected changed inputs and corrupted artifacts.

### Result and limits

Supported recovery paths preserve the completed model rather than fitting a replacement. The ambiguous save window remains fail-closed, which means manual intervention may be required. Tests cover specific software interruption points, not every operating system, concurrent writer or storage-device failure.

The [public demo](../demo/README.md) illustrates a smaller concept: recreate a missing receipt only when artifact contents match trusted evidence. It does not reproduce the private trainer or its complete recovery guarantees.

**Transferable lesson:** reliable automation requires an explicit definition of completion. A persisted output and a committed job are different facts.

## 3. Training success must not become deployment permission

### Problem and consequence

A model can train successfully yet have unknown evaluation quality. Repeated reports can also make a small amount of experience look larger than it is. If readiness is represented by a loosely interpreted approval flag, old records or fallback behavior can bypass the intended evidence requirements.

The confirmed admission defect allowed readiness to coexist with an unknown evaluation state. That is a control-flow problem even before considering whether the model predicts anything useful.

### Requirement and engineering decision

Admission was made conditional on the required evidence for the specific candidate. Training completion is insufficient. Unknown, missing, failed or incompatible evaluation evidence cannot justify approval, and old saved flags cannot serve as an alternative route.

Experience accounting must preserve the distinction between multiple observations of one underlying trade and independent support. Duplicate or conflicting reports cannot manufacture a larger confirmed sample. Unresolved and scenario-based outcomes must not be presented as confirmed positive evidence.

### Verification

| Input condition | Expected decision |
|---|---|
| Successful training, no required evaluation evidence | Reject admission |
| Old approval flag with unknown evaluation | Reject admission when read |
| Evidence for a different candidate or incompatible contract | Reject use |
| Duplicate or conflicting experience | Do not count as additional valid support |
| Compatible candidate and all required evidence present | Allow the relevant eligibility status; do not activate automatically |

The private acceptance includes regression checks for admission, unique experience and research handoff. Research evaluation remains separate from runtime permission: a candidate may be tested under restricted conditions without becoming deployable.

### Result and limits

The system can reject a technically valid model. This is necessary behavior, not an unsuccessful completion of the engineering task. Gate tests demonstrate that tested evidence requirements are enforced; they do not prove that the requirements themselves establish a durable trading advantage.

**Transferable lesson:** artifact creation, evaluation and authorization should have separate meanings. An automated workflow must retain a valid rejection path.

## What these cases demonstrate together

The work addresses three different sources of false confidence: incompatible targets, ambiguous completion and unsupported approval. The owner's contribution was to define these problems and acceptance constraints, direct AI-assisted implementation and require evidence before proceeding. The code and tests were developed with AI assistance; these accounts do not claim an external independent audit or unaided manual implementation.
