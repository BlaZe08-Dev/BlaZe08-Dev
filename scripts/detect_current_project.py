#!/usr/bin/env python3
"""Detect the user's active GitHub project and update the profile README + hero."""
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

OWNER = "BlaZe08-Dev"
USERNAME = "BlaZe08-Dev"
IST = ZoneInfo("Asia/Kolkata")
API = "https://api.github.com"
TOKEN = os.environ["GITHUB_TOKEN"]
OVERRIDE_INPUT = os.environ.get("PROJECT_OVERRIDE", "").strip()

PROJECTS = {
    "MiniCloud": {
        "repo": "BlaZe08-Dev/MiniCloud",
        "url": "https://github.com/BlaZe08-Dev/MiniCloud",
        "subtitle": "Distributed job execution · Go · PostgreSQL",
    },
    "Harmoniq": {
        "repo": "BlaZe08-Dev/Harmoniq",
        "url": "https://github.com/BlaZe08-Dev/Harmoniq",
        "subtitle": "Music discovery · Flask · JavaScript",
    },
    "Kavach Pay": {
        "repo": "raunaksahahere/kavachPay",
        "url": "https://github.com/raunaksahahere/kavachPay",
        "subtitle": "Payment risk analysis · Next.js · PostgreSQL",
    },
    "WebThreatDetection": {
        "repo": "raunaksahahere/webThreatDetection",
        "url": "https://github.com/raunaksahahere/webThreatDetection",
        "subtitle": "Evidence-based web threat investigation",
    },
    "RogueSignal": {
        "repo": "raunaksahahere/RogueSignal",
        "url": "https://github.com/raunaksahahere/RogueSignal",
        "subtitle": "Multiplayer social deduction · Game systems",
    },
    "LoopSpill": {
        "repo": "raunaksahahere/LoopSpill",
        "url": "https://github.com/raunaksahahere/LoopSpill",
        "subtitle": "Satellite oil-spill detection · AIS attribution",
    },
    "LoopSatellite": {
        "repo": "raunaksahahere/LoopSatellite",
        "url": "https://github.com/raunaksahahere/LoopSatellite",
        "subtitle": "Wetland monitoring · Earth observation",
    },
}
# JOCKY is intentionally excluded: it is private and belongs to another owner.
# A profile-repository GITHUB_TOKEN cannot read another user's private repository.

def api_get(url):
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/vnd.github+json",
            "Authorization": f"Bearer {TOKEN}",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "BlaZe08-Dev-current-project-detector",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return json.loads(response.read().decode("utf-8"))
    except urllib.error.HTTPError as error:
        if error.code in (403, 404):
            print(f"Skipping inaccessible repository ({error.code}): {url}")
            return []
        raise

def parse_dt(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00"))

def collect_activity(now):
    since = (now - timedelta(days=8)).astimezone(timezone.utc).isoformat().replace("+00:00", "Z")
    activity = {}
    for name, config in PROJECTS.items():
        daily = 0
        weekly = 0
        latest = None
        for page in range(1, 11):
            query = urllib.parse.urlencode({
                "author": USERNAME,
                "since": since,
                "per_page": 100,
                "page": page,
            })
            commits = api_get(f"{API}/repos/{config['repo']}/commits?{query}")
            if not commits:
                break
            for item in commits:
                author = (item.get("author") or {}).get("login", "")
                parents = item.get("parents") or []
                if author.lower() != USERNAME.lower() or len(parents) > 1:
                    continue
                commit_data = item.get("commit") or {}
                author_data = commit_data.get("author") or {}
                date_text = author_data.get("date")
                if not date_text:
                    continue
                committed_at = parse_dt(date_text).astimezone(IST)
                if committed_at > now:
                    continue
                if committed_at >= now - timedelta(days=7):
                    weekly += 1
                    if latest is None or committed_at > latest:
                        latest = committed_at
                if committed_at.date() == now.date():
                    daily += 1
            if len(commits) < 100:
                break
        activity[name] = {
            "today": daily,
            "seven_days": weekly,
            "latest": latest,
        }
        print(f"{name}: {daily} today, {weekly} in rolling 7 days")
    return activity

def main():
    now = datetime.now(IST)
    state_path = Path(".automation-state/current-project-state.json")
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state = json.loads(state_path.read_text()) if state_path.exists() else {
        "current_project": None, "manual_override": None
    }

    # Manual workflow_dispatch selection persists until the user chooses "auto".
    if OVERRIDE_INPUT:
        if OVERRIDE_INPUT == "auto":
            state["manual_override"] = None
        elif OVERRIDE_INPUT in PROJECTS:
            state["manual_override"] = OVERRIDE_INPUT
        else:
            raise SystemExit(f"Unknown manual project selection: {OVERRIDE_INPUT}")

    activity = collect_activity(now)
    eligible = [
        name for name, values in activity.items()
        if values["today"] >= 10
    ]
    eligible.sort(
        key=lambda name: (
            activity[name]["today"],
            activity[name]["seven_days"],
            activity[name]["latest"] or datetime.min.replace(tzinfo=IST),
        ),
        reverse=True,
    )

    if state.get("manual_override") in PROJECTS:
        current = state["manual_override"]
        mode = "MANUAL OVERRIDE"
    elif eligible:
        current = eligible[0]
        mode = "AUTO DETECTED"
    else:
        current = state.get("current_project") if state.get("current_project") in PROJECTS else None
        mode = "RETAINED" if current else "WAITING FOR SIGNAL"

    if current:
        values = activity[current]
        latest = values["latest"].strftime("%d %b %Y, %I:%M %p IST") if values["latest"] else "No recent commit"
        config = PROJECTS[current]
        project_label = current
        project_url = config["url"]
        today_label = f"{values['today']} COMMITS TODAY"
        week_label = f"{values['seven_days']} IN 7 DAYS"
        status_label = mode
        subtitle = config["subtitle"]
        hero_badge = "MANUAL" if mode == "MANUAL OVERRIDE" else "AUTO"
        hero_badge_color = "#eda231" if mode == "MANUAL OVERRIDE" else "#8da697"
    else:
        values = {"today": 0, "seven_days": 0, "latest": None}
        project_label = "AWAITING ACTIVITY SIGNAL"
        project_url = f"https://github.com/{OWNER}"
        today_label = "10 COMMITS TO ACTIVATE"
        week_label = "CHECKED HOURLY"
        status_label = "AUTOMATIC DETECTION"
        latest = "No project has reached the daily threshold yet"
        subtitle = "10 qualifying commits in one India-local day"
        hero_badge = "WAITING"
        hero_badge_color = "#eda231"

    signature = json.dumps({
        "current_project": current,
        "mode": mode,
        "today": values["today"],
        "seven_days": values["seven_days"],
        "latest": values["latest"].isoformat() if values["latest"] else None,
    }, sort_keys=True)
    if state.get("published_signature") != signature:
        state["current_project"] = current
        state["daily_threshold"] = 10
        state["published_signature"] = signature
        state["last_published_at"] = now.isoformat(timespec="minutes")
        state_path.write_text(json.dumps(state, indent=2) + chr(10))
    published_at = state.get("last_published_at", now.isoformat(timespec="minutes"))

    # Detection remains private to the workflow cache; nothing is published to the profile.
    print(f"Internal current-project detection: {current or 'none'} ({mode})")

if __name__ == "__main__":
    main()
