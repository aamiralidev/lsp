# Window / Show Message Request

The `window/showMessageRequest` command in the Language Server Protocol (LSP) is used to send a message to the user from the server and requests the client to provide a response based on the provided actions.

## Purpose

The `window/showMessageRequest` command is used to send a popup notification message from the server to the user; it can also be used to ask questions with a pre-defined set of responses. This aids in human-friendly communication between the server and the user.

## Example Scenario

For instance, the server might send a `window/showMessageRequest` to announce that an analysis of the codebase has been completed, and perhaps offer several actions to the user such as viewing the analysis report or ignoring it.

## Request Structure

The request for `window/showMessageRequest` typically includes the type of message and the message itself. Also, an array of `MessageActionItem` is included to provide actions that the user can take.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "window/showMessageRequest",
  "params": {
    "type": 3,  // Info
    "message": "Analysis complete.",
    "actions": [
      {
        "title": "View Report"
      },
      {
        "title": "Ignore"
      }
    ]
  }
}
```

In this request:
- `type` specifies the type of message (in this case, an info message).
- `message` is the content of the message.
- `actions` is an array of `MessageActionItem` objects, which the client can select from.

## Response Structure

The response from the `window/showMessageRequest` will be the action selected (if any) by the user.

**Response:**

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "title": "View Report"
  }
}
```

In this response:
- `title` indicates the selected action by the user. If no `MessageActionItem` was chosen, `null` will be passed.

## Summary

The `window/showMessageRequest` request in LSP is used by the server to send a popup notification message to the user, allowing for intuitive human-friendly interaction. The request may also include options for user actions, the responses to which can be used by the server for further processing.