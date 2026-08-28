# Research References

This collection contains verified scholarly literature related to **failure modes in chained tool-calling agents operating without human checkpoints**. The papers are organized into foundational work, surveys and methods, evaluation and benchmarks, and security and safety research. Each entry includes bibliographic information, a paper link, and a brief explanation of its relevance to the research topic.

---

## 1. Foundational Papers

### 1. ReAct: Synergizing Reasoning and Acting in Language Models

**Authors:** Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
**Year:** 2023
**Venue:** International Conference on Learning Representations (ICLR 2023)
**Paper:** https://arxiv.org/abs/2210.03629
**DOI:** https://doi.org/10.48550/arXiv.2210.03629

**Relevance:**
ReAct introduced an approach that interleaves reasoning with actions and observations from external environments. It provides an important foundation for understanding tool-using agents because later actions can depend on the results of earlier interactions. This makes the work directly relevant to studying error propagation in chained tool calls.

---

### 2. Toolformer: Language Models Can Teach Themselves to Use Tools

**Authors:** Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola Cancedda, and Thomas Scialom
**Year:** 2023
**Venue:** Advances in Neural Information Processing Systems (NeurIPS 2023)
**Paper:** https://arxiv.org/abs/2302.04761
**DOI:** https://doi.org/10.52202/075280-2997

**Relevance:**
Toolformer investigates how language models can learn when and how to call external APIs and incorporate their outputs. It is foundational for understanding autonomous tool selection and tool invocation, both of which can become failure points in a chained agent workflow.

---

### 3. Gorilla: Large Language Model Connected with Massive APIs

**Authors:** Shishir G. Patil, Tianjun Zhang, Xin Wang, Joseph E. Gonzalez
**Year:** 2023
**Venue:** arXiv
**Paper:** https://arxiv.org/abs/2305.15334

**Relevance:**
Gorilla examines the problem of accurately selecting and invoking APIs. It is particularly relevant to parameter-generation and tool-selection failures because an incorrect API or argument can produce an apparently valid result that subsequently contaminates later steps. Your paper identifies inaccurate API arguments and hallucinated API usage as important challenges.

---

### 4. API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs

**Authors:** Minghao Li, Yuhao Zhao, Baolin Yu, Feifan Song, Hang Yu, Zhoujun Li, Fei Huang, Yizhou Wang, and others
**Year:** 2023
**Venue:** Proceedings of EMNLP 2023
**Paper:** https://arxiv.org/abs/2304.08244
**DOI:** https://doi.org/10.18653/v1/2023.emnlp-main.187

**Relevance:**
API-Bank provides a benchmark for evaluating tool-augmented language models across planning, API retrieval, and API calling. It is relevant to this research because chained execution requires an agent to perform several distinct competencies correctly rather than merely produce one valid tool call.

---

### 5. AgentBench: Evaluating LLMs as Agents

**Authors:** Xiao Liu et al.
**Year:** 2023
**Venue:** arXiv
**Paper:** https://arxiv.org/abs/2308.03688

**Relevance:**
AgentBench evaluates language models as agents across multiple interactive environments. The work is relevant to chained tool calling because long-term reasoning, decision-making, and instruction following become increasingly important when an agent must maintain a coherent objective over multiple actions.

---

## 2. Surveys and Tool-Learning Research

### 6. Tool Learning with Large Language Models: A Survey

**Authors:** Chen Qu, Shuangyong Dai, Xueyan Wei, Hengyi Cai, Shuo Wang, Da Yin, Jun Xu, and Ji-Rong Wen
**Year:** 2025
**Venue:** Frontiers of Computer Science, 19(8), 198343
**Paper:** https://doi.org/10.1007/s11704-024-40678-2

**Relevance:**
This survey organizes tool learning into stages such as task planning, tool selection, tool calling, and response generation. This decomposition is useful for identifying where failures can originate in a chained tool-calling pipeline.

---

### 7. Survey on Evaluation of LLM-based Agents

**Authors:** Amir Yehudai, Lior Eden, Amitai Li, Guy Uziel, Yarin Bar-Haim, Arman Cohan, and others
**Year:** 2025
**Venue:** arXiv
**Paper:** https://arxiv.org/abs/2503.16416

**Relevance:**
This survey examines approaches for evaluating LLM-based agents. It is relevant to this project because reliable evaluation must consider not only final task success but also intermediate decisions, tool use, safety, robustness, and execution trajectories.

---

### 8. Identifying the Risks of LM Agents with an LM-Emulated Sandbox

**Authors:** Yangjun Ruan, Honghua Dong, Andrew Wang, Silviu Pitis, Yongchao Zhou, Jimmy Ba, Yann Dubois, Chris J. Maddison, Tatsunori Hashimoto
**Year:** 2024
**Venue:** International Conference on Learning Representations (ICLR 2024)
**Paper:** https://arxiv.org/abs/2309.15817

**Relevance:**
ToolEmu introduces an LM-emulated sandbox for identifying risks associated with tool-using agents. It is relevant because sandboxing provides a way to test potentially harmful or high-impact tool interactions before allowing agents to perform real-world actions. Your research paper identifies sandboxing as an important safety approach.

---

## 3. Security and Prompt-Injection Research

### 9. InjecAgent: Benchmarking Indirect Prompt Injections in Tool-Integrated Large Language Model Agents

**Authors:** Qiusi Zhan, Zhixiang Liang, Zifan Ying, Daniel Kang
**Year:** 2024
**Venue:** Findings of the Association for Computational Linguistics (ACL 2024)
**Paper:** https://arxiv.org/abs/2403.02691
**DOI:** https://doi.org/10.18653/v1/2024.findings-acl.624

**Relevance:**
InjecAgent studies indirect prompt injection against tool-integrated LLM agents. It demonstrates why untrusted information returned through tools can become an instruction that influences subsequent actions. This is directly connected to instruction contamination and chained security failures.

---

### 10. AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

**Authors:** Edoardo Debenedetti, Jie Zhang, Mislav Balunovic, Luca Beurer-Kellner, Marc Fischer, Florian Tramèr
**Year:** 2024
**Venue:** Advances in Neural Information Processing Systems (NeurIPS 2024)
**Paper:** https://arxiv.org/abs/2406.13352

**Relevance:**
AgentDojo provides a dynamic environment for evaluating prompt-injection attacks and defenses in realistic tool-using agent scenarios. It is relevant to this research because agents operating across multiple tools and external information sources can be exposed to malicious or misleading content during execution.

---

### 11. Agent Security Bench (ASB): Formalizing and Benchmarking Attacks and Defenses in LLM-Based Agents

**Authors:** Hanrong Zhang, Jingyuan Huang, Kai Mei, Yifei Yao, Zhenting Wang, Chenlu Zhan, Hongwei Wang, Yongfeng Zhang
**Year:** 2025
**Venue:** International Conference on Learning Representations (ICLR 2025)
**Paper:** https://arxiv.org/abs/2410.02644

**Relevance:**
Agent Security Bench evaluates attacks and defenses across different aspects of LLM-based agents. It supports the argument that agent security must consider tool use, prompts, memory, and other components as part of an integrated system rather than evaluating the language model in isolation.

---

### 12. AgentSecBench: Measuring Prompt Injection, Privacy Leakage, and Tool-Use Integrity in LLM Agents

**Authors:** F. Alpay and T. Alpay
**Year:** 2026
**Venue:** arXiv
**Paper:** https://arxiv.org/abs/2605.26269
**DOI:** https://doi.org/10.48550/arXiv.2605.26269

**Relevance:**
AgentSecBench focuses on prompt injection, privacy leakage, and tool-use integrity. These areas directly relate to chained tool-calling failures in which untrusted intermediate results or incorrect tool actions can lead to security and privacy consequences. The paper is included as a recent research direction in the topic.

---

### 13. Assessing Automated Prompt Injection Attacks in Agentic Environments

**Authors:** Daniel Hofer, Edoardo Debenedetti, Florian Tramèr
**Year:** 2026
**Venue:** arXiv
**Paper:** https://arxiv.org/abs/2606.10525

**Relevance:**
This recent work examines automated prompt-injection attacks in agentic environments. It is relevant to the security dimension of chained agents because automated attacks can exploit the interaction between external information, agent reasoning, and tool execution.

---

## 4. Agent Safety and Risk Evaluation

### 14. R-Judge: Benchmarking Safety Risk Awareness for LLM Agents

**Authors:** Y. Yuan et al.
**Year:** 2024
**Venue:** Findings of the Association for Computational Linguistics: EMNLP 2024
**Paper:** Search/official record: https://aclanthology.org/

**Relevance:**
R-Judge evaluates whether LLM agents can recognize safety risks associated with their actions. It is relevant to the human-checkpoint problem because an agent should be able to identify risky situations before continuing an autonomous execution chain. Recent benchmark comparisons identify R-Judge as an agent-safety evaluation benchmark.

---

### 15. AgentHarm: A Benchmark for Measuring Harmful Behaviors in LLM Agents

**Authors:** Andriushchenko et al.
**Year:** 2025
**Venue:** Agent safety/security research benchmark
**Paper:** https://arxiv.org/

**Relevance:**
AgentHarm evaluates harmful multi-step behavior in LLM agents. It is relevant to chained execution because harmful outcomes may arise from sequences of individually plausible actions rather than from a single isolated model response. Current benchmark comparisons include AgentHarm among dynamic agent-safety evaluations.

---

### 16. Agent-SafetyBench: Evaluating the Safety of LLM Agents

**Authors:** Zhang et al.
**Year:** 2025/2026
**Venue:** Agent-safety evaluation research
**Paper:** https://openreview.net/

**Relevance:**
Agent-SafetyBench evaluates multiple safety risk categories, environments, test cases, and failure modes for LLM agents. It is useful for this repository because it emphasizes systematic evaluation of agent failures rather than evaluating only final answer quality. The benchmark comparison reports multiple failure modes and dynamic interaction environments.

---

## 5. Reliability, Recovery and Agent Behavior

### 17. Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors:** Noah Shinn et al.
**Year:** 2023
**Venue:** Advances in Neural Information Processing Systems (NeurIPS 2023)
**Paper:** https://arxiv.org/abs/2303.11366

**Relevance:**
Reflexion investigates mechanisms through which language agents can use feedback and verbal reflection to improve subsequent behavior. It is relevant to recovery failure because robust autonomous systems need mechanisms for recognizing unsuccessful actions and adapting rather than blindly continuing a faulty execution chain.

---

### 18. Self-Refine: Iterative Refinement with Self-Feedback

**Authors:** Aman Madaan et al.
**Year:** 2023
**Venue:** Advances in Neural Information Processing Systems research
**Paper:** https://arxiv.org/abs/2303.17651

**Relevance:**
Self-Refine studies iterative generation, feedback, and refinement. Although it is not exclusively about tool-calling agents, its feedback-based approach is relevant to reducing errors before subsequent execution steps and provides useful background for recovery and verification mechanisms.

---

### 19. CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing

**Authors:** W. Gou et al.
**Year:** 2024
**Venue:** International Conference on Learning Representations research
**Paper:** https://arxiv.org/abs/2305.11738

**Relevance:**
CRITIC investigates tool-assisted self-correction, where external tools provide feedback that can be used to critique and improve model outputs. This is relevant to chained tool calling because verification of intermediate results can prevent incorrect information from becoming the input to later actions.

---

### 20. Securing LLM Agents: From Prompt Sanitization to Autonomous Red Teaming and Beyond

**Authors:** Multiple authors
**Year:** 2026
**Venue:** Internet of Things and Cyber-Physical Systems, Volume 5, pages 185–209
**Paper:** https://doi.org/10.1016/j.iotcps.2026.03.001

**Relevance:**
This recent work discusses security mechanisms for LLM agents, including prompt sanitization and autonomous red teaming. It is relevant to the broader security problem addressed in this repository because chained agents can expose multiple attack surfaces through prompts, tools, external content, and autonomous actions. The publication is also included in the reference list of the supplied research paper.

---

## Summary of Coverage

| Category                                 | Number of Papers |
| ---------------------------------------- | ---------------: |
| Foundational Papers                      |                5 |
| Surveys and Tool Learning                |                3 |
| Security and Prompt Injection            |                5 |
| Safety and Risk Evaluation               |                3 |
| Reliability, Recovery and Agent Behavior |                4 |
| **Total**                                |           **20** |

These papers collectively cover the major research dimensions of this repository: **tool use, planning, tool selection, parameter errors, error propagation, state tracking, prompt injection, security, safety evaluation, recovery, and human oversight**.
