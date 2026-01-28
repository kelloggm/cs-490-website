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

[This page from Google](https://developers.google.com/gemini-code-assist/docs/configure-logging) describes the _best_ way to export logs, but it requires your Google account to be enterprise-level.
Most personal accounts can't access this feature.

[Google Takeout](https://takeout.google.com/) can export the logs of chat sessions via the web interface. Make a takeout request and uncheck everything except "My Activity". Click on the "All activity data included" button and uncheck everything _except_ "Gemini Apps".

For the [Gemini CLI](https://github.com/google-gemini/gemini-cli), it's straightforward to collect logs, since it saves them locally: one MacOS or Linux, in `~/.gemini/tmp/`, and on Windows in `%USERPROFILE%\.gemini\tmp\`. Inside that folder, you will see subdirectories with long hexadecimal names (e.g., `4ebf39`...). Find the ones associated with whatever you're working on, and then inside each of those, look for `logs.json`. Submit these `.json` files. If you use the command `/chat save [tag]`, it creates a file named `checkpoint-[tag].json` in that same directory, which makes it more convenient to find a particular record.

For Gemini use via an IDE, you have to recover the logs from the IDE itself. This varies by IDE; if you figure out how to do it for your IDE, let us know, and we'll add instructions here.

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