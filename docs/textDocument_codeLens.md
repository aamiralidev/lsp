# Text Document / Code Lens

The `textDocument/codeLens` request in the Language Server Protocol (LSP) is used for gathering metadata information, typically useful for a specific point of view like code references, error information, etc. Each lens typically shows up in the places like above function definitions.

## Purpose

The `textDocument/codeLens` command assists developers by providing high-level context. This can include references, implemented interface members, test metadata, error details, etc. 

## Example Scenario

Assuming you have a function named `calculateSum` in a file called `main.ts`. You want to find all the references and other metadata related to `calculateSum` to gain more high-level context while coding.

## Request Structure

The request for `textDocument/codeLens` contains a text document identifier pointing to the file of interest.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "textDocument/codeLens",
  "params": {
    "textDocument": {
      "uri": "file:///path/to/main.ts"
    }
  }
}
```

In this request:
- `uri` specifies the location of the file.

## Response Structure

The response will include a list of code lens items relevant to the requested file. 

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": [
    {
      "range": {
        "start": {
          "line": 12,
          "character": 0
        },
        "end": {
          "line": 14,
          "character": 2
        }
      },
      "command": {
        "title": "References",
        "command": "editor.action.showReferences",
        "arguments": [
          {
            "uri": "file:///path/to/main.ts",
            "position": {
              "line": 13,
              "character": 9
            }
          },
          [
            {
              "uri": "file:///path/to/util.ts",
              "range": {
                "start": {
                  "line": 20,
                  "character": 7
                },
                "end": {
                  "line": 20,
                  "character": 19
                }
              }
            }
          ]
        ]
      }
    }
  ]
}
```

In this response:
- `range` indicates the range in the document from where the CodeLens applies.
- `command` specifies a command which can be executed. Here, it shows the references to the `calculateSum` function.
- `title` provides a short, human-readable description of the command.
- `command` defines the identifier of the command to be executed when selected.
- `arguments` provides additional contextual arguments when executing the command.

## Summary

The `textDocument/codeLens` command in LSP provides a high-level point of view (usually above the function definitions) which provides additional meta-information such as references, implementation counts, or test statuses and error details. This greatly helps developers in gaining context within the code.