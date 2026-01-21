---
layout: page
title: How to Save Logs From Your LLM
permalink: /tutorials/llm-logs.html
parent: Tutorials
nav_order: 1
---

It is a **requirement** for all [project assignments](../projects) that you submit
logs of all of your interactions with your AI assistant(s), not just the final result.
This page contains information about how to gather the required logs from different
model providers, but it is ultimately _your responsibility_ to submit the required logs.

The logs you submit should include, for every project member:
* a record of each prompt you sent to the model
* a record of the model's output
* a record of the results of any tools that the model ran (e.g., if the model ran your project's tests and looked at the terminal output, you'd need to make sure the terminal output is included in the log)

The rest of this page is arranged by model provider. If your preferred model provider
isn't present, we encourage you to try to figure out how to get the required logs on
your own and then let us know how you did so, so that other students can benefit from
your exploration.

### Google Gemini Code Assist

See [this page from Google](https://developers.google.com/gemini-code-assist/docs/configure-logging).

### GitHub Copilot in VS Code

[GitHub Copilot in VS Code](https://code.visualstudio.com/docs/copilot/overview) makes it easier to provide LLMs with context files since it is embedded within the IDE.
You can register for your free GitHub Pro account [here](https://github.com/education/students) and use GitHub Copilot Pro for free.

Exporting your LLM chat logs is straightforward as well. 
Run `Chat: Export Chat...` command from the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) in VS Code will do the trick.
However, note that you ***must use a chat session*** to interact with the LLM because ***only chat session logs can be exported***.
You can refer to the details [here](https://code.visualstudio.com/docs/copilot/chat/chat-sessions)

### ChatGPT

ChatGPT also provides an option for you to export your logs. First, you need an OpenAI account. 
Your chat history can be exported by going to Profile &rarr; Data controls &rarr; Export data. 
You will then receive an email containing a link to download your chat history.
The process is not as straightforward as GitHub Copilot's.
You can refer to the details [here](https://help.openai.com/en/articles/7260999-how-do-i-export-my-chatgpt-history-and-data)

### Cursor

[Cursor](https://cursor.com/students) is free for students as well. However, it does not provide native support for exporting logs. It requires third-party tools to do so.