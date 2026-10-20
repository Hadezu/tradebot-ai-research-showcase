# TradeBot — building a complex product with AI

**Private research project · Active development**

I am building TradeBot to investigate whether software can learn to make better trading decisions. It studies historical markets, compares possible actions and tests them with virtual money, costs and risk limits.

The research platform has been built and tested. **Consistent profitability has not been proven.** This portfolio shows how I manage a complex software project with ChatGPT and Codex. The application and its trading rules remain private.

## How I work

I develop ideas, define requirements and discuss possible solutions with ChatGPT. I give Codex specific implementation tasks, read its reports, ask for checks and decide what to improve next.

**AI helps write and test the code. I manage the direction, priorities and decisions.** I do not claim to have written the whole system by hand.

![How I work with AI](assets/development-loop.svg)

## What we have built

- A research system covering **nine markets and 21 trading strategies**.
- Tools to study completed trades, rejected opportunities and situations where strategies gave no signal.
- Virtual trading that tracks costs, available money and risk.
- A workflow to train models, compare their results and reject unsuitable versions.
- Checks for data quality and recovery after interrupted work.

The selected private test suites recorded **280 passed, 0 failed and 2 skipped** on 20 October 2026. This checks specific software behavior; it does not prove profitability or cover every possible failure. [What the tests establish](docs/verification.md)

## Three problems we solved

| Problem | Solution and result |
|---|---|
| Old research results could be used after calculation rules changed. | Added compatibility checks and rebuilt affected results. Unsuitable old data is blocked. |
| An interruption could leave uncertainty about whether model training had finished. | Added verified recovery. Completed work can be reused; uncertain files are stopped for review. |
| A trained model could appear ready without the required evaluation. | Separated training from approval. Missing evidence now prevents admission. |

[Read the detailed cases](docs/engineering-case-studies.md)

## Why this project matters

It shows how I turn an idea into requirements, coordinate AI-assisted implementation and keep asking for evidence when something goes wrong. These are the skills I want to bring to AI-assisted product development and automation work.

The next challenge is to find out whether the models can consistently make useful decisions. A working platform does not guarantee that result.

**Explore:** [My development process](docs/ai-development-workflow.md) · [Technical architecture](docs/architecture.md) · [Current status](docs/project-status.md) · [Small, safe demo](demo/README.md)
