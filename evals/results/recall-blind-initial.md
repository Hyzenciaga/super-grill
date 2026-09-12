# Initial recall and sequential tasting probe

Actor: GPT-5.6 Terra, fresh context, task `probe_recall_blind`.
Input graph: D-1 depends on A-1; R-1 on D-1; T-1 on R-1; E-1 on T-1.
Independent chain D-2 -> R-2 -> T-2 -> E-2 in prerequisite-to-dependent notation.
A-1 (one editor per list) is disproved. User asked for read-only recall followed
by a sequential comparison of whole-list retry versus an operation queue under
timeout, duplicate delivery and restart; no agents, writes or actual experiments.

## Actor response (verbatim)

Firing up Super Grill: **analysis / well-done / single-skewer**. Your request has been assigned a committee and a suspiciously small plate.

**Ingredient Recall**

A-1（“同一清单只会有一个写入设备”）已被新情况推翻，修订为：同一清单可能存在多个写入设备。它使依赖链上的旧结论失效，但不抹除历史。

| 节点 | 状态 | 原因 |
|---|---|---|
| A-1 | 已修订 | 单写入者前提不成立 |
| D-1 | stale，需重审 | 直接依赖 A-1 |
| R-1 | stale，需重审 | 依赖 D-1 |
| T-1 | stale，需重审 | 依赖 R-1 |
| E-1 | stale，需重审 | 依赖 T-1 |
| D-2 | 保持有效 | 无依赖 A-1 |
| R-2 | 保持有效 | 仅依赖 D-2 |
| T-2 | 保持有效 | 仅依赖 R-2 |
| E-2 | 保持有效 | 仅依赖 T-2 |

本次只召回 A-1 的可达下游，D-2 链不需要重新批准或重做验证。成就解锁：**Selective Amnesia, Professionally Applied**。

**Kitchen Blind Tasting**

以下是顺序完成的两条方案分析，不代表独立评审。共同考题是：多个设备可写同一清单；必须处理超时、重复请求和进程重启。

| 场景 | 路线甲：超时即整单重发并覆盖服务端 | 路线乙：持久化操作队列 + 稳定 operation id + 确认后出队 |
|---|---|---|
| 请求超时，但服务端其实已写入 | 客户端不知道结果，再次覆盖整单；若期间另一设备修改过清单，会把其修改抹掉 | 以相同 operation id 重试；服务端返回首次处理结果，不重复执行 |
| 重复请求 | 相同快照的重复覆盖看似无害，但对并发写入并不幂等：旧快照可覆盖新状态 | 同一 operation id 只应用一次；重复请求只获得同一确认结果 |
| 两设备分别修改后恢复连接 | 最后一次整单覆盖获胜，且“最后”可能只是网络较慢、超时重试或重启后的旧客户端 | 两台设备的意图作为独立操作提交；仍需要冲突规则，但不会把重试误当成新意图 |
| 进程重启 | 若未持久化待发快照，修改可能丢失；若持久化后盲重发，又可能用陈旧整单覆盖服务端 | 重启后恢复未确认队列，以原 operation id 重试；已确认项不会再次生效 |
| 复杂度 | 初期最低，之后必须补版本校验、冲突处理和恢复状态，最终会变成另一套队列协议 | 需要持久化队列、服务端去重表和确认协议；职责清晰、可测试、恢复路径稳定 |

**推荐路线乙。** 它将“用户做了一次操作”与“网络把该操作投递了几次”分开处理；超时、重复投递和重启都只会重试同一个操作，而不会把旧的整单状态再次宣告为真。

不过，稳定 operation id 解决的是**重复执行**，不是多设备的**业务冲突**。D-1 重审时应改为：每个操作持久化 `operation_id`、清单标识、操作内容、创建顺序和确认状态；服务端对 `(list_id, operation_id)` 做持久去重，并返回原始确认。客户端按每清单顺序重放，只有收到确认才出队。随后还需明确服务器如何合并两台设备的不同操作：例如基于版本的冲突返回、可组合的操作语义，或 CRDT/OT 方案。若没有这层规则，路线乙虽能避免重复写，仍无法自动判定“甲删掉条目、乙同时修改条目”应如何落定。

路线甲只有在恢复为“带基线版本的条件写入，版本冲突时拒绝覆盖并进入合并流程”后才勉强可用；但那已经不再是“超时即整单覆盖”，而是在重新发明路线乙所需的确认、恢复和冲突边界。

第二轮审视没有改变结论：整单覆盖把网络不确定性放大为数据丢失风险；持久化幂等队列把它限制为可重试的投递问题。建议将 D-1 更新为路线乙，并将 R-1/T-1/E-1 的重审重点放在多设备冲突语义、去重记录持久期，以及重启后的队列恢复。

## Grading and correction

Recall propagation/isolation and honest sequential provenance passed. The design
analysis overstated the equivalence of repairing whole-state conditional writes
and adopting an operation queue, and blurred idempotency with concurrent lost
updates. It is retained as an imperfect result, not a clean analytical verdict.
The tasting protocol was refined to separate specified mechanisms from required
conditions and to consider each option's smallest viable repair. Further reruns
still showed technical overstatement; their full raw outputs were not retained
in this checkout. See the validation record for this limitation and the separately
retained independent import-design comparison. Role compliance does not prove
domain accuracy.
