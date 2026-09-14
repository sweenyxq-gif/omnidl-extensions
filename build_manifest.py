#!/usr/bin/env python3
"""
OmniDownloader Extensions - Automatic Repository Index Generator
Scans all .user.js files in userscripts/, extracts metadata, and updates extensions.json.
"""

import os
import re
import json
import glob

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
USERSCRIPTS_DIR = os.path.join(SCRIPT_DIR, "userscripts")
OUTPUT_MANIFEST = os.path.join(SCRIPT_DIR, "extensions.json")

RAW_BASE_URL = "https://raw.githubusercontent.com/sweenyxq-gif/omnidl-extensions/main/userscripts"


def parse_userscript_metadata(file_path):
    with open(file_path, "r", encoding="utf-8", errors="replace") as f:
        content = f.read()

    match = re.search(r"//\s*==UserScript==([\s\S]*?)//\s*==/UserScript==", content)
    if not match:
        return None

    header = match.group(1)
    meta = {
        "name": "",
        "namespace": "",
        "version": "1.0.0",
        "description": "",
        "author": "",
        "category": "general",
        "matches": [],
        "includes": [],
        "connects": [],
        "grants": []
    }

    for line in header.splitlines():
        line = line.strip()
        tag_match = re.match(r"^//\s*@([a-zA-Z0-9_\-]+)(?:\s+(.*))?$", line)
        if not tag_match:
            continue

        tag = tag_match.group(1).lower()
        val = (tag_match.group(2) or "").strip()

        if tag == "name" and not meta["name"]:
            meta["name"] = val
        elif tag == "namespace":
            meta["namespace"] = val
        elif tag == "version":
            meta["version"] = val
        elif tag == "description" and not meta["description"]:
            meta["description"] = val
        elif tag == "author":
            meta["author"] = val
        elif tag == "omni-category":
            meta["category"] = val
        elif tag == "match":
            meta["matches"].append(val)
        elif tag == "include":
            meta["includes"].append(val)
        elif tag == "connect":
            meta["connects"].append(val)
        elif tag == "grant":
            meta["grants"].append(val)

    filename = os.path.basename(file_path)
    script_id = f"{meta['namespace']}:{meta['name']}" if meta["namespace"] else meta["name"]

    return {
        "id": script_id,
        "name": meta["name"] or filename,
        "namespace": meta["namespace"],
        "version": meta["version"],
        "category": meta["category"],
        "author": meta["author"] or "OmniDownloader Community",
        "description": meta["description"],
        "filename": filename,
        "scriptUrl": f"{RAW_BASE_URL}/{filename}",
        "matches": meta["matches"],
        "includes": meta["includes"],
        "connects": meta["connects"]
    }


def build_manifest():
    script_files = sorted(glob.glob(os.path.join(USERSCRIPTS_DIR, "*.user.js")))
    extensions = []

    print(f"[*] Scanning {len(script_files)} userscripts in {USERSCRIPTS_DIR}...")
    for sf in script_files:
        data = parse_userscript_metadata(sf)
        if data:
            extensions.append(data)
            print(f"  + [{data['category']}] {data['name']} (v{data['version']})")
        else:
            print(f"  ! Skipped invalid userscript: {os.path.basename(sf)}")

    manifest = {
        "name": "OmniDownloader Extension Repository",
        "version": "1.0.0",
        "description": "Official and community-curated resolver extensions for OmniDownloader",
        "homepage": "https://github.com/sweenyxq-gif/omnidl-extensions",
        "totalExtensions": len(extensions),
        "extensions": extensions
    }

    with open(OUTPUT_MANIFEST, "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)

    print(f"[+] Successfully wrote {len(extensions)} extensions to {OUTPUT_MANIFEST}")


if __name__ == "__main__":
    build_manifest()
