# Agentic tools stack: core tools and workflows

Curated by @aunysillyme · Reviewed 2026-11-28

Source: https://code.claude.com/docs/en/overview

## Core tools (18)

- **[Claude Code](https://code.claude.com/docs/en/overview):** Freemium. Agentic coding tool that reads a repo, edits files, and runs commands in the terminal, IDE, desktop app, or browser.
- **[Claude Code subagents](https://code.claude.com/docs/en/sub-agents):** Freemium. Specialized workers inside one Claude Code session. Each returns a summary instead of filling the main context.
- **[Claude Code agent teams](https://code.claude.com/docs/en/agent-teams):** Freemium. Experimental teams of Claude Code sessions with a shared task list and messages between teammates. Off unless enabled.
- **[Claude Code dynamic workflows](https://code.claude.com/docs/en/workflows):** Freemium. Scripted orchestration that runs many Claude Code subagents and cross-checks their results.
- **[Claude Agent SDK](https://code.claude.com/docs/en/agent-sdk/overview):** Freemium. Python and TypeScript library for the Claude Code agent loop, tools, permissions, and sessions.
- **[Model Context Protocol](https://modelcontextprotocol.io/):** Free. Open protocol for connecting agents to tools and data.
- **[MCP reference servers](https://github.com/modelcontextprotocol/servers):** Free. Official reference MCP servers maintained with the protocol.
- **[GitHub MCP server](https://github.com/github/github-mcp-server):** Free. GitHub's official MCP server for repository, issue, and pull request tools.
- **[Playwright MCP](https://github.com/microsoft/playwright-mcp):** Free. Microsoft's MCP server that lets an agent drive a browser through Playwright.
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli):** Free. Open-source terminal agent that brings Gemini into the shell. API usage is billed by Google.
- **[Google ADK](https://adk.dev/):** Free. Open-source Agent Development Kit for building, debugging, and deploying agents.
- **[Jules](https://jules.google/):** Freemium. Google's autonomous coding agent that plans a change in a GitHub repo and opens a pull request.
- **[OpenAI Codex](https://openai.com/codex/):** Freemium. OpenAI coding agent for planning, building, reviewing, and shipping code across ChatGPT, the editor, and the terminal.
- **[Cursor](https://cursor.com/):** Freemium. AI coding agent and editor for handing tasks to agents inside a repository.
- **[LangGraph](https://www.langchain.com/langgraph):** Free. Open framework for durable agent workflows, memory, streaming, and human review.
- **[CrewAI](https://crewai.com/):** Freemium. Framework and platform for crews of agents that share a task.
- **[AutoGen](https://github.com/microsoft/autogen):** Free. Microsoft's open programming framework for agentic applications.
- **[OpenHands](https://docs.openhands.dev/):** Freemium. Open-source coding agent with a cloud option that can work from GitHub issues.

## Workflows (2)

### Delegate a repo change with subagents and MCP

Source: https://code.claude.com/docs/en/sub-agents

1. Write the task, the files in scope, and the check that shows the change worked.
2. In Claude Code, send the search or test work to a subagent so the main session keeps the summary rather than the raw logs.
3. Connect an MCP server such as the GitHub server or Playwright when the task needs issues, pull requests, or a browser.
4. For a larger split, use an agent team or a dynamic workflow, then read the diff before merging.
5. When the same loop should run inside an application, move it to the Claude Agent SDK and keep the permission list explicit.

### Sketch the same task in two agent frameworks

Source: https://adk.dev/

1. Write one task, the tools it may call, and a check for a good result.
2. Build a short version in Google ADK and another in LangGraph, CrewAI, or AutoGen.
3. Run both on the same example and compare the trace, the tool calls, and the final answer.
4. Keep the version a teammate can rerun, and record which framework produced it.
