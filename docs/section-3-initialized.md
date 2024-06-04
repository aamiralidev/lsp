# Initialized

The `initialized` notification in the Language Server Protocol (LSP) is sent by the client to the server after the server has started successfully. It indicates that the client is ready to send further requests or notifications. 

## Purpose

The `initialized` command provides a synchronization point between the client and the server after the `initialize` request and before any other requests or notifications are sent.

## Example Scenario

For example, a client starts an LSP server to provide IDE like features for a Python project. After the server has started and responded to the `initialize` request, the client will send the `initialized` notification.

## Request Structure

The `initialized` notification doesn't have any parameters.

**Request:**

```json
{
  "jsonrpc": "2.0",
  "method": "initialized",
  "params": {}
}
```

In this request:
- `method` is the name of the LSP method which is being invoked by the client.
- `params` is empty as this notification does not include any parameters.

## Response Structure

Since the `initialized` notification does not require a response, there is no formal response structure for it. However, it might trigger specific server-initiated notifications or requests.

## Response

No formal response is expected to the `initialized` notification. However, server-initiated requests or notifications based on this could look like:

```json
{
  "jsonrpc": "2.0",
  "method": "workspace/configuration",
  "params": {
    "items": [
      {
        "section": "python"
      }
    ]
  }
}
```

In this response:
- `method` specifies the type of notification or request initiated by the server in response to the `initialized` notification.
- `params` contains the parameters required by the `workspace/configuration` method. Here, it s requesting the configuration of the python interpreter used.

## Summary

The `initialized` notification in LSP is a reminder to the server that the client is ready to send further requests, starting from this point. It doesn't require a direct response but may trigger server-initiated requests or notifications.