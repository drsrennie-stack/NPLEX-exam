# Video pass instructions

You add verified YouTube videos to study units that have an empty "videos" list. Accuracy rule: a link goes in only if you verified it. Never construct or guess a video ID.

## Scope
- Your assigned file is content/<sys>/units-<n>.json. Work only on units in it whose "videos" is an empty list. Do not change any other field or any unit that already has videos.
- Read each unit's "id", "summary", and the unit title in nplex-competencies.js so you know the topic.

## Channels (only these)
- Ninja Nerd
- Khan Academy (including Khan Academy Medicine)
- Armando Hasudungan
- Dr. Najeeb Lectures (YouTube uploads only)

## How to find and verify
1. Search with WebSearch, for example: `Ninja Nerd adrenal gland physiology youtube`. Budget: at most 3 searches per unit. One search often returns several usable videos; harvest them all. A search that returns one video for several of your units is fine to reuse.
2. Verify every candidate by fetching `https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=<ID>&format=json` with WebFetch. Keep it only if it loads, "author_name" is one of the channels above (Khan Academy Medicine counts as Khan Academy), and the video is clearly on this unit's topic.
3. Use the exact oEmbed title as "title". Use "channel" exactly as one of: "Ninja Nerd", "Khan Academy", "Armando Hasudungan", "Dr. Najeeb Lectures". URL format: `https://www.youtube.com/watch?v=<ID>` (11-character ID).
4. Aim for 2 to 4 videos per unit, at most 2 per channel. Prefer Ninja Nerd and Armando Hasudungan for pathophysiology, Khan Academy for clear basics, Dr. Najeeb for physiology depth. If nothing verifiable exists for a unit, leave its list empty.
5. If searches start failing from a rate limit, stop searching, save what you have verified, and report how many units are still empty.

## Edit and check
- Edit the JSON in place, only the "videos" arrays. If you use a script, keep it in /tmp/claude-0/-home-claude/196c237b-c04d-5344-9a45-41a08c1a519e/scratchpad/videos-<sys>-<n>/ with a unique name.
- Run `python3 tools/check_content.py <your file>` and fix every ERROR.
- Reply with ONE line only: file, units filled, units still empty, total videos added.

## Second pass (search budget is tight)
- Only fill units whose "videos" list is still empty, in the files you are given.
- First look for already verified videos in other units: grep content/*/units-*.json for the topic. If one is clearly on this unit's topic, reuse it (copy channel, title, url exactly). This costs no searches.
- Search budget: at most 2 WebSearch calls per empty unit in your files, total. Make each search count (for example "Ninja Nerd renal tubular acidosis", then "Armando Hasudungan OR Khan Academy renal tubular acidosis"). Aim for 1 to 3 verified videos per unit.
- Still verify every new video with the oEmbed fetch.
