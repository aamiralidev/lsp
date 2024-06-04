# Workspace / Configuration

The `workspace/configuration` request in the Language Server Protocol (LSP) is used to fetch configuration settings of the workspace.

## Purpose

The `workspace/configuration` command is beneficial for the language server to understand the workspace configuration settings. These settings are typically determined by the client or the user's environment and can influence the functioning of the language server.

## Example Scenario

Consider a scenario where you have a TypeScript language server and the client wants to fetch configuration settings for code formatting. The configuration could include settings like the number of spaces for the tab, whether to use single or double quotes for strings, etc.

## Request Structure

The request for `workspace/configuration` usually includes a list of configuration items that the server wishes to fetch.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "method": "workspace/configuration",
  "params": {
    "items": [
      {
        "scopeUri": "file:///path/to/workspace",
        "section": "typescript.format"
      }
    ]
  }
}
```

In this request:
- `scopeUri` specifies the location of the workspace whose configuration settings are to be fetched.
- `section` is the specific section of the configuration that the server is interested in.

## Response Structure

The response will include a list of configuration values corresponding to each configuration item requested.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 2,
  "result": [
    {
      "insertSpaces": true,
      "tabSize": 2,
      "quoteStyle": "single"
    }
  ]
}
```

In this response:
- `insertSpaces` determines if spaces should be used over tabs.
- `tabSize` specifies the number of spaces to be used for a single tab.
- `quoteStyle` specifies the quoting style for strings.

## Summary

The `workspace/configuration` request in LSP is used to fetch the configuration settings of the specified workspace. This allows the language server to adapt to the specific settings of the client's environment, ensuring consistent behavior across different workspaces.
