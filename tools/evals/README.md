# EvoWrite behavior cases

These cases describe observable behavior expected from `evo-write`. They are evaluation prompts and acceptance checks, not a substitute for blind human review.

Run them in a fresh agent session after installing the Skill. Each case should be checked for:

1. factual preservation;
2. no invented evidence;
3. reduced AI tells and defensive framing;
4. EC terminology accuracy;
5. correct output mode.

The JSON file uses this schema:

- `id`: short identifier;
- `mode`: rewrite, draft, voice-match, or audit;
- `input`: prompt material;
- `must`: required behavior;
- `must_not`: forbidden behavior;
- `notes`: review guidance.
