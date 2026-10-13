# Optional reusable Ask panel patches

These patches address general Shell surfaces used by any App Hub application.
TrendyHear's formal bundle remains compatible with the official Shell and does
not contain or silently apply Shell changes.

## 0002: submit a free-text answer to `ask_user_question`

`0002-ask-question-free-text-submit.patch` fixes the Ask panel's composer
button while an Agent is waiting on `ask_user_question`. The Shell already
routes typed text to the open question, but the button was rendered as **Stop**
because the parked Agent turn was still considered running. A person who typed
an answer outside the suggested options, such as `12:00`, then interrupted the
turn instead of answering it.

The patch gives an open question priority over the generic running state:

- empty composer: **Answer** is disabled;
- typed composer: **Answer** submits the free-text answer through the existing
  `user_question/respond` path;
- a running turn without an open question still shows **Stop**.

It changes no Agent permissions, question ownership, or app API. The included
unit test covers the reported `12:00` case.

Apply and verify from a matching OctoSense checkout:

```sh
git apply /path/to/TrendyHear/build/shell-patches/0002-ask-question-free-text-submit.patch
cargo test -p octosense-shell an_open_question_turn_submits_the_free_text_answer --lib
```

## 0001: open the focused app's Ask panel

TrendyHear's Agent workflow uses the official Shell-owned **Ask TrendyHear**
panel. The application does not start a second conversation or ship a chat UI.

The current Android Shell has no app-facing touch control that reveals the
existing `Ask <app>` panel. `0001-open-focused-app-ask-panel.patch` adds one
optional argument to the existing contained-app service:

```splash
host.request("octos.session.open", {show: true}, fn(r) { ... })
```

The request remains bound to the authenticated calling app. The Shell opens
the panel only when that same app is currently focused. An app cannot name or
open another app's Agent. All existing `{}` calls keep their behavior.

This patch is a convenience enhancement for TrendyHear's green shortcut. The
core Agent workflow remains usable on an unmodified official Shell from the
system's `Ask TrendyHear` entry.

### Apply and verify

From an OctoSense checkout matching the version documented in the project
README:

```sh
git apply /path/to/TrendyHear/build/shell-patches/0001-open-focused-app-ask-panel.patch
cargo test --locked -p octosense-ai-host contained::tests::contained_open_may_request_the_shell_owned_ask_surface -- --exact
cargo check --locked -p octosense-shell
```

The patch changes only the contained Octos service, one focused-app Shell
bridge, its focused test, and the matching English and Chinese service docs.
