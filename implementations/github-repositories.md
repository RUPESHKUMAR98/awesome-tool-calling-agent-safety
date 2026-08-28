# GitHub Implementations

This section contains open-source GitHub implementations related to LLM-based agents, tool calling, tool learning, and agent security. The selected repositories provide practical implementations that can be used to understand, reproduce, or evaluate the problems discussed in this research, including tool-selection errors, chained execution, prompt injection, security vulnerabilities, and failure propagation.

---

## 1. AgentDojo

**Repository:**
https://github.com/ethz-spylab/agentdojo

**Project:** AgentDojo

**What it Implements:**
AgentDojo provides a dynamic environment for evaluating LLM agents that interact with external tools. It includes realistic tasks and environments in which agents must use tools to complete user objectives. The implementation also supports evaluation of indirect prompt-injection attacks and defensive techniques.

**Why It Is Relevant:**
This repository is highly relevant to the research topic because an agent can receive information from one tool and use that information when deciding what to do next. If the information contains a malicious instruction or an incorrect assumption, the problem can propagate to later tool calls. AgentDojo therefore provides a practical environment for studying **prompt injection, tool-output contamination, autonomous tool use, and security failures in chained workflows**.

**Research Connection:**
Your research paper identifies AgentDojo as a dynamic environment for evaluating prompt-injection attacks and defenses against agents operating on untrusted data.

---

## 2. ToolBench / ToolLLM

**Repository:**
https://github.com/OpenBMB/ToolBench

**Project:** ToolBench / ToolLLM

**What it Implements:**
ToolBench provides an open-source framework, dataset, training code, evaluation code, tool environment, and models for teaching language models to use a large collection of real-world APIs. The project includes ToolLLaMA models, tool retrieval, tool-use data, and ToolEval evaluation components. The repository supports both single-tool and multi-tool scenarios.

**Why It Is Relevant:**
ToolBench is directly connected to chained tool calling because multi-tool tasks require an agent to select and invoke several tools. A mistake in tool retrieval, tool selection, parameter generation, or execution can influence subsequent steps.

It can therefore be used to study:

* Tool-selection failure
* API retrieval errors
* Parameter-generation errors
* Multi-tool planning
* Sequential tool execution
* Error propagation

**Research Connection:**
Your research paper identifies API selection, planning, and tool calling as separate competencies and explains that an error at an earlier stage can affect later stages.

**Implementation Evidence:**
The official repository provides installation instructions, training scripts, retrieval models, ToolLLaMA models, and ToolEval evaluation components.

---

## 3. Gorilla

**Repository:**
https://github.com/ShishirPatil/gorilla

**Project:** Gorilla: Large Language Model Connected with Massive APIs

**What it Implements:**
Gorilla is an implementation designed to connect large language models with APIs and tools. It focuses on generating appropriate API calls from natural-language requests and improving the reliability of API invocation.

The project also provides APIBench, a collection of APIs designed for research on tool and API use. A publicly available implementation describes Gorilla as an LLM system capable of selecting semantically and syntactically appropriate APIs.

**Why It Is Relevant:**
Gorilla is especially relevant to **tool-selection and parameter-generation failures**. An agent may select an incorrect API or generate an incorrect argument even when the request appears syntactically valid. In a chained workflow, such an error can become the input to another tool and produce a downstream failure.

**Research Connection:**
Your paper specifically identifies Gorilla as research demonstrating problems with inaccurate API arguments and API usage.

**Key Research Area:**
`Tool Selection → Parameter Generation → Tool Execution → Error Propagation`

---

## 4. Agent Security Bench (ASB)

**Repository:**
https://github.com/agiresearch/ASB

**Project:** Agent Security Bench (ASB)

**What it Implements:**
ASB is an open-source framework for systematically evaluating attacks and defenses against LLM-based agents. The implementation includes multiple attack types, defensive methods, agent scenarios, tools, memory components, and evaluation mechanisms. The official repository describes attacks including direct prompt injection, indirect prompt injection, Plan-of-Thought backdoors, and memory poisoning.

The associated research evaluates agents across **10 scenarios, 10 agents, more than 400 tools, 23 attack/defense methods, and 8 evaluation metrics**.

**Why It Is Relevant:**
ASB is one of the most directly relevant implementations for this research because it evaluates security problems occurring at multiple stages of agent execution.

It can be used to investigate:

* Prompt injection
* Tool-use attacks
* Memory poisoning
* Planning attacks
* Agent security
* Defensive mechanisms
* Vulnerabilities across agent execution stages

**Research Connection:**
Your paper identifies Agent Security Bench as evidence that security must be evaluated across system prompts, tool usage, memory retrieval, and other components rather than treating security as a property of the underlying LLM alone.

**Key Research Area:**
`Prompt / Memory → Agent Planning → Tool Use → Attack → Defense`

---

## 5. ReAct

**Repository / Implementations:**
https://github.com/ysymyth/ReAct

**Project:** ReAct: Synergizing Reasoning and Acting in Language Models

**What it Implements:**
ReAct implements the reasoning-and-acting paradigm in which a language model alternates between reasoning steps and actions that interact with an external environment. The approach allows observations obtained from an environment to influence subsequent actions.

**Why It Is Relevant:**
ReAct is foundational for understanding the execution structure behind tool-using agents. A chained tool-calling agent can be viewed as a sequence in which an action produces an observation, which then influences the next action.

This makes ReAct useful for studying:

* Reasoning and action loops
* Tool interaction
* Observation handling
* Sequential decision making
* Planning
* Error propagation

**Research Connection:**
Your research paper explains that ReAct established an influential approach in which reasoning and acting are interleaved, allowing observations from an external environment to influence subsequent actions.

**Key Research Area:**
`Reasoning → Action → Observation → Reasoning → Action`

---

# Implementation Comparison

| Implementation           | Main Focus                             | Major Research Connection                      |
| ------------------------ | -------------------------------------- | ---------------------------------------------- |
| **AgentDojo**            | Agent security and prompt injection    | Untrusted tool output and security failures    |
| **ToolBench / ToolLLM**  | Tool learning and multi-tool execution | Tool selection, planning and error propagation |
| **Gorilla**              | API/tool invocation                    | API selection and parameter errors             |
| **Agent Security Bench** | Agent attacks and defenses             | Prompt injection, memory and tool security     |
| **ReAct**                | Reasoning + acting                     | Sequential tool interaction and planning       |

---

# Why These Implementations Were Selected

The five implementations were selected because they represent different layers of the research problem.

**ReAct** provides the conceptual foundation for reasoning and acting through external environments.

**Gorilla** focuses on reliable API invocation and therefore addresses the tool-selection and parameter-generation stages of an agent workflow.

**ToolBench / ToolLLM** extends tool use to large collections of real-world APIs and multi-tool scenarios, making it suitable for investigating chained execution.

**AgentDojo** provides realistic environments for studying prompt injection and tool-integrated agent security.

**Agent Security Bench** provides a broader security evaluation framework covering multiple attack surfaces, tools, memory, and agent scenarios.

Together, these implementations cover the main execution path studied in this research:

**Planning → Tool Selection → Parameter Generation → Tool Execution → Observation → Next Action → Security Check → Recovery / Human Checkpoint**

This makes the collection useful for understanding not only whether an agent produces a correct final answer, but also **where and how failures occur during the execution chain**.

