<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="assets/logo-dark.svg">
    <img src="assets/logo.svg" width="160" alt="A ring of 33 prayer beads around the words سبحان الله">
  </picture>
</p>

# Islamic Dhikr Spinner (Claude Code plugin)

Replaces Claude Code's spinner words ("Pondering…", "Flibbertigibbeting…") with 20 short dhikr/du'a phrases in Arabic.

## Install

```
/plugin marketplace add Qenawi/claude-dhikr-spinner
/plugin install islamic-dhikr-spinner@dhikr-spinner
```

The plugin's first session writes `spinnerVerbs` into `~/.claude/settings.json` through a SessionStart hook. Start another session to see the new spinner, because Claude Code reads settings at startup. The hook needs `python3`.

The hook only adds the key when it's missing, so it never replaces a `spinnerVerbs` list you already set. To force the dhikr list, ask Claude to **"apply the dhikr spinner"**.

## Remove

Run `/plugin uninstall islamic-dhikr-spinner@dhikr-spinner` first, then delete the `spinnerVerbs` key from `~/.claude/settings.json`. If you delete the key while the plugin is still installed, the hook adds it again at the next session start.
