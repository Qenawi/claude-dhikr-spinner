# Islamic Dhikr Spinner (Claude Code plugin)

Replaces Claude Code's spinner words ("Pondering…", "Flibbertigibbeting…") with 20 short dhikr/du'a phrases in Arabic.

## Install

```
/plugin marketplace add Qenawi/claude-dhikr-spinner
/plugin install islamic-dhikr-spinner@dhikr-spinner
```

Then ask Claude: **"apply the dhikr spinner"**. It writes `spinnerVerbs` into `~/.claude/settings.json`.
Restart Claude Code to see it.

## Remove

Delete the `spinnerVerbs` key from `~/.claude/settings.json`, then `/plugin uninstall islamic-dhikr-spinner@dhikr-spinner`.
