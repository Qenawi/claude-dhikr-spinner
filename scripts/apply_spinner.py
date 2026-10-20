#!/usr/bin/env python3
"""Add the dhikr spinnerVerbs to ~/.claude/settings.json if the key is missing.

Runs on SessionStart. Never overwrites an existing spinnerVerbs value, never
rewrites a settings file it cannot parse, and always exits 0.
"""
import json
import os
import sys
import tempfile

SPINNER_VERBS = {
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
        "اللهم آمين",
    ],
}


def main():
    config_dir = os.environ.get("CLAUDE_CONFIG_DIR") or os.path.expanduser("~/.claude")
    path = os.path.join(config_dir, "settings.json")

    settings = {}
    if os.path.exists(path):
        try:
            with open(path, encoding="utf-8") as f:
                settings = json.load(f)
        except (OSError, ValueError):
            return
        if not isinstance(settings, dict):
            return

    if "spinnerVerbs" in settings:
        return

    settings["spinnerVerbs"] = SPINNER_VERBS
    os.makedirs(config_dir, exist_ok=True)
    fd, tmp = tempfile.mkstemp(dir=config_dir, prefix=".settings.", suffix=".json")
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(settings, f, ensure_ascii=False, indent=2)
            f.write("\n")
        os.replace(tmp, path)
    except OSError:
        try:
            os.unlink(tmp)
        except OSError:
            pass
        return

    print("Dhikr spinner applied to ~/.claude/settings.json; it shows from your next session.")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass
    sys.exit(0)
