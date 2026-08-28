# Datasets and Benchmarks

This section contains datasets and benchmark environments relevant to the study of **failure modes in chained tool-calling agents operating without human checkpoints**. These resources provide realistic tasks, tool-use interactions, API calls, and security scenarios that can be used to evaluate planning, tool selection, error propagation, prompt injection, and agent reliability.

---

## 1. AgentDojo

**Name:** AgentDojo: A Dynamic Environment to Evaluate Prompt Injection Attacks and Defenses for LLM Agents

**Source:** ETH Zürich / Invariant Labs

**Year:** 2024

**Type:** Agent evaluation benchmark and dynamic environment

**Official Repository:**
https://github.com/ethz-spylab/agentdojo

**Paper:**
https://arxiv.org/abs/2406.13352

**Description:**
AgentDojo is a dynamic benchmark designed to evaluate the security and utility of LLM agents that interact with external tools. It provides realistic tasks involving environments such as banking, travel, workspace, and communication-related activities. The benchmark also introduces prompt-injection scenarios in which untrusted information can attempt to influence an agent's behavior.

**Application:**
AgentDojo is particularly useful for studying **indirect prompt injection, tool-output contamination, autonomous tool use, and security failures in multi-step agent workflows**. It can be used to examine whether an agent continues to perform the user's legitimate task when malicious instructions appear in tool outputs. The benchmark supports both attack and defense evaluation.

**Relevance to This Research:**
The benchmark closely matches the research problem because a chained agent may receive untrusted information from one tool and subsequently use that information when deciding what to do with another tool. This makes AgentDojo valuable for investigating how errors or malicious instructions propagate through chained tool calls.

**License / Availability:**
The official implementation is publicly available on GitHub and provides instructions for running the benchmark.

---

## 2. ToolBench

**Name:** ToolBench: An Open Platform for Training, Serving, and Evaluating Large Language Models for Tool Learning

**Source:** OpenBMB

**Year:** 2023

**Type:** Large-scale tool-use dataset and benchmark

**Official Repository:**
https://github.com/OpenBMB/ToolBench

**Paper / Project:**
https://github.com/OpenBMB/ToolBench

**Description:**
ToolBench is a large-scale dataset designed to improve the ability of language models to use real-world APIs and tools. The project collects more than 16,000 real-world APIs from RapidAPI and creates realistic instructions involving these APIs. The dataset contains both single-tool and multi-tool scenarios.

The dataset includes single-tool scenarios as well as multiple-tool scenarios. Multi-tool tasks are organized into different categories, including intra-category and intra-collection multi-tool tasks. The released data contains instructions, answer/solution paths, tool environments, retrieval information, and evaluation data.

**Application:**
ToolBench can be used to train and evaluate LLMs on **tool selection, API retrieval, parameter generation, multi-tool planning, and sequential tool execution**.

**Relevance to This Research:**
ToolBench is highly relevant to chained tool-calling research because multi-tool tasks require an agent to perform several operations sequentially. A failure in tool selection, parameter generation, or intermediate reasoning can affect later steps in the chain. Therefore, ToolBench can support experiments investigating **planning failure, tool-selection failure, parameter errors, and error propagation**.

**Dataset Information:**
The official repository reports thousands of tools and APIs together with large numbers of tool-use instances and reasoning traces.

**License / Availability:**
The project provides the dataset and associated code through its official repository. Researchers should follow the repository's current licensing and data-use conditions before redistribution or modification.

---

## 3. API-Bank

**Name:** API-Bank: A Comprehensive Benchmark for Tool-Augmented LLMs

**Source:** Academic research benchmark

**Year:** 2023

**Type:** Tool-augmented LLM benchmark

**Paper:**
https://arxiv.org/abs/2304.08244

**DOI:**
https://doi.org/10.18653/v1/2023.emnlp-main.187

**Description:**
API-Bank is a benchmark for evaluating the ability of language models to use external APIs. It evaluates several capabilities involved in tool use, including planning, API retrieval, and API calling. The benchmark contains runnable APIs and annotated tool-use dialogues designed to test different aspects of tool utilization.

Your research paper identifies API-Bank as an important benchmark for tool-augmented LLMs and notes that tool utilization involves several distinct competencies rather than one single capability.

**Application:**
API-Bank can be used to evaluate whether an LLM agent can:

* understand a task requiring external tools;
* select an appropriate API;
* retrieve relevant API information;
* generate appropriate API calls;
* interpret API results;
* use tool results in subsequent reasoning.

**Relevance to This Research:**
API-Bank is directly relevant to the study of **tool-selection failure and parameter-generation failure**. A chained agent may successfully execute an API call while still using the wrong tool or incorrect parameters. The resulting output can then become the input to a later operation, creating a downstream failure.

**Research Importance:**
The benchmark is particularly useful because it separates different tool-use competencies. This supports the analysis of failure points within a multi-stage tool-calling pipeline rather than treating the entire agent as a single black box.

---

## Dataset Selection Summary

| Dataset / Benchmark | Main Focus                                 | Relevance to Research                                      |
| ------------------- | ------------------------------------------ | ---------------------------------------------------------- |
| **AgentDojo**       | Agent security, prompt injection, tool use | Prompt injection, untrusted tool output, security failures |
| **ToolBench**       | Large-scale API and multi-tool learning    | Tool selection, planning, parameters, chained execution    |
| **API-Bank**        | Tool-augmented LLM evaluation              | API selection, API calling, planning and tool-use errors   |

---

## Why These Three Resources Were Selected

These three resources complement one another rather than covering exactly the same problem.

**AgentDojo** focuses strongly on the **security side** of tool-using agents, especially prompt injection and malicious information entering through external tools.

**ToolBench** provides a large-scale environment for **single-tool and multi-tool scenarios**, making it useful for studying sequential tool use and the problems that can arise when multiple tool calls are chained together.

**API-Bank** focuses on the different competencies required for **tool-augmented language-model interaction**, including planning, API retrieval, and API calling. Your research paper specifically identifies these as important components of tool-use evaluation.

Together, these resources cover three major dimensions of the research topic:

**Tool Use → Chained Execution → Security and Failure Analysis**

