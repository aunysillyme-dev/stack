# Agentic tools

Coding agents, the Claude Agent SDK, the Model Context Protocol, and frameworks for multi-step work. Reviewed 2026-11-28. Each entry below is name, link, one-line description, and a `free`, `freemium`, or `paid` tag.

Claude Code documents subagents, experimental agent teams, and dynamic workflows for running many subagents from a script. No separate official page titled "swarms" was found, so the scale path is listed as dynamic workflows.

This stack has no separate illustrated guide yet.

- **Core tools and workflows:** [canonical.md](canonical.md) (plain text) · [canonical.json](canonical.json)
- **Full inventory (18):** [inventory.md](inventory.md) (plain text) · [inventory.json](inventory.json)
- **Resources by tier:** [free/](free/free.md) (`8`, [JSON](free/free.json)) · [freemium/](freemium/freemium.md) (`10`, [JSON](freemium/freemium.json)) · [premium/](premium/premium.md) (`0`, [JSON](premium/premium.json))
- **Community workflows:** [community/](community/). [Submit a workflow](../CONTRIBUTING.md).
- **Category metadata:** [stack.json](stack.json)

## Coding agents

- [Claude Code](https://code.claude.com/docs/en/overview): Agentic coding tool that reads a repo, edits files, and runs commands in the terminal, IDE, desktop app, or browser. `freemium`
- [Claude Code subagents](https://code.claude.com/docs/en/sub-agents): Specialized workers inside one Claude Code session. Each returns a summary instead of filling the main context. `freemium`
- [Claude Code agent teams](https://code.claude.com/docs/en/agent-teams): Experimental teams of Claude Code sessions with a shared task list and messages between teammates. Off unless enabled. `freemium`
- [Claude Code dynamic workflows](https://code.claude.com/docs/en/workflows): Scripted orchestration that runs many Claude Code subagents and cross-checks their results. `freemium`
- [Gemini CLI](https://github.com/google-gemini/gemini-cli): Open-source terminal agent that brings Gemini into the shell. API usage is billed by Google. `free`
- [Jules](https://jules.google/): Google's autonomous coding agent that plans a change in a GitHub repo and opens a pull request. `freemium`
- [OpenAI Codex](https://openai.com/codex/): OpenAI coding agent for planning, building, reviewing, and shipping code across ChatGPT, the editor, and the terminal. `freemium`
- [Cursor](https://cursor.com/): AI coding agent and editor for handing tasks to agents inside a repository. `freemium`
- [OpenHands](https://docs.openhands.dev/): Open-source coding agent with a cloud option that can work from GitHub issues. `freemium`

## SDK, protocol, and servers

- [Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview): Python and TypeScript library for the Claude Code agent loop, tools, permissions, and sessions. `freemium`
- [Model Context Protocol](https://modelcontextprotocol.io/): Open protocol for connecting agents to tools and data. `free`
- [MCP reference servers](https://github.com/modelcontextprotocol/servers): Official reference MCP servers maintained with the protocol. `free`
- [GitHub MCP server](https://github.com/github/github-mcp-server): GitHub's official MCP server for repository, issue, and pull request tools. `free`
- [Playwright MCP](https://github.com/microsoft/playwright-mcp): Microsoft's MCP server that lets an agent drive a browser through Playwright. `free`

## Frameworks

- [Google ADK](https://adk.dev/): Open-source Agent Development Kit for building, debugging, and deploying agents. `free`
- [LangGraph](https://www.langchain.com/langgraph): Open framework for durable agent workflows, memory, streaming, and human review. `free`
- [CrewAI](https://crewai.com/): Framework and platform for crews of agents that share a task. `freemium`
- [AutoGen](https://github.com/microsoft/autogen): Microsoft's open programming framework for agentic applications. `free`

## How an agent task runs

1. Write the task, the files in scope, and the check that shows it worked.
2. Keep search and test logs in a subagent or a second framework run so the main session keeps the summary.
3. Connect an MCP server when the task needs GitHub or a browser.
4. Read the diff or the trace before you keep the result.

[Browse community workflows](community/) · [Category metadata](stack.json)
