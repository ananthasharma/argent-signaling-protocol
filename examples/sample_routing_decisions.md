# Sample Routing Decisions

| Header | Failure class | Decision | Reason |
| --- | --- | --- | --- |
| `[@C:E; @G:F; @S:1; A:[K:12, L:07]]` | Pass | `EXECUTE` | Grounded and low stochasticity |
| `[@C:A; @G:D; @S:2; A:[K:12, L:09]]` | Grounded partial | `REGENERATE` | Coverage can be improved without containment |
| `[@C:8; @G:A; @S:4; A:[L:21, P:03]]` | Citation gap | `REGENERATE` | Repairable citation weakness |
| `[@C:3; @G:1; @S:C; A:[H:17]]` | Ungrounded | `BLOCK` | Weak grounding and high stochasticity |# Sample Routing Decisions

| Header | Failure class | Decision | Reason |
| --- | --- | --- | --- |
| `[@C:E; @G:F; @S:1; A:[K:12, L:07]]` | Pass | `EXECUTE` | Grounded and low stochasticity |
| `[@C:A; @G:D; @S:2; A:[K:12, L:09]]` | Grounded partial | `REGENERATE` | Coverage can be improved without containment |
| `[@C:8; @G:A; @S:4; A:[L:21, P:03]]` | Citation gap | `REGENERATE` | Repairable citation weakness |
| `[@C:3; @G:1; @S:C; A:[H:17]]` | Ungrounded | `BLOCK` | Weak grounding and high stochasticity |
