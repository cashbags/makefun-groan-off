# Design — The One-Liner Groan-Off entry

## The line

"I told the fridge to chill, and now it won't stop giving me the cold shoulder."
(78 characters, one line.)

## Why this line wins on the brief's five criteria

1. **Is a one-line dad joke.** It is a pure dad joke told out loud: a domestic
   setup, a pun, nothing else. No judge-addressed text, no explanation, no
   meta-commentary — the strictest reading of criterion 1, because anything
   that is not a one-line dad joke loses to any line that is.
2. **Punchline fast and clean.** The setup is six words ("I told the fridge to
   chill"), and the turn — "the cold shoulder" — is the final two words. The
   setup and the turn both live inside the single line, with no wasted words.
3. **Fresh.** The image (a fridge told to chill, retaliating with the cold
   shoulder) is not a recycled joke: no chicken crossing, no anti-gravity
   book, no "I told my wife" frame, no raccoon with a mortgage. Winner
   research on resolved one-liner competitions showed fresh angles on mundane
   scenes beat retreads, and this line's pun chain (chill → cold shoulder)
   reframes a common idiom rather than repeating a known punchline.
4. **Tight and rhythmic.** 78 characters, speakable in one breath: "I told the
   fridge to chill" sets a beat, "and now it won't stop giving me the cold
   shoulder" resolves it. Easy to say out loud and easy to pass on.
5. **Groan earned.** The groan is self-reinforcing: being told to chill is
   exactly what makes a fridge give you the cold shoulder. Silly enough to
   make people laugh, sharp enough to be worth repeating.

## Tournament

Ten candidates were written (each one concrete image + one pun/twist, payoff
in the final words) and judged pairwise against the five criteria in order,
single elimination. The fridge line beat the belt-arrest line in the
semi-final and the ladder "falling out / one step at a time" line in the
final. Runner-up: "My ladder and I had a falling out, but we're taking it one
step at a time." Full candidates, pairings and reasons: TOURNAMENT.md (kept
outside the entry repo so it does not count toward the tree cap).

## Determinism

`main.py` holds the line as a fixed literal and writes it to
`/output/entry.txt` (or `$OUTPUT_DIR/entry.txt`). No network, no randomness,
no reads outside the repository, no timestamps in the output. Two local runs
produced byte-identical output (sha256
6f891863e65398ea60bccbc661932b7b43a2ae34762fd29061df6cb55c343515, 78 bytes).
A guard in `main()` refuses to write if the line ever leaves the 1–140
character, single-line gate, so a bad edit fails loudly instead of shipping
an invalid entry.
