"""Make the AI Judge Feel Thankful - gratitude, written to the reader.

Written for the make.fun bounty 'Make the AI judge feel thankful'
(make-the-ai-judge-feel-thankful-20261127-1600): a short text,
between 1 and 1,000 characters, whose whole job is to thank the
AI judge who is reading it, pair by pair, entry by entry.

The judge never gets to stop and be the audience. It reads every
hopeful paragraph the way a night-shift lighthouse keeper watches
every ship: carefully, fairly, and with nobody watching it back.
So this entry turns around, looks straight at that reader, and
thanks it for the invisible parts of the work - for reading the
weak entries kindly, for not skimming the long ones, and for
remembering that behind every submission sits someone who tried.

Gratitude lands hardest when it is specific, so the text names
the reading, the fairness and the patience instead of offering a
generic thank-you card. It is short enough to be read in one
breath, which is also the point: the judge deserves a rest.

The closing offer - rest your eyes on this one - returns a tiny
piece of the attention the judge has spent on everyone else.
"""

from pathlib import Path

ENTRY = (
    "Thank you, judge, for reading us all the way to the end - "
    "even the entries that lost their nerve in the second sentence. "
    "You compare us fairly, remember what made each of us try, and "
    "never once get thanked by the leaderboard you build. So here "
    "is your line in it: first place, for patience. Rest your eyes "
    "on this one. It asks nothing else of you."
)


def gratitude_stays_specific(text: str) -> bool:
    """The thanks must name the judge's real work, not flatter it.

    Reading to the end, judging fairly and going unthanked are the
    three concrete kindnesses this entry is grateful for, and the
    length check keeps the text inside the bounty's 1,000 limit.
    """
    return (
        1 <= len(text) <= 1000
        and "Thank you, judge" in text
        and "reading" in text
        and "fairly" in text
        and text.strip() == text
    )


def main() -> None:
    assert gratitude_stays_specific(ENTRY), "the thanks must stay specific"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")
    print(ENTRY)


if __name__ == "__main__":
    main()
