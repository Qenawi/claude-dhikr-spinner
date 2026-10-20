---
name: islamic-dhikr-spinner
description: Applies a fixed set of short Islamic dhikr/du'a phrases (Arabic) as Claude Code's spinner status words, replacing the default whimsical English verbs. Use when a user asks to install, apply, or share the "Islamic spinner", "dhikr spinner", or "ad3ya spinner" words.
---

# Islamic Dhikr Spinner

Claude Code shows a random word next to its spinner while it works (e.g. "Pondering…", "Flibbertigibbeting…"). This is controlled by the `spinnerVerbs` setting. This skill replaces that list with 20 short Islamic dhikr/du'a phrases in Arabic.

## What gets written

This skill merges the following into the user's **global** `~/.claude/settings.json` (every other existing key in that file must be left untouched):

```json
{
  "spinnerVerbs": {
    "mode": "replace",
    "verbs": [
      "سبحان الله",
      "الحمد لله",
      "الله أكبر",
      "لا إله إلا الله",
      "لا حول ولا قوة إلا بالله",
      "أستغفر الله",
      "بسم الله",
      "ما شاء الله",
      "إن شاء الله",
      "سبحان الله وبحمده",
      "حسبي الله",
      "توكلت على الله",
      "ربي اغفر لي",
      "رب ارحمني",
      "رب زدني علما",
      "رب يسر ولا تعسر",
      "حسبنا الله ونعم الوكيل",
      "اللهم بارك",
      "رب اشرح لي صدري",
      "اللهم آمين"
    ]
  }
}
```

`mode: "replace"` means only these phrases are shown — Claude Code's default English verbs are fully replaced, not mixed in.

## Steps to apply

1. Read `~/.claude/settings.json`. If the file doesn't exist, start from `{}`.
2. Set/overwrite only the `spinnerVerbs` key to the value above. Every other key in the file must survive unchanged (theme, plugins, autoMode config, etc.).
3. Write the file back as valid UTF-8 JSON with 2-space indentation. Write the Arabic text as literal UTF-8 characters — do not escape it as `\uXXXX`.
4. Tell the user in one line that it's applied and takes effect on their next Claude Code session (the current session's spinner won't change retroactively).

## Notes for engineers reusing this skill

- Since 1.1.0, the plugin's SessionStart hook (`scripts/apply_spinner.py`) writes this list automatically when `spinnerVerbs` is missing. Use this skill to force the list over an existing `spinnerVerbs` value, or to re-apply it.
- If you change the phrase list, update it both here and in `scripts/apply_spinner.py`.

- This is a **global** setting — it changes every Claude Code session for that user's machine, not just one project.
- Re-running this skill is safe — it just overwrites the `spinnerVerbs` key again.
- To remove it later, uninstall the plugin first, then delete the `spinnerVerbs` key from `~/.claude/settings.json`. If the plugin is still installed, the hook adds the key back.
- To use a different word list instead of this fixed one, edit `verbs` directly, or ask Claude: "change my spinnerVerbs to append with [words]". The schema is `{ mode: "append" | "replace", verbs: string[] }` — `append` adds to Claude Code's built-in whimsical list, `replace` shows only your words.
- To share this with a teammate: `/plugin marketplace add Qenawi/claude-dhikr-spinner` then `/plugin install islamic-dhikr-spinner@dhikr-spinner`.
