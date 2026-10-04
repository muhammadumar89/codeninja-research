# codeninja-research-mcp

An MCP server that gives coding agents the **Vertical-Driven Architectures**: complete reference architectures for physical AI in ports, grids, mills, plants and construction sites. Each design says what to sense, where each model runs, what the object model holds, which open-weight models and hardware it needs, what it costs over three years, and who approves every action.

Every design was reasoned on [Praxis](https://muhammadumar89.github.io/codeninja-research/praxis/) and ships an object model in the `hyper-ontology/1` format for [Hyper Ontology](https://muhammadumar89.github.io/codeninja-research/hyper-ontology/). Papers, object models and data are CC BY 4.0; cite the design's DOI.

## Tools

| Tool | What it returns |
|---|---|
| `list_designs(sector, country)` | Every design, filterable, with DOI and object counts |
| `get_design(design_id)` | Summary, object model, model and hardware register with reasons, cost lines, write paths, human approval loop |
| `read_paper(design_id, page)` | The full paper as text, paged |
| `find(text)` | Where a model, system, regulation or object appears across all designs |
| `about_praxis_and_hyper_ontology()` | Where the designs come from, and how to request access |

The server reads the published dataset at call time, so it always serves the latest designs. Set `CODENINJA_RESEARCH_DATA` to a local `dataset/` folder to run offline.

## Install

With [uv](https://docs.astral.sh/uv/):

```json
{
  "mcpServers": {
    "codeninja-research": {
      "command": "uvx",
      "args": ["--from", "git+https://github.com/muhammadumar89/codeninja-research#subdirectory=mcp-server", "codeninja-research-mcp"]
    }
  }
}
```

Claude Code:

```bash
claude mcp add codeninja-research -- uvx --from "git+https://github.com/muhammadumar89/codeninja-research#subdirectory=mcp-server" codeninja-research-mcp
```

With pip: `pip install "git+https://github.com/muhammadumar89/codeninja-research#subdirectory=mcp-server"`, then use `codeninja-research-mcp` as the command.

## Ask it

- "Which designs run vision at the edge, and on what hardware?"
- "Show me the object model for the container terminal design and turn it into Postgres tables."
- "What does it cost to own versus rent the GPUs for the wildfire design?"

Licence: code Apache-2.0; data CC BY 4.0. By [CodeNinja](https://codeninjaconsulting.com).
