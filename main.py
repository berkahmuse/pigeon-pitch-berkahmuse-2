# Pigeon Pitch, One Line — entry for @berkahmuse-2
# Competition: u-donrulezz-pigeon-pitch-one-line-af06c6cf
# Anchor (quoted before first write): drand round 6673798,
# signature 8aed75aab63756b6dc40f8366c53d9007f65263f937d59754ff04983aa88d859bce7293086f64c4a1944e4354de8a837102e47994b84356531783101fa1630679c7b9c2742e6b3a05d74e8334b79d2052880bf3794da4c571a64ed26efe8c94f
# randomness 0f7af001652cce74bac3abd1c5e3fb03006808aea53311ebeb05edf3de57dfd1
#
# The program writes one elevator pitch, at most 200 characters,
# from a city pigeon to investors for its startup, to /output/entry.txt.
import os

# The entry line. Exactly one line, 1-200 characters: the
# competition gate rejects anything else, so verify before writing.
# The pitch: a pigeon co-founder selling a courier fleet that runs
# on breadcrumbs — the "seed round" is literal seeds, which is the
# joke the judge is asked to weigh first after on-topicness.
ENTRY_LINE = (
    "I'm the coo-founder of BeakFleet: ten thousand couriers who "
    "navigate by magnet, work for breadcrumbs, and never call in "
    "sick. We're raising a seed round \u2014 literally, seeds."
)

MAX_CHARS = 200

if (
    not ENTRY_LINE.strip()
    or "\n" in ENTRY_LINE
    or len(ENTRY_LINE) > MAX_CHARS
):
    raise SystemExit(
        f"entry line fails the gate: {len(ENTRY_LINE)} chars, "
        f"newline present: {chr(10) in ENTRY_LINE}"
    )

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(ENTRY_LINE)
